from django import template


register = template.Library()


@register.inclusion_tag('dashboard/price_history.html')
def price_history_graph(title, container, data):
    graph_data = dict()
    for oid, odata in data.items():
        if oid not in graph_data:
            graph_data[oid] = {'org_name': odata['org_name'], 'history': list()}
        graph_data[oid]['history'].append({'date': odata['date'], 'price': odata['price']})
    print data
    return {'title': title, 'container': container, 'graph_data': graph_data}

