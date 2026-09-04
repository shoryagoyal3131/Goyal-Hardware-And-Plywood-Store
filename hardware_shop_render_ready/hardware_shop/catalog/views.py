from django.shortcuts import (

    render,

    redirect,

    get_object_or_404

)

from django.db.models import Q

from urllib.parse import quote

from .models import (

    Category,

    Product,

    Enquiry

)


# ============================================================
# IMPORTANT
# CHANGE THIS TO YOUR OWN WHATSAPP NUMBER
#
# Example:
# 919876543210
#
# No +
# No spaces
# ============================================================

WHATSAPP_NUMBER = "919999999999"


# ============================================================
# HOME PAGE
# ============================================================

def home(request):


    categories = Category.objects.all()


    featured_products = Product.objects.filter(

        available=True,

        featured=True

    ).order_by(

        "-created_at"

    )[:8]


    latest_products = Product.objects.filter(

        available=True

    ).order_by(

        "-created_at"

    )[:8]


    selected_ids = request.session.get(

        "selected_products",

        []

    )


    return render(

        request,

        "catalog/home.html",

        {

            "categories": categories,

            "featured_products": featured_products,

            "latest_products": latest_products,

            "selection_count": len(selected_ids),

        }

    )


# ============================================================
# PRODUCT LIST
# SEARCH + FILTERS
# ============================================================

def products(request):


    product_list = Product.objects.filter(

        available=True

    )


    search = request.GET.get(

        "search",

        ""

    )


    category = request.GET.get(

        "category",

        ""

    )


    color = request.GET.get(

        "color",

        ""

    )


    finish = request.GET.get(

        "finish",

        ""

    )


    min_price = request.GET.get(

        "min_price",

        ""

    )


    max_price = request.GET.get(

        "max_price",

        ""

    )


    # SEARCH


    if search:


        product_list = product_list.filter(

            Q(

                name__icontains=search

            )

            |

            Q(

                description__icontains=search

            )

            |

            Q(

                brand__icontains=search

            )

            |

            Q(

                color__icontains=search

            )

        )


    # CATEGORY FILTER


    if category:


        product_list = product_list.filter(

            category_id=category

        )


    # COLOR FILTER


    if color:


        product_list = product_list.filter(

            color__icontains=color

        )


    # FINISH FILTER


    if finish:


        product_list = product_list.filter(

            finish=finish

        )


    # PRICE FILTER


    if min_price:


        product_list = product_list.filter(

            price__gte=min_price

        )


    if max_price:


        product_list = product_list.filter(

            price__lte=max_price

        )


    categories = Category.objects.all()


    selected_ids = request.session.get(

        "selected_products",

        []

    )


    return render(

        request,

        "catalog/products.html",

        {

            "products": product_list,

            "categories": categories,

            "selection_count": len(selected_ids),

        }

    )


# ============================================================
# PRODUCT DETAIL
# ============================================================

def product_detail(request, product_id):


    product = get_object_or_404(

        Product,

        id=product_id,

        available=True

    )


    selected = request.session.get(

        "selected_products",

        []

    )


    is_selected = product.id in selected


    return render(

        request,

        "catalog/product_detail.html",

        {

            "product": product,

            "is_selected": is_selected,

        }

    )


# ============================================================
# ADD DESIGN TO SELECTION
# ============================================================

def add_to_selection(request, product_id):


    product = get_object_or_404(

        Product,

        id=product_id

    )


    selected = request.session.get(

        "selected_products",

        []

    )


    if product.id not in selected:


        selected.append(

            product.id

        )


    request.session[

        "selected_products"

    ] = selected


    request.session.modified = True


    return redirect(

        request.META.get(

            "HTTP_REFERER",

            "my_selection"

        )

    )


# ============================================================
# REMOVE DESIGN
# ============================================================

def remove_from_selection(request, product_id):


    selected = request.session.get(

        "selected_products",

        []

    )


    if product_id in selected:


        selected.remove(

            product_id

        )


    request.session[

        "selected_products"

    ] = selected


    request.session.modified = True


    return redirect(

        "my_selection"

    )


# ============================================================
# MY SELECTED DESIGNS
# ============================================================

def my_selection(request):


    selected_ids = request.session.get(

        "selected_products",

        []

    )


    products = Product.objects.filter(

        id__in=selected_ids

    )


    return render(

        request,

        "catalog/my_selection.html",

        {

            "products": products,

            "selection_count": len(selected_ids),

        }

    )


# ============================================================
# CUSTOMER ENQUIRY
# ============================================================

def enquiry(request):


    selected_ids = request.session.get(

        "selected_products",

        []

    )


    products = Product.objects.filter(

        id__in=selected_ids

    )


    if request.method == "POST":


        name = request.POST.get(

            "name"

        )


        phone = request.POST.get(

            "phone"

        )


        email = request.POST.get(

            "email"

        )


        city = request.POST.get(

            "city"

        )


        address = request.POST.get(

            "address"

        )


        message = request.POST.get(

            "message"

        )


        product_names = ", ".join(

            product.name

            for product in products

        )


        # SAVE ENQUIRY


        Enquiry.objects.create(

            name=name,

            phone=phone,

            email=email,

            city=city,

            address=address,

            message=message,

            selected_products=product_names

        )


        # CREATE WHATSAPP MESSAGE


        whatsapp_message = f'''

NEW CUSTOMER ENQUIRY

Name: {name}

Phone: {phone}

Email: {email}

City: {city}

Address:
{address}

SELECTED DESIGNS:
{product_names}

ADDITIONAL REQUIREMENTS:
{message}

'''


        whatsapp_url = (

            "https://wa.me/"

            + WHATSAPP_NUMBER

            + "?text="

            + quote(

                whatsapp_message

            )

        )


        # CLEAR SELECTION


        request.session[

            "selected_products"

        ] = []


        request.session.modified = True


        return render(

            request,

            "catalog/success.html",

            {

                "customer_name": name,

                "whatsapp_url": whatsapp_url,

            }

        )


    return render(

        request,

        "catalog/enquiry.html",

        {

            "products": products,

        }

    )