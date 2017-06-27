from django.shortcuts import render
from sqlModels.models import ServerList
from django.shortcuts import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
import json
import time
import logging


def logServerRevise(request, id):
    logger = logging.getLogger("sql")
    logger.info("%s : revise server %s", request.user.username, id)


def logServerNew(request, id):
    logger = logging.getLogger("sql")
    logger.info("%s : create server %s", request.user.username, id)


def logServerDelete(request, id):
    logger = logging.getLogger("sql")
    logger.info("%s : delete server %s", request.user.username, id)


# 删除一个服务器条目（is_used设置为0）
@login_required
def serverConfigDelete(request):
    id = request.POST.get("id", "-1")
    # 查找该项目是否存在
    targetData = ServerList.objects.filter(id=id)
    if len(targetData) > 0:
        for data in targetData:
            data.is_used = 0
            data.save()
            logServerDelete(request,data.id)
    return HttpResponseRedirect('/serverConfigSearch/')


# 新增或者更改条目
# 表单中id为-1为新增，否则为更改
@login_required
def handleServerRevise(request):
    ip = request.POST.get("ip", "")
    port = request.POST.get("port", "")
    idc = request.POST.get("idc", "")
    sign = request.POST.get("sign", "")

    updateTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    registrationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    id = request.POST.get("id", "-1")
    # 查找该项目是否存在
    targetData = ServerList.objects.filter(id=id)

    if len(targetData) > 0:
        for data in targetData:
            data.ip = ip
            data.port = port
            data.idc = idc
            data.sign = sign
            data.update_time = updateTime
            data.save()
            logServerRevise(request,data.id)

    else:
        data=ServerList.objects.create(
            update_time=updateTime,
            registration_time=registrationTime,
            ip=ip,
            port=port,
            idc=idc,
            sign=sign,
            is_used=1
        )
        logServerNew(request,data.id)


# 显示更改服务器信息主界面
@login_required
def serverConfigRevise(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        ip = request.POST.get('ip')
        port = request.POST.get('port')
        idc = request.POST.get('idc')
        sign = request.POST.get('sign')

        targetData = ServerList.objects.filter(ip=ip, port=port, idc=idc, sign=sign)

        if len(targetData) > 0:
            return_json = {'result': False}
            return JsonResponse(return_json)
        else:
            handleServerRevise(request)
            return_json = {'result': True}
            return JsonResponse(return_json)
    else:
        id = request.GET.get("id", "-1")

        return render(request, 'serverConfig/serverConfigRevise.html',
                      {"id": id,
                       "allServer": ServerList.objects.all()
                       })



# 显示搜索服务器主界面
@login_required
def serverConfigSearch(request):
    result = []
    ip = ""
    port = ""
    idc = ""
    sign = ""

    if request.method == "POST":
        ip = request.POST.get("ip", "")
        port = request.POST.get("port", "")
        idc = request.POST.get("idc", "")
        sign = request.POST.get("sign", "")

    allServer = ServerList.objects.all()

    for server in allServer:
        if (ip == "" or server.ip == ip) and (
                        port == "" or server.port == port) and (
                        idc == "" or server.idc == idc) and (
                        sign == "" or server.sign == sign) and (
                    server.is_used == 1):
            result.append(server)

    resultSize=len(result)
    return render(request, 'serverConfig/serverConfigSearch.html',
                  {
                      "result": result,
                      "resultSize":resultSize
                  })
