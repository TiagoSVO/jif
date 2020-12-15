from django.contrib import admin
from django.contrib.admin.forms import AdminPasswordChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, JIFProfile
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group


class JIFUserProfile(admin.StackedInline):
    model = User.jif_profiles.through
    extra = 0


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm

    exclude = ['last_login', 'groups']

    fieldsets = (
        (None, {'fields': ('siape', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name',
                                             'cpf', 'rg', 'is_staff',
                                             'is_active', 'sex', 'dept')}),
        ('Acesso', {'fields': ('last_sign_in_ip',
                               'last_sign_in_at',
                               'current_sign_in_ip',
                               'current_sign_in_at')}),
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
        ('Permissões', {'fields': ('user_permissions',)}),
    )

    readonly_fields = [
        'last_sign_in_ip',
        'last_sign_in_at',
        'current_sign_in_ip',
        'current_sign_in_at',
    ]

    inlines = [JIFUserProfile, ]

    search_fields = ('siape',)
    ordering = ('siape',)
    filter_horizontal = ()

    def get_queryset(self, request):
        qs = super(CustomUserAdmin, self).get_queryset(request)
        if request.user.is_superuser is not True:
            qs = qs.filter(pk=self.id)
        return qs


@admin.register(JIFProfile)
class JIFProfileAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Group)
