from django.contrib import admin
from .models import CVE

@admin.register(CVE)
class CVEAdmin(admin.ModelAdmin):
    list_display = ('cve_id', 'severity', 'cvss_score', 'published_date')
    search_fields = ('cve_id', 'description')
