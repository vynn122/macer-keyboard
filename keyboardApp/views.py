from django.shortcuts import redirect, render
from rest_framework import viewsets
from .models import *
from .serializers import *
from appApi.views.keyboardAppViews.middlewareViews import Cookie_validation_middleware
from appApi.views.keyboardAppViews.authViews import admin_only_view, user_only_view, user_or_guest_view
from rest_framework.parsers import MultiPartParser, FormParser
from django.conf import settings
import os





# Create your views here.
@user_or_guest_view
def shop_page(request):
    return render(request, 'shop.html')

def login_page(request):
    return render(request, 'login.html')

def signup_page(request):
    return render(request, 'signup.html')

def header_page(request):
    return render(request, 'navigation/header.html')

def home_page(request):
    return render(request, 'home.html')
@user_or_guest_view
def about_page(request):
    return render(request, 'about.html')

def footer_page(request):
    return render(request, 'navigation/footer.html')
@user_only_view
def checkout_page(request):
    return render(request, 'checkout.html')
@user_only_view
def history_page(request):
    return render(request, 'history.html')

def forbidden_430_view(request):
    return render(request, '430.html')


# class ItemView(viewsets.ModelViewSet):
#     queryset = Store_item.objects.all()
#     serializer_class = ItemSerializer
#     parser_classes = [MultiPartParser, FormParser]
#     def get_queryset(self):
#         return Store_item.objects.all()

#     def perform_create(self, serializer):
#         item_image = self.request.FILES.get('item_image')

#     # Step 1: Save the object without the image to get item_id
#         instance = serializer.save()  # item_id is generated here

#         if item_image:
#         # Step 2: Construct filename using item_id
#             filename = f"keyboard{instance.item_id}.png"
#             image_dir = os.path.join(settings.MEDIA_ROOT, 'keyboardApp/static/img/keyboardImg/')
#             image_path = os.path.join(image_dir, filename)

#         # Step 3: Ensure directory exists
#             os.makedirs(image_dir, exist_ok=True)

#         # Step 4: Save image file manually
#             with open(image_path, 'wb+') as destination:
#                 for chunk in item_image.chunks():
#                     destination.write(chunk)

#         # Step 5: Update image path and save again
#         instance.item_image = f"keyboardApp/static/img/keyboardImg/{filename}"
#         instance.save()

#         print(f"Image saved successfully: {instance.item_image}")
    

#     def perform_update(self, serializer):
#         item_image = self.request.FILES.get('item_image')
#         instance = serializer.save()
#         if item_image:
#             try:
#                 filename = f"keyboard{instance.item_id}.png"
#                 image_dir = os.path.join(settings.MEDIA_ROOT, 'keyboardApp/static/img/keyboardImg/')
#                 os.makedirs(image_dir, exist_ok=True)
#                 image_path = os.path.join(image_dir, filename)

#                 with open(image_path, 'wb+') as destination:
#                     for chunk in item_image.chunks():
#                         destination.write(chunk)

#                 instance.item_image = f"keyboardApp/static/img/keyboardImg/{filename}"
#                 instance.save()
#                 print(f"Updated image: {instance.item_image}")

#             except Exception as e:
#                 print(f"Error saving image file: {e}")
#             # optionally raise or handle error properly here


    


     

# @Cookie_validation_middleware
# @admin_only_view
# def admin_panel_page(request):
#     return render(request, "admindash.html")  

from django.shortcuts import redirect, render
from rest_framework import viewsets
from .models import *
from .serializers import *
from appApi.views.keyboardAppViews.middlewareViews import Cookie_validation_middleware
from appApi.views.keyboardAppViews.authViews import (
    admin_only_view,
    user_only_view,
    user_or_guest_view
)
from rest_framework.parsers import MultiPartParser, FormParser


class ItemView(viewsets.ModelViewSet):
    queryset = Store_item.objects.all()
    serializer_class = ItemSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return Store_item.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

@Cookie_validation_middleware
@admin_only_view
def admin_panel_page(request):
    return render(request, "admindash.html")  