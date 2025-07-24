import requests

API_URL = "https://api.nvd.nist.gov/rest/json/cves/2.0"

try:
    response = requests.get(API_URL, params={"resultsPerPage": 1})
    print(f"Status code: {response.status_code}")
    print(response.json())
except Exception as e:
    print(f"Erreur : {e}")
