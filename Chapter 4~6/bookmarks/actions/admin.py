from django.contrib import admin
from .models import Action

# Register your models here.
class ActionAdmin(admin.ModelAdmin):
	"""docstring for ActionAdmin"""
	list_display = ('user', 'verb', 'target', 'created')
	list_filter = ('created',)
	search_fields = ('verb',)

admin.site.register(Action, ActionAdmin)