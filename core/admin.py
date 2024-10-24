from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models

class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["name", "email"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("name", "personal_info", "telephone", "document")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "created_at") }),
        (_("Groups"), {"fields": ("groups",)}),
        (_("User Permissions"), {"fields": ("user_permissions",)}),
    )
    readonly_fields = ["last_login", "created_at"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    "telephone",
                    "personal_info",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "document",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Category)
admin.site.register(models.DiscountCoupon)
admin.site.register(models.Service)
admin.site.register(models.Promotion)
admin.site.register(models.Room)
admin.site.register(models.Booking)
admin.site.register(models.RoomAvailability)
admin.site.register(models.BookingService)
admin.site.register(models.Cancellation)
admin.site.register(models.Payment)
admin.site.register(models.Feedback)
admin.site.register(models.BookingRoom)
admin.site.register(models.RoomPhoto)