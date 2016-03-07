from django.conf.urls import include, url
from django.contrib import admin
from inventory import views

urlpatterns = [
    # List of calls to the url() function.
    # Takes params in form of:
    # regex of the url pattern, view file, template name.
    # url is mapped to fiew and template.
    # Careful!  Django starts at the top and works down until it finds
    # a match.  The first match is the one that counts.
    url(r'^$', views.index, name = 'index'),
    # This url regex contains a named group in params.  It names the value
    # id and passes the digits as a parameter with that name.
    url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),

    # Don't have to worry about the admin urls, the include sends anything
    # which goes to 'admin/' to Djangos built in admin app.
    url(r'^admin/', include(admin.site.urls))
]
