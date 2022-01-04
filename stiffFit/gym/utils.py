from .models import *
def getMsg(request):
    # Notification
    data=Notify.objects.all().order_by('-id')
    notifStatus=False
    jsonData=[]
    totalUnread=0
    for d in data:
        try:
            notifStatusData=NotifUserStatus.objects.get(user=request.user,notif=d)
            if notifStatusData:
                notifStatus=True
        except NotifUserStatus.DoesNotExist:
            notifStatus=False
            if not notifStatus:
                totalUnread=totalUnread+1
    return totalUnread 