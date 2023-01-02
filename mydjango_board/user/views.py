from django.http import HttpResponse

def index(request):
    user_profile = {
        '이름':'수경',
        '별명':'sk'

    }
    result = "<h3>나의 프로필</h3> <ul>"
    for k, v in user_profile.items():
        result += f"<li>{k}:{v}</li>"
    result += "</ul>"
    return HttpResponse(result)