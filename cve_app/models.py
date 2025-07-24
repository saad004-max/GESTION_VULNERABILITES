from django.db import models

class CVE(models.Model):
    cve_id = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    severity = models.CharField(max_length=50, null=True, blank=True)
    cvss_score = models.FloatField(null=True, blank=True)
    published_date = models.DateTimeField()
    last_modified = models.DateTimeField()
    references = models.TextField(blank=True)

    def __str__(self):
        return self.cve_id