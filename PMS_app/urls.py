from django.urls import path

from PMS_app import views, adminviews, cusviews, ownerviews

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('ownerreg',views.ownerreg,name='ownerreg'),
    path('cusreg',views.cusreg,name='cusreg'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('ownerpage',views.ownerpage,name='ownerpage'),
    path('cuspage',views.cuspage,name='cuspage'),
    path('logout_view',views.logout_view,name='logout_view'),


    path('view_cus',adminviews.view_cus,name='view_cus'),
    path('view_owner',adminviews.view_owner,name='view_owner'),
    path('approve_cus/<int:id>/',adminviews.approve_cus,name='approve_cus'),
    path('del_cus/<int:id>/',adminviews.del_cus,name='del_cus'),
    path('approve_owner/<int:id>/',adminviews.approve_owner,name='approve_owner'),
    path('del_owner/<int:id>/',adminviews.del_owner,name='del_owner'),
    path('view_property_ad',adminviews.view_property_ad,name='view_property_ad'),
    path('approve_property/<int:id>/',adminviews.approve_property,name='approve_property'),
    path('del_property/<int:id>/',adminviews.del_property,name='del_property'),
    path('appointment_adminss',adminviews.appointment_adminss,name='appointment_adminss'),
    path('generate_bill',adminviews.generate_bill,name='generate_bill'),
    path('view_payment_details',adminviews.view_payment_details,name='view_payment_details'),
    path('Feedback_admin',adminviews.Feedback_admin,name='Feedback_admin'),
    path('reply_Feedback/<int:id>/',adminviews.reply_Feedback,name='reply_Feedback'),


    path('own_view',cusviews.own_view,name='own_view'),
    path('view_property_cus',cusviews.view_property_cus,name='view_property_cus'),
    path('view_schedule_customer',cusviews.view_schedule_customer,name='view_schedule_customer'),
    path('take_appointment/<int:id>/',cusviews.take_appointment,name='take_appointment'),
    path('appointment_view',cusviews.appointment_view,name='appointment_view'),
    path('view_bill_user',cusviews.view_bill_user,name='view_bill_user'),
    path('pay_bill/<int:id>/',cusviews.pay_bill,name='pay_bill'),
    path('pay_in_direct/<int:id>/',cusviews.pay_in_direct,name='pay_in_direct'),
    path('bill_history',cusviews.bill_history,name='bill_history'),
    path('Feedback_add_user', cusviews.Feedback_add_user, name='Feedback_add_user'),
    path('Feedback_view_user', cusviews.Feedback_view_user, name='Feedback_view_user'),


    path('property_add',ownerviews.property_add,name='property_add'),
    path('property_view_ow',ownerviews.property_view_ow,name='property_view_ow'),
    path('update_property/<int:id>/',ownerviews.update_property,name='update_property'),
    path('del_property_ow/<int:id>/',ownerviews.del_property_ow,name='del_property_ow'),
    path('cus_view_ow',ownerviews.cus_view_ow,name='cus_view_ow'),
    path('schedule_add',ownerviews.schedule_add,name='schedule_add'),
    path('schedule_view',ownerviews.schedule_view,name='schedule_view'),
    path('schedule_update/<int:id>/',ownerviews.schedule_update,name='schedule_update'),
    path('schedule_delete/<int:id>/',ownerviews.schedule_delete,name='schedule_delete'),
    path('appointment_admin', ownerviews.appointment_admin, name='appointment_admin'),
    path('approve_appointment/<int:id>/', ownerviews.approve_appointment, name='approve_appointment'),
    path('reject_appointment/<int:id>/', ownerviews.reject_appointment, name='reject_appointment'),
    path('view_bill_owner', ownerviews.view_bill_owner, name='view_bill_owner'),


]