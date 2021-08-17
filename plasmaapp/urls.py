from django.contrib.auth import logout
from django.urls import path

from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('acceptor/',views.acceptor,name='acceptor'),
    path('donator/',views.donator,name='donator'),
    path('admin1/',views.admin1,name='admin1'),
    path('admin1/editaccept/<username>',views.editaccept,name='editaccept'),
    # path('editaccept/sendmail/<username>',views.mailAppointment,name='mailit'),
    # path('admin1/editdoaner/<id>',views.editdoaner,name='editdoaner'),
    path('SignUp/',views.signuppage,name='signup'),
    path('login/',views.loginpage,name='loginpage'),
    path('logout/',views.logoutpage,name='logout'),
    path('customer/',views.customerpage,name='customerpage'),
    path('customer/formfill',views.formfill,name='formfill'),
    
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="reset_token.html"),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="reset_success.html"),name='password_reset_complete'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)