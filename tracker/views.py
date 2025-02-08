from django.shortcuts import render, get_object_or_404, redirect
from .utils import get_link_data
from .models import Link
from .forms import AddLinkForm, EditLinkForm
from django.contrib import messages
# Create your views here.
'''
For our home view we need to pass the template:
- qs
- number of items
- number of items discounted
- form
- error (if exists)
'''

def home_view(request):
    form = AddLinkForm(request.POST or None)
    edit_form = EditLinkForm(request.POST or None)

    # Handle adding new link
    if request.method == 'POST' and 'add_link' in request.POST:
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Link added successfully!')
                return redirect('home-view')
            except Exception as e:
                messages.error(request, f'Error adding link: {str(e)}')
    

    # handle updating existing link
    if request.method == 'POST' and 'update_link' in request.POST:
        pk = request.POST.get('link_id')
        link = get_object_or_404(Link, pk=pk)

        try:
            name, price, img = get_link_data(request.POST.get('url'))

            link.url = request.POST.get('url')
            link.name = name 
            link.old_price = link.current_price or 0
            link.current_price = link.convert_to_int(price)
            link.price_difference = link.current_price - link.old_price
            link.img = img 

            link.sve()
            messages.success(request, 'Link updated successfully!')
            return redirect('home-view')
        
        except Exception as e:
            messages.error(request, f'Error updating link: {str(e)}')


    qs = Link.objects.all().order_by('-created')
    items_no = qs.count()

    discount_list = [item for item in qs if item.old_price > item.current_price]
    no_discounted = len(discount_list)

    context = {
        'qs': qs,
        'items_no': items_no,
        'no_discounted': no_discounted,
        'form': form,
        'edit_form': edit_form,
    }

    return render(request, 'tracker/main.html', context)
        
    
def delete_link(request, pk):
    link = get_object_or_404(Link, pk=pk)
    link.delete()
    messages.success(request, 'Link deleted successfully')
    return redirect('home-view')


