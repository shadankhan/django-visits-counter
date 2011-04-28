from visits_counter.models import Visit
from datetime import datetime

def add_visit(request,obj):
    visit = Visit()
    visit.ip_address = request.META['REMOTE_ADDR']
    visit.user_agent = request.META['HTTP_USER_AGENT']
    visit.object_id = obj.id
    visit.object_model = obj.__class__.__name__
    visit.time = datetime.today()
    visit.save()
