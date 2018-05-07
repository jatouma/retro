from django.contrib import admin
from .models import Positive, Delta, ActionItem, Board
# Register your models here.

class PositiveInline(admin.TabularInline):
    model = Positive

class DeltaInline(admin.TabularInline):
    model = Delta

class ActionItemInline(admin.TabularInline):
    model = ActionItem

class BoardAdmin(admin.ModelAdmin):
    inlines = [
        PositiveInline, DeltaInline, ActionItemInline
    ]

admin.site.register(Board, BoardAdmin)

admin.site.register(Positive)
admin.site.register(Delta)
admin.site.register(ActionItem)
