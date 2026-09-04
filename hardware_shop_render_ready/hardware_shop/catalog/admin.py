from django.contrib import admin

from .models import Category, Product, Enquiry


# ------------------------------------------------------------
# CATEGORY ADMIN
# ------------------------------------------------------------

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (

        "id",

        "name",

    )


# ------------------------------------------------------------
# PRODUCT ADMIN
# ------------------------------------------------------------

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):


    list_display = (

        "id",

        "name",

        "category",

        "brand",

        "price",

        "available",

        "featured",

    )


    list_filter = (

        "category",

        "finish",

        "available",

        "featured",

    )


    search_fields = (

        "name",

        "brand",

        "color",

        "description",

    )


# ------------------------------------------------------------
# ENQUIRY ADMIN
# ------------------------------------------------------------

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):


    list_display = (

        "id",

        "name",

        "phone",

        "email",

        "city",

        "created_at",

    )


    search_fields = (

        "name",

        "phone",

        "email",

    )


    readonly_fields = (

        "created_at",

    )