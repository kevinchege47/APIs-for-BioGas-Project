from cgitb import lookup
import django_filters
from django_filters import DateFilter,CharFilter
from .models import *
class RoleFilter(django_filters.FilterSet):
    
    role = CharFilter(field_name='role',lookup_expr= 'icontains')
    class Meta:
        model = Users
        fields = '__all__'
        exclude = ['date_created']