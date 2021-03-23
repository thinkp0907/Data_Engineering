from django.contrib import admin

# Register your models here.

## parsed_data/admin.py
from django.contrib import admin
## models에서 NavpayData를 import 해옵니다.
from .models import NavpayData

## 아래의 코드를 입력하면 NavpayData를 admin 페이지에서 관리할 수 있습니다.
admin.site.register(NavpayData)