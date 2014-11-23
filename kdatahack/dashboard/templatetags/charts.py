from django import template
from datetime import datetime, timedelta
from random import randrange

register = template.Library()


@register.inclusion_tag('dashboard/price_history.html')
def price_history_graph(title, container, data):
    graph_data = dict()
    if data:
        for oid, odata in data.items():
            for point in odata:
                if oid not in graph_data:
                    graph_data[oid] = {'org_name': point['org_name'], 'history': list()}
                past = timedelta(days=randrange(365))
                graph_data[oid]['history'].append({
                    'date': point['date'] or datetime.today()-past,
                    'price': point['price']})
    return {'title': title, 'container': container, 'graph_data': graph_data}

