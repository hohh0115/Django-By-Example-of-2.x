# Django-By-Example-of-2.x
《Django By Example》在Django 2.0版本以上的練習

## 章節劃分 ##

在《Django By Example》這本書裡面總共會有4個成品：

1. 第一章到第三章：一個Blog網站
2. 第四章到第六章：一個包含會員系統、會員互動追蹤和標記及上傳圖片的網站(Bookmarks)
3. 第七章到第九章：一個購物網站
4. 第十章到第十二章：一個e-Learning平台

## 練習中跳過的功能 ##

《Django By Example》是2015年年底所出版的，有些套件功能早就不如書中所述，再加上不是那麼必要(可替代)，所以以下的功能就是先跳過：

第一章到第三章的Blog:

1. 使用Solr和Haystack做一個搜尋引擎

第四章到第六章：

1. Adding social authentication to your site: 需要SSL憑證

第七章到第九章：

1. Integrating a payment gateway: 金流串接
2. Generating PDF invoices dynamically：在windows上使用這個套件太坑人了，沒辦法用
3. Translating models with django-parler:
	1. 在Creating a custom migration這節中，對繼承由django-parler提供的TranslatableModel的自定義model做migrations時，會出現這樣的錯誤：The model 'Category' already has a field named 'name'，這是因為該model中有出現重複的欄位名稱，可以依照[https://github.com/django-parler/django-parler/issues/154](https://github.com/django-parler/django-parler/issues/154)裡面提供的小技巧解決
	2. 令我放棄的錯誤是這一小節：Adapting views for translations，會出現unhashable type: 'list'，依照Django的錯誤頁面依循路徑去查找，還是找不到問題。

## 備註 ##

### 2.0以及2.1下認證框架(authentication framework)的import ###
Django 2.0以前:
![image](https://raw.githubusercontent.com/hohh0115/Django-By-Example-of-2.x/master/media/before.png)
Django 2.1:
![image](https://raw.githubusercontent.com/hohh0115/Django-By-Example-of-2.x/master/media/Image.png)

說明：

1. [https://docs.djangoproject.com/en/2.1/releases/2.1/#features-removed-in-2-1](https://docs.djangoproject.com/en/2.1/releases/2.1/#features-removed-in-2-1)
2. 在2.1版本之中，contrib.auth.views.login(), logout(), password_change(), password_change_done(), password_reset(), password_reset_done(), password_reset_confirm(), and password_reset_complete() are removed.
3. 在2.0之前的寫法是使用的login()去調用LoginView class的as_view()，在2.1之後是直接調用LoginView class的as_view()，login()就被移除了