from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail

from .models import Category, Announcement, Link
from .forms import ContactForm


def index(request):
    context = RequestContext(request)

    announcement_list = Announcement.objects.filter(show_this = True)
    context_dict = {'announcements': announcement_list,
    'header_text': "Welcome to PANT", 
    'subheader_text': "The Portland Area N-trak model railroad club"}

    return render_to_response('pant/index.html', context_dict, context)


def links(request):
    context = RequestContext(request)

    link_list = Link.objects.order_by('category')
    context_dict = {'links': link_list,
    'header_text': "PANT Links",
    'subheader_text': "Portland Area N-Trak model railroad club. Links to other sites."}

    return render_to_response('pant/links.html', context_dict, context)    


def directions(request):
    context = RequestContext(request)
    context_dict = {'header_text': "Portland Area N-trak",
    'subheader_text': "How to find us"}
    return render_to_response('pant/directions.html', context_dict, context)


def contact(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/pant/thanks/')
    else:
        form = ContactForm()

    context_dict = {'header_text': "Portland Area N-trak",
    'subheader_text': "How to contact us",
    'form': form}        
    return render(request, 'pant/contact.html', context_dict)



def stub(request):
    # Here is another way to construct a view using templates. This one does not
    # require that we get the context of the request. We just pass it to the render shortcut.

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key 'header_text' is the same as {{ header_text }} in the template!    
    context_dict = {'header_text': "Welcome to PANT"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the original request.
    # The second parameter is the template we wish to use.
    return render(request, 'pant/stub.html', context_dict)

def base(request):
    # This view is to make the dase template visible for development.
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key 'header_text' is the same as {{ header_text }} in the template!    
    context_dict = {'header_text': "Welcome to PANT", 'subheader_text': "The Portland Area N-trak model railroad club"}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    # Then we pass the new context and the original request context.
    return render_to_response('pant/base.html', context_dict, context)
   

def hello(request):
    # This view is an example of bypassing the templates and directly returning HTML.
    html = """
    <html>
    <head>
    <title> Hello </title>
    </head>
    <body>Hello world!.</body>
    </html>"""
    return HttpResponse(html)
  

def photos(request):
    context = RequestContext(request)
    context_dict = {'header_text': "Pant-o-graphs"}
    return render_to_response('pant/stub.html', context_dict, context)   

def tour(request):
    context = RequestContext(request)
    context_dict = {'header_text': "Layout tour"}
    return render_to_response('pant/stub.html', context_dict, context)
