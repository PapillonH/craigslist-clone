from django.shortcuts import get_object_or_404, render

# Create your views here.


from django.shortcuts import render
from .models import Ad

def list_ads(request):
    ads = Ad.objects.all()
    return render(request, 'ads/list.html', {'ads': ads})

def view_ad(request, ad_id):
    ad = Ad.objects.get(id=ad_id)
    return render(request, 'ads/view.html', {'ad': ad})


# For the create_ad and edit_ad views, you'll need to handle form submission, 
# which is a bit more complex and requires understanding of Django forms.




# from .forms import AdForm


# def create_ad(request):
#     if request.method == 'POST':
#         form = AdForm(request.POST)
#         if form.is_valid():
#             new_ad = form.save()
#             return redirect('some_view_name')
#     else:
#         form = AdForm()
#     return render(request, 'ads/create_ad.html', {'form': form})

# def edit_ad(request, ad_id):
#     ad = get_object_or_404(Ad, id=ad_id)
#     if request.method == 'POST':
#         form = AdForm(request.POST, instance=ad)
#         if form.is_valid():
#             form.save()
#             return redirect('some_view_name')
#     else:
#         form = AdForm(instance=ad)
#     return render(request, 'ads/edit_ad.html', {'form': form, 'ad': ad})


