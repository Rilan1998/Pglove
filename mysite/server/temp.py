from .models import GloveData
from django.utils import timezone

json_data={'updata':
               {'username': 'ten',
                'date': '2018-11-10 12:20:20',
                'angledata': [
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1],
                    [2, 2, 2, 2, 2, 2, 2, 2, 2, 20, 2, 2, 2, 2],
                    [3, 3, 3, 3, 3, 3, 3, 3, 3, 30, 3, 3, 3, 3]
                ]
                }
           }
length = len(json_data['updata']['angledata'])
i = 0
while i < length:
    username = json_data['updata']['username']
    print(username)
    datetime = timezone.now()
    print(datetime)
    strb = [str(n) for n in json_data['updata']['angledata'][i]]
    stra=','+','.join(strb)
    angledata = stra.strip(',')
    print('%s' % angledata)
    i += 1
    data=GloveData(
        username=username,
        datetime=datetime,
        angledata=angledata
    )
    data.save()

