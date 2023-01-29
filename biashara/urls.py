from django.urls import include, re_path
from . import views

urlpatterns = [
   
     re_path('all_borrowers/',views.get_all_borrowers ,name='all_borrowers'),
     re_path('single_borrower/(?P<borrower_id>[0-9]+)/$',views.get_borrowers_by_id ,name='single_borrower'),
     re_path('all_business',views.get_all_business ,name='all_business'),
     re_path('single_business/(?P<business_id>[0-9]+)/$',views.get_business_by_id ,name='single_business'),
     re_path('all_loans',views.get_all_loans ,name='all_loans'),
     re_path('single_loan/(?P<loan_id>[0-9]+)/$',views.get_loan_by_id ,name='single_loan'),
  
    
]
