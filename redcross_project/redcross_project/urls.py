"""
URL configuration for redcross_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from blood_donate import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('administrate/',views.administrate,name="administrate"),
    path('admindashboard/',views.admindashboard,name="admindashboard"),
    # path('', views.countdown , name='countdown'),
    path('',views.homepage,name='home'),
    path('test/',views.test,name='test'),
    path('cards/',views.cards,name='cards'),
    path("footer/",views.footer,name="footer"),
    path('events/',views.event,name='events'),
    path('blood_carousel/', views.blood_carousel, name='blood_carousel'),
   
   
    path("search_blood",views.search_blood,name="search_blood"),

    path('about/',views.about,name='about'),
    
    path("basic_requires/",views.basic_requires,name="basic_requires"),
    path("additional_requires/",views.additional_requires,name="additional_requires"),
    path('requestform/',views.requestform,name="requestform"),
    path('patientrequesttable/',views.patientrequesttable,name="patientrequesttable"),
    path('patientrequestdata_delete/<int:id>',views.patientrequestdata_delete,name="patientrequestdata_delete"),


    path('get_states/<int:country_id>/', views.get_states, name='get_states'),
    path('get_districts/<int:state_id>/', views.get_districts, name='get_districts'),
    path('my_view/',views.my_view,name="my_view"),
    path('donor_register/', views.donor_register , name='donor_register'),
    path('donor_login/', views.donor_login, name='donor_login'),
    path('donor_logout/', views.donor_logout, name='donor_logout'),
    path('doner_home/',views.doner_home, name='doner_home'),


    path('donor_forget_password/', views.donor_forget_password, name='donor_forget_password'),
    path('password_reset_otp/', views.password_reset_otp, name='password_reset_otp'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('bloodA/',views.bloodA, name='bloodA'),
    path('typesofblood/',views.typesofblood , name='typesofblood'),
    path('history/',views.history ,name='history'),
    path("donator/",views.donator, name="donator"),
    path('announce/',views.announce,name="announce"),

    path('image-slider/', views.image_slider, name='image_slider'),
    path('video1/',views.video1,name="video1"),
    path('admindash/',views.admindash , name='admindash'),
    path('donation_process/',views.donation__process , name = "donation_process"),
    path('lastdonform/',views.lastdonform, name='lastdonform'),
    path('lastdonret/',views.last_don_retrieve , name="lastdonret"),
    path('update_donors/<int:donor_id>/', views.update_donors, name='update_donors'),
    path('save_image/', views.save_image, name='save_image'),
    path("__reload__/", include("django_browser_reload.urls")),

    path('additional_update/<int:id>',views.additional_update,name='additional_update'),
    path('additional_delete/<int:id>',views.additional_delete,name='additional_delete'),
    path('additional_edit/<int:id>',views.additional_edit,name='additional_edit'),
    path('additional_form/',views.additional_form,name='additional_form'),
    path('additional_table/',views.additional_table,name='additional_table'),

    path("basicform/",views.basicform,name="basicform"),
    path('basic_table/',views.basic_table,name="basic_table"),
    path('basic_update/<int:id>',views.basic_update,name='basic_update'),
    path('basic_delete/<int:id>',views.basic_delete,name='basic_delete'),
    path('basic_edit/<int:id>',views.basic_edit,name='basic_edit'),

    path('tips_update/<int:id>',views.tips_update,name='tips_update'),
    path('tips_delete/<int:id>',views.tips_delete,name='tips_delete'),
    path('tips_edit/<int:id>',views.tips_edit,name='tips_edit'),
    path('tips_form/',views.tips_form,name='tips_form'),
    path('tips_table/',views.tips_table,name="tips_table"),

    path('content_form/',views.content_form,name='content_form'),
    path('content_update/<int:id>',views.content_update,name='content_update'),
    path('content_delete/<int:id>',views.content_delete,name='content_delete'),
    path('content_edit/<int:id>',views.content_edit,name='content_edit'),

    path('contactform/', views.contactform, name='contactform'),
    path('contactupdate/<int:id>',views.contactupdate,name='contactupdate'),
    path('contactdelete/<int:id>',views.contactdelete,name='contactdelete'),
    path('contactedit/<int:id>',views.contactedit,name='contactedit'),
    path('contactretrive/',views.contactretrive,name="contactretrive"),

    path('events_update/<int:id>',views.event_update,name='events_update'),
    path('events_delete/<int:id>',views.event_delete,name='events_delete'),
    path('events_edit/<int:id>',views.event_edit,name='events_edit'),
    path('eventsform/',views.eventform, name='eventsform'),
    path('events_table/',views.event_table,name="events_table"),

    path('insertphoto/', views.insertphoto, name='insertphoto'),
    path('photo_edit/<int:id>',views.photo_edit,name='photo_edit'),
    path('photo_update/<int:id>',views.photo_update,name='photo_update'),
    path('photo_delete/<int:id>',views.photo_delete,name='photo_delete'),

    path('photo_table/',views.photo_table,name="photo_table"),
    path('insertvideo/',views.insertvideo,name="insertvideo"),
    path('video_update/<int:id>',views.video_update,name='video_update'),
    path('video_delete/<int:id>',views.video_delete,name='video_delete'),
    path('video_edit/<int:id>',views.video_edit,name='video_edit'),
    path('video_table/',views.video_table,name="video_table"),

    path('donationform/',views.donationform,name="donationform"),
    path('donationprocess_update/<int:id>',views.donationprocess_update,name='donationprocess_update'),
    path('donationprocess_delete/<int:id>',views.donationprocess_delete,name='donationprocess_delete'),
    path('donationprocess_edit/<int:id>',views.donationprocess_edit,name='donationprocess_edit'),
    path('donationprocess_table/',views.donationprocess_table,name="donationprocess_table"),



    path('announcements_insert_form/',views.announcements_insert_form,name='announcements_insert_form'),
    path('announcements_edit/<int:id>',views.announcements_edit,name="announcements_edit"),
    path('announcements_update_form/<int:id>',views.announcements_update_form,name="announcements_update_form"),
    path('announcements_delete/<int:id>',views.announcements_delete,name="announcements_delete"),   
    path('announcements_retrive_table/',views.announcements_retrive_table,name="announcements_retrive_table"),


    path('blood_carousel/', views.blood_carousel, name='blood_carousel'),
    path('blood_carousel_img_table/',views.blood_carousel_img_table,name='tblood_carousel_img_tableable'),
    path('blood_carousel_img_form/',views.blood_carousel_img_form,name='blood_carousel_img_form'),
    path('blood_carousel_img_edit/<int:id>',views.blood_carousel_img_edit,name="blood_carousel_img_edit"),
    path('blood_carousel_img_update/<int:id>',views.blood_carousel_img_update,name="blood_carousel_img_update"),
    path('blood_carousel_img_delete/<int:id>',views.blood_carousel_img_delete,name="blood_carousel_img_delet"),




    path('contactus_form/',views.contactus_form,name='contactus_form'),
    path('contactusadmin/',views.contactusadmin,name='contactusadmin'),
    path('contactus_update/<int:id>',views.contactus_update,name='contactus_update'),
    path('contactus_delete/<int:id>',views.contactus_delete,name='contactus_delete'),
    path('contactus_edit/<int:id>',views.contactus_edit,name='contactus_edit'),
    path('contactus_table/',views.contactus_table,name="contactus_table"),
    path('contactdelete/<int:id>',views.contactdelete,name="contactdelete"),


    path('registerretrive/',views.registerretrive,name="registerretrive"),
    path('hidedonor/<int:id>/',views.hidedonor,name="hidedonor"),
    path('showdonor/<int:id>/',views.showdonor,name="showdonor"),
    path('registerdelete/<int:id>/', views.registerdelete, name='registerdelete'),
    path('table-to-excel/',views.table_to_excel, name='table_to_excel'),

    path('aboutus_form/',views.aboutus_form,name='aboutus_form'),
    path('aboutus_update/<int:id>',views.aboutus_update,name='aboutus_update'),
    path('aboutus_delete/<int:id>',views.aboutus_delete,name='aboutus_delete'),
    path('aboutus_edit/<int:id>',views.aboutus_edit,name='aboutus_edit'),
    path('aboutus_table/',views.aboutus_table,name="aboutus_table"),
    
    path('historyform/',views.historyform,name="historyform"),
    path('history_table/',views.history_table,name="history_table"),
    path('history_update/<int:id>',views.history_update,name='history_update'),
    path('history_delete/<int:id>',views.history_delete,name='history_delete'),
    path('history_edit/<int:id>',views.history_edit,name='history_edit'),

    path('bloodtypesform/',views.bloodtypesform,name='bloodtypesform'),
    path('bloodtyperetrieve/',views.bloodtyperetrieve,name="bloodtyperetrieve"),
    path('bloodtypesupdate/<int:id>',views.bloodtypesupdate,name="bloodtypesupdate"),
    path('bloodtypesedit/<int:id>',views.bloodtypesedit,name="bloodtypesedit"),
    path('bloodtypesdelete/<int:id>',views.bloodtypesdelete,name="bloodtypesdelete"),

    path('donorsform/',views.donorsform,name='donorsform'),
    path('donorsretrieve/',views.donorsretrieve,name="donorsretrieve"),
    path('donorsupdate/<int:id>',views.donorsupdate,name="donorsupdate"),
    path('donorsedit/<int:id>',views.donorsedit,name="donorsedit"),
    path('donorsdelete/<int:id>',views.donorsdelete,name="donorsdelete"),
    
     path('read/<int:id>/',views.read,name="read"),
    path('readhide/<int:id>/',views.readhide,name="readhide"),
    path('my_view/',views.my_view,name='my_view'),
    path('evebloodshow/<int:id>/',views.evebloodshow, name="evebloodshow"),
    path('evebloodhide1/<int:id>/',views.evebloodhide1,name="evebloodhide1"),
    path('bloodlistshow/<int:id>/',views.bloodlistshow,name="bloodlistshow1"),
    path('bloodlisthide/<int:id>/',views.bloodlisthide,name="bloodlisthide"),
    path('gallashow/<int:id>/',views.gallashow,name="gallashow"),
    path('gallahide/<int:id>/',views.gallahide,name="gallahide"),
    path('contshow/<int:id>/',views.contshow,name="contshow"),
    path('conthide/<int:id>/',views.conthide,name="conthide"),
    path('adminuser_register/',views.admin_register,name="admin_register"),
    path('search_user/',views.search_user,name="search_user"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('logout_admin/',views.logout_admin, name="logout_admin"),
    path('nav_list/',views.nav_list, name="nav_list"),
    path('footer_table/',views.footer_table, name="footer_table"),
    path('update_donors/<int:donor_id>/', views.update_donors, name='update_donors'),
    path('donor_details/<int:donor_id>/', views.donor_details, name='donor_details'),
    path('nav_update/<int:pk>/', views.nav_update, name='nav_update'),
    path('nav_delete/<int:pk>/', views.nav_delete, name='nav_delete'),
    path('change_password/',views.change_password, name="change_password"),


   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
