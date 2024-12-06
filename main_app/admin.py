from django.contrib import admin

from main_app.models import Fundraiser

# Register your models here.

admin.site_header = 'CrowdFund Administration'
admin.site.site_title = 'Crowdy Admin'


class FundraiserAdmin(admin.ModelAdmin):
    list_display = ['first_name',
                    'last_name',
                    'email',
                    'gender',
                    'dob']
    search_fields = ['first_name',
                     'last_name',
                     'email']
    list_filter = ['gender']
    list_per_page = 20





admin.site.register(Fundraiser, FundraiserAdmin)


# python manage.py --help

# python manage.py createsuperuser
# admin@gmail.com
# 123456

# localhost:8000/admin

# 1a2Bc9*33aa!!
from django.contrib import admin

# Register your models here.
