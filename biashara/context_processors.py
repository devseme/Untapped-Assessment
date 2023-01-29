from .models import *

def menu_links(request):
    links = Borrower.objects.all()
    return dict(links=links)