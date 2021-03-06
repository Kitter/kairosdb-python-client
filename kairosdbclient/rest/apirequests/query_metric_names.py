from kairosdbclient.rest.apirequests.base import Request
from kairosdbclient.rest.resources import MetricNames


class QueryMetricNamesRequest(Request):
    uri = 'metricnames'
    resource = MetricNames
    success_status_code = 200
    request_method = 'GET'

    def payload(self):
        return None