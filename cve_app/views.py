from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CVE

@login_required
def dashboard(request):
    total_cves = CVE.objects.count()
    critical_cves = CVE.objects.filter(cvss_score__gte=7.0).count()
    # You can add more stats if you want
    context = {
        'total_cves': total_cves,
        'critical_cves': critical_cves,
    }
    return render(request, 'cve_app/dashboard.html', context)


@login_required
def cve_list(request):
    severity = request.GET.get('severity')
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')

    cves = CVE.objects.all()

    if severity:
        cves = cves.filter(severity__iexact=severity)

    if date_from:
        cves = cves.filter(published_date__gte=date_from)

    if date_to:
        cves = cves.filter(published_date__lte=date_to)

    cves = cves.order_by('-published_date')

    return render(request, 'cve_app/cve_list.html', {'cves': cves})


@login_required
def cve_detail(request, cve_id):
    cve = get_object_or_404(CVE, cve_id=cve_id)
    return render(request, 'cve_app/cve_detail.html', {'cve': cve})
