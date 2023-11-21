from django.urls import path
from main.views import create_product_flutter, show_main
from main.views import show_main, create_product
from main.views import show_main, create_product, show_xml
from main.views import show_main, create_product, show_xml, show_json
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_product
from main.views import delete_product
from main.views import get_product_json
from main.views import add_product_ajax
from main.views import increment, decrement, increment_ajax, decrement_ajax, delete_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('delete/<int:id>', delete_product, name='delete_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('increment/<int:products>', increment, name='increment'),
    path('decrement/<int:products>', decrement, name='decrement'),
    path('increment-ajax/<int:id>/', increment_ajax, name="increment_ajax"),
    path('decrement-ajax/<int:id>/', decrement_ajax, name="decrement_ajax"),
    path('delete-ajax/<int:id>/', delete_ajax, name="delete_ajax"),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]
