from django.shortcuts import render
import json
from .models import GloveData
from django.http import HttpResponse
from django.utils import timezone
# Create your views here.


def index(request):

    if request.method == 'GET':
        return HttpResponse("干嘛鸭.")
    if request.method == 'POST':
        postBody = request.body

        json_data = json.loads(postBody)

        length = len(json_data['updata']['angledata'])
        i = 0
        strc=""
        while i < length:
            username = json_data['updata']['username']
            print(username)
            datetime = timezone.now()
            print(datetime)
            strb = [str(n) for n in json_data['updata']['angledata'][i]]
            stra = ',' + ','.join(strb)
            angledata = stra.strip(',')
            print('%s' % angledata)
            i += 1
            data = GloveData(
                username=username,
                datetime=datetime,
                angledata=angledata
            )
            data.save()
            strc=strc+","+str(data.id)

        strd=strc.strip(',')
        return HttpResponse(strd)

