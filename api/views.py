from django.http import JsonResponse
from datetime import datetime,timezone
import pytz




def api_home(request,*args,**kwargs):
    dt=datetime.now(timezone.utc)
    weekday = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    today = weekday[dt.weekday()]
    re = request.GET
    date_time = dt.strftime("%Y-%m-%d %H:%M:%S").split(" ")

    uct_time = f"{date_time[0]}T{date_time[1]}Z"

    response = {
        "slack_name":f"{re['slack_name']}",
        "current_day":today,
        "uct_time":uct_time,
        "track":re['track'],
        "github_file_url":"https://github.com/Dober09/Api-endpoint/blob/main/backend/api/views.py",
        "github_repo_url":"https://github.com/Dober09/Api-endpoint",
        "status_code":200
    }

    # json_re = json.dumps(response)
    print(uct_time)
    
    return JsonResponse(response);
