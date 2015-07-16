from django.shortcuts import render , render_to_response
from django.http import HttpResponse , HttpResponseRedirect
from Curator.models import Document
from Curator.forms  import DocumentForm
from django.core.urlresolvers import reverse
from django.template import RequestContext

def base(request):
    return render(request, 'Seshat/form.html', {})


def document2(request):
    if request.POST:
        # extract request variables
       # title = request.POST['new_title']
        #image = request.POST['picture']

        # create the document object
        d = Document(title=title, image="images/someimage.jpg")


    # create html string and return
    html = "<html><body>It worked!</body></html>"
    return HttpResponse(html)









def document(request):
    print request
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(image = request.FILES['image'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('Curator.views.document'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'Seshat/form.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )


#title= request.POST['title']