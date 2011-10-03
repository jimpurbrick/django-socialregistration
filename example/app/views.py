from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from socialregistration.contrib.linkedin.models import LinkedInProfile
from socialregistration.contrib.openid.models import OpenIDProfile
from socialregistration.contrib.twitter.models import TwitterProfile

def index(request):
    return render_to_response(
        'index.html', dict(
#            facebook=FacebookProfile.objects.all(),
            twitter=TwitterProfile.objects.all(),
            openid=OpenIDProfile.objects.all(),
            linkedin=LinkedInProfile.objects.all(),
    ), context_instance=RequestContext(request))