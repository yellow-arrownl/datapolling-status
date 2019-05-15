import sys
sys.path.append("site-packages")
import requests
from requests.auth import HTTPBasicAuth

kudu_url = 'https://inzichtin.scm.azurewebsites.net/api/continuouswebjobs/datapolling'
kudu_repo ='$inzichtin'
kudu_key = 'hP5avMuFlRHi7NjrZ6BHlhSvZmu6YrlluRGQFkepAvg0o5gS4RmDnJe4SBJF'
authenication_mode = 'BasicAuth'
kr = requests.get(kudu_url,auth=HTTPBasicAuth(kudu_repo, kudu_key))
print(kr.json())