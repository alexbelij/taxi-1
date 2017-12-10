from flask import Blueprint, render_template, request
from services.commons import json_response
# Register routes blueprint
driver = Blueprint ('driver', __name__)

@driver.route('/driverapp')
def home():
    from services import taxi_service
    from models.request import ReqStatus
    req_status = request.args.get('req_status', ReqStatus.WAITING)
    driver_id = request.args.get('id')
    xhr = request.args.get('xhr', False)
    if driver_id is None:
        return "Unknown driver"
    from models.request import ReqStatus
    requests = []
    if req_status == ReqStatus.WAITING.name:
        requests = taxi_service.get_requests_by_status(req_status)
    else:
        requests = taxi_service.get_requests_by_status(req_status, driver_id)

    template = 'driver/driver.html'
    if xhr:
        template = 'driver/{req_status}.html'.format(req_status=req_status.lower())

    print "Template.....", template
    return render_template(template, data=requests)