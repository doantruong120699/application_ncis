from django.shortcuts import render
from .utils import ISSUE_DATE_FINDER
# Create your views here.
def ncis(request):
    list = []
    if request.method == 'POST':
        date = request.POST['ncis'].split(',')
        print(date)
        for dt in date:
            try:
                t = ISSUE_DATE_FINDER()
                response = t.EXECUTOR(dt)
                if response == "":
                    list.append({'date':'not exist','ncis':dt})
                else:
                    list.append(response)
            except Exception as e:
                print(e)
                continue
        context = {'records':list}
        return render(request,'index.html',context)
    else:
        return render(request,'index.html',{})

