from django.shortcuts import render
from ..models import SupportedResourceType
from django.shortcuts import render
from collections import OrderedDict
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def delete(request, resource_type, id):
    
    """Delete FHIR Interaction"""
    # Example client use in curl:
    # curl -X DELETE -H "Content-Type: application/json" --data @test.json http://127.0.0.1:8000/fhir/Practitioner/12345
    od = OrderedDict()
    od['request_method']= request.method
    od['interaction_type'] = "delete"
    od['resource_type']    = resource_type
    od['id'] = id
    od['note'] = "This is only a stub for future implementation"
    return HttpResponse(json.dumps(od, indent=4),
                        content_type="application/json")