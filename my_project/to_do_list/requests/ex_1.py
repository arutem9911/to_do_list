from datetime import datetime

# ex_1
current_date = datetime.today()
Tasks.objects.filter(updated_at__date__range=(datetime(current_date.year, current_date.month - 1, current_date.day).date(), current_date))

# ex_2
Tasks.objects.filter(status__status__in=['in progress', 'done'], type__type__in=('Bug', 'Enhancement'))

# ex_3
qs1 = Q(short_description__icontains='bug')
qs2 = Q(type__type='Bug')
Tasks.objects.filter(qs1 | qs2)



######## Bonus ########
# ex_1
Tasks.objects.values_list('id', 'short_description', 'status__status', 'type__type')

# ex_3
status_list = ['new', 'in progress', 'done', 'unknown']
for item_status in status_list:
    print(item_status, ': ', Tasks.objects.filter(status__status=item_status).count())
