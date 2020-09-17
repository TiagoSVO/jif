from django.contrib import admin
from django.contrib.admin.forms import AdminPasswordChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserCreationForm, UserChangeForm


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm

    exclude = ['last_login']

    fieldsets = (
        (None, {'fields': ('siape', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name',
                                             'cpf', 'rg', 'is_staff',
                                             'is_active', 'sex', 'dept')}),
        ('Acesso', {'fields': ('last_sign_in_ip',
                               'last_sign_in_at',
                               'current_sign_in_ip',
                               'current_sign_in_at')}),
        ('Grupoes', {'fields': ('groups',)}),
        ('Permissões', {'fields': ('user_permissions',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('siape', 'password1', 'password2')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name',
                                             'cpf', 'rg', 'is_staff',
                                             'is_active', 'sex', 'dept')}),
        ('Acesso', {'fields': ('last_sign_in_ip',
                               'last_sign_in_at',
                               'current_sign_in_ip',
                               'current_sign_in_at')}),
        ('Grupoes', {'fields': ('groups',)}),
        ('Permissões', {'fields': ('user_permissions',)}),
    )

    readonly_fields = [
        'last_sign_in_ip',
        'last_sign_in_at',
        'current_sign_in_ip',
        'current_sign_in_at',
    ]

    search_fields = ('siape',)
    ordering = ('siape',)
    filter_horizontal = ()

    def get_queryset(self, request):
        qs = super(CustomUserAdmin, self).get_queryset(request)
        if request.user.is_superuser is not True:
            qs = qs.filter(pk=self.id)
        return qs

