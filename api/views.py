from django.http import JsonResponse
from datetime import datetime,timezone
import pytz




def api_home(request,*args,**kwargs):
    dt=datetime.now(timezone.utc)
    weekday = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    today = weekday[dt.weekday()]
    re = request.GET
    date_time = dt.strftime("%Y-%m-%dT%H:%M:%SZ")
   

    response = {
        "slack_name":f"{re['slack_name']}",
        "current_day":today,
        "utc_time":date_time,
        "track":re['track'],
        "github_file_url":"https://github.com/Dober09/Api-endpoint/blob/main/backend/api/views.py",
        "github_repo_url":"https://github.com/Dober09/Api-endpoint",
        "status_code":200
    }

    # json_re = json.dumps(response)
    print(date_time)
    
    return JsonResponse(response);
