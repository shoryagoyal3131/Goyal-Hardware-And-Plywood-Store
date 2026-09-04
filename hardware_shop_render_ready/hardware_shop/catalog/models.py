from django.db import models


# ------------------------------------------------------------
# PRODUCT CATEGORY
# ------------------------------------------------------------

class Category(models.Model):

    name = models.CharField(
        max_length=100
    )

    image = models.ImageField(
        upload_to="categories/",
        blank=True,
        null=True
    )


    def __str__(self):

        return self.name


# ------------------------------------------------------------
# PRODUCT / DESIGN
# ------------------------------------------------------------

class Product(models.Model):


    FINISH_CHOICES = [

        ("Matte", "Matte"),

        ("Glossy", "Glossy"),

        ("Wooden", "Wooden"),

        ("Textured", "Textured"),

        ("Metal", "Metal"),

        ("Other", "Other"),

    ]


    name = models.CharField(
        max_length=200
    )


    category = models.ForeignKey(

        Category,

        on_delete=models.CASCADE,

        related_name="products"

    )


    description = models.TextField(
        blank=True
    )


    brand = models.CharField(
        max_length=100,
        blank=True
    )


    color = models.CharField(
        max_length=100,
        blank=True
    )


    finish = models.CharField(

        max_length=50,

        choices=FINISH_CHOICES,

        blank=True

    )


    thickness = models.CharField(
        max_length=100,
        blank=True
    )


    size = models.CharField(
        max_length=100,
        blank=True
    )


    price = models.DecimalField(

        max_digits=10,

        decimal_places=2,

        blank=True,

        null=True

    )


    image = models.ImageField(
        upload_to="products/"
    )


    available = models.BooleanField(
        default=True
    )


    featured = models.BooleanField(
        default=False
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.name


# ------------------------------------------------------------
# ENQUIRY
# ------------------------------------------------------------

class Enquiry(models.Model):


    name = models.CharField(
        max_length=100
    )


    phone = models.CharField(
        max_length=20
    )


    email = models.EmailField(
        blank=True
    )


    city = models.CharField(
        max_length=100,
        blank=True
    )


    address = models.TextField(
        blank=True
    )


    message = models.TextField(
        blank=True
    )


    selected_products = models.TextField(
        blank=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return f"{self.name} - {self.phone}"