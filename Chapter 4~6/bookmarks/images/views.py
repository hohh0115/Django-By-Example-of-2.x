from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from common.decorators import ajax_required
from .forms import ImageCreateForm
from .models import Image
from django.http import HttpResponse
from actions.utils import create_action
import redis

# connect to redis
r = redis.StrictRedis(host=settings.REDIS_HOST,
                      port=settings.REDIS_PORT,
                      db=settings.REDIS_DB)
# r.flushall() Delete all keys in all databases on the current host
# r.flushdb() Delete all keys in the current database

@login_required
def image_create(request):
    """
    View for creating an Image using the JavaScript Bookmarklet.
    """
    if request.method == 'POST': # form is sent
        form = ImageCreateForm(data=request.POST) # type(form) = <class 'images.forms.ImageCreateForm'>
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            new_item = form.save(commit=False) # ImageCreateForm.save(), type(new_item) = <class 'images.models.Image'>
            # assign current user to the item
            new_item.user = request.user
            new_item.save() # Image.save()
            create_action(request.user, 'bookmarked image', new_item)
            messages.success(request, 'Image added successfully')
            # redirect to new created item detail view
            return redirect(new_item.get_absolute_url())
    else:
        # build form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET)

    return render(request, 'images/image/create.html', {'section': 'images',
                                                        'form': form})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    # increment total image views by 1
    total_views = r.incr('image:{}:views'.format(image.id))
    # increment image ranking by 1
    r.zincrby('image_ranking', image.id, 1)
    return render(request, 'images/image/detail.html', {'section': 'images',
                                                        'image': image,
                                                        'total_views': total_views})

@ajax_required
@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
                create_action(request.user, 'likes', image)
            else:
                image.users_like.remove(request.user)
        except:
            pass

    return JsonResponse({'status':'ok'})

@login_required
def image_list(request):
    num_images = 8 # how many images
    images = Image.objects.all()
    paginator = Paginator(images, num_images)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger: # If page is not an integer deliver the first page
        images = paginator.page(1)
    except EmptyPage: # the page is out of range
        if request.is_ajax(): # If the request is AJAX, return an empty page
            return HttpResponse('')
        images = paginator.page(paginator.num_pages)

    render_params = {'section':'images', 'images':images}
    if request.is_ajax():
        return render(request, 'images/image/list_ajax.html', render_params)

    return render(request, 'images/image/list.html', render_params)

@login_required
def image_ranking(request):
    # get image ranking dictionary
    image_ranking = r.zrange('image_ranking', 0, -1, desc=True)[:10]
    image_ranking_ids = [int(id) for id in image_ranking]
    # get most viewed images
    most_viewed = list(Image.objects.filter(id__in=image_ranking_ids))
    most_viewed.sort(key=lambda x: image_ranking_ids.index(x.id))

    response_params = {'section': 'images', 'most_viewed': most_viewed}
    return render(request, 'images/image/ranking.html', response_params)