from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.views',
    #PUT
    url(r'^todo/(?P<tid>[0-9]+)', 'update_create_delete_get', name='update'),

    #DELETE
    url(r'^todo/(?P<tid>[0-9]+)', 'update_create_delete_get', name='delete'),

    # GET One
    url(r'^todo/(?P<tid>[0-9]+)', 'update_create_delete_get', name='get_one'),

    #POST
    url(r'^todo$', 'create_new', name='create'),

    # GET All
    url(r'^todos', 'get_all', name='get_all'),
)
