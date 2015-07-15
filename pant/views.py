from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse


def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'header_text': "Welcome to PANT", 'subheader_text': "The Portland Area N-trak model railroad club"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('pant/index.html', context_dict, context)

def stub(request):
    context = RequestContext(request)
    context_dict = {'header_text': "Welcome to PANT"}
    return render_to_response('pant/stub.html', context_dict, context)

def base(request):
    context = RequestContext(request)
    context_dict = {'header_text': "Welcome to PANT", 'subheader_text': "The Portland Area N-trak model railroad club"}
    return render_to_response('pant/base.html', context_dict, context)

def links(request):
    context = RequestContext(request)
    context_dict = {'header_text': "PANT Links"}
    return render_to_response('pant/stub.html', context_dict, context)   

def hello(request):
    context = RequestContext(request)
    context_dict = {'header_text': "Hello World"}
    return render_to_response('pant/stub.html', context_dict, context)   

def contact(request):
    context = RequestContext(request)
    context_dict = {'header_text': "Contact us"}
    return render_to_response('pant/stub.html', context_dict, context)   

def photos(request):
    context = RequestContext(request)
    context_dict = {'header_text': "Pant-o-graphs"}
    return render_to_response('pant/stub.html', context_dict, context)   

def tour(request):
    context = RequestContext(request)
    context_dict = {'header_text': "Layout tour"}
    return render_to_response('pant/stub.html', context_dict, context)

def directions(request):
    context = RequestContext(request)
    context_dict = {'header_text': "How to find us"}
    return render_to_response('pant/stub.html', context_dict, context)
