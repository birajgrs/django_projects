from django.contrib import admin
from .models import Employee, Role, Department
# admin.site.register(model_name)
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)


