# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from tidbits.forms import HomepageTidbitForm, TidbitUrlForm
from tidbits.models import Tidbit

def homepage(request):
    tidbit_form = HomepageTidbitForm()
    recent_tidbits = Tidbit.objects.recent_tidbits()
    url_form = TidbitUrlForm()
    return render_to_response("homepage.html", { 'tidbit_form': tidbit_form,
                                                 'url_form': url_form,
                                                 'recent_tidbits': recent_tidbits,
                                                 }, context_instance=RequestContext(request))

def create_tidbit(request):
    if request.method == "POST":
        tidbit_form = HomepageTidbitForm(request.POST)
        if tidbit_form.is_valid():
            tidbit_form.save()
        else:
            # todo return to a different page that will display the errors
            pass
        
        return HttpResponseRedirect(reverse("show_my_tidbits"))



def my_tidbits(request):
    return render_to_response('my_tidbits.html', {'tidbits': Tidbit.objects.all()}, context_instance=RequestContext(request))