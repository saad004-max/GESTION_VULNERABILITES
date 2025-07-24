import json
from .models import CVE  # adapte selon ton projet Django
from datetime import datetime

def load_cves_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Les vulnérabilités sont sous la clé 'CVE_Items'
    cve_items = data.get("CVE_Items", [])

    for item in cve_items:
        cve_info = item.get("cve", {})
        cve_id = cve_info.get("CVE_data_meta", {}).get("ID", "")
        
        descriptions = cve_info.get("description", {}).get("description_data", [])
        description = descriptions[0]["value"] if descriptions else ""

        published_date = item.get("publishedDate", None)
        modified_date = item.get("lastModifiedDate", None)

        # CVSS info (version 3.1 ou autre)
        impact = item.get("impact", {})
        baseMetricV3 = impact.get("baseMetricV3", {})
        cvss_v3 = baseMetricV3.get("cvssV3", {})
        cvss_score = cvss_v3.get("baseScore", None)
        severity = cvss_v3.get("baseSeverity", None)

        # Évite doublons
        if not CVE.objects.filter(cve_id=cve_id).exists():
            CVE.objects.create(
                cve_id=cve_id,
                description=description,
                published_date=published_date,
                last_modified=modified_date,
                cvss_score=cvss_score,
                severity=severity,
                references="; ".join(ref["url"] for ref in cve_info.get("references", {}).get("reference_data", []))
            )
    print(f"{len(cve_items)} CVEs imported from {filepath}")
