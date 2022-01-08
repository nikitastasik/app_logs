from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from .models import NameForm, Logs
from django.views import View
from django.core.files import File
import json
import logging

# def return_json(raw_data):
#     return JsonResponse(raw_data)

@csrf_exempt
def log_list(request):
    # get and write values in vars
    # and request.META['REMOTE_ADDR'] == '5.17.3.88'
    if request.method == 'POST':
        domain_name = request.POST.get('domain')
        log_text = request.POST.get('logs')
        date = request.POST.get('date')
        type_logs = request.POST.get('type')
        # write values in db
        response_from_db = Logs.objects.create(domain=domain_name, text_log=log_text, date_add=date,
                                               type_logs=type_logs)

        # display status
        dict_values = Logs.objects.filter(domain=domain_name).values()
        last_add_data = dict_values[0]['text_log']
        status = {
            'status': bool(response_from_db),
        }
        # status = return_json(pre_status)

        return render(request, 'logs/logs_list.html', {'status': json.dumps(status), 'add_data': last_add_data})
    else:
        status = {
            'status': False,
        }
        return render(request, 'logs/logs_list.html', {'status': json.dumps(status)})




@csrf_exempt

# and request.META['REMOTE_ADDR'] == '5.17.3.88'
def result(request):
    if request.method == 'POST':
        domain_name = request.POST.get('domain')
        type_logs = request.POST.get('type')
        if type_logs == 'o':
            dict_values = Logs.objects.order_by('-date_add').filter(domain=domain_name, type_logs='o').values()
            last_add_data = {}
            for i in range(3):
                date_for_dict = dict_values[i]['date_add']
                last_add_data[date_for_dict] = dict_values[i]['text_log']
            status = 'ok'
            return render(request, 'logs/result.html', {'domain': domain_name, 'getted_data': last_add_data, 'status': status})
        else:
            status = {
                'status': 'logs with other type is hidden',
            }
            return render(request, 'logs/result.html', {'domain': domain_name, 'status': status})
    else:
        status = {
            'status': 'use POST request',
        }
        return render(request, 'logs/result.html', {'status': status})