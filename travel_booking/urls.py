from django.contrib import admin
from django.urls import path, include
from trips.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),        # ✅ HOME
    path("trips/", include("trips.urls")),
    path("bookings/", include("bookings.urls")),
    path("accounts/", include("accounts.urls")),
]


# from django.contrib import admin
# from django.urls import path, include
# from django.shortcuts import redirect  # IMPORTANT

# # 👇 DEFINE home BEFORE urlpatterns
# def home(request):
#     return redirect('/accounts/login/')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', home, name='home'),
#     path('accounts/', include('accounts.urls')),
#     path('trips/', include('trips.urls')),
#     path('bookings/', include('bookings.urls')),
# ]
