from django.urls import path

from . import views


urlpatterns = [


    path(

        "",

        views.home,

        name="home"

    ),


    path(

        "products/",

        views.products,

        name="products"

    ),


    path(

        "product/<int:product_id>/",

        views.product_detail,

        name="product_detail"

    ),


    path(

        "select/<int:product_id>/",

        views.add_to_selection,

        name="add_to_selection"

    ),


    path(

        "remove/<int:product_id>/",

        views.remove_from_selection,

        name="remove_from_selection"

    ),


    path(

        "my-selection/",

        views.my_selection,

        name="my_selection"

    ),


    path(

        "enquiry/",

        views.enquiry,

        name="enquiry"

    ),

]