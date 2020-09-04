from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = [
        'siape',
        'email',
        'password',
        'cpf',
        'rg',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        'sex',
        'dept',
        'last_sign_in_ip',
        'last_sign_in_at',
        'current_sign_in_ip',
        'current_sign_in_at'
    ]
    exclude = ['last_login']
    readonly_fields = [
        'last_sign_in_ip',
        'last_sign_in_at',
        'current_sign_in_ip',
        'current_sign_in_at',
    ]

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        if request.user.is_superuser is not True:
            qs = qs.filter(pk=self.id)
        return qs


