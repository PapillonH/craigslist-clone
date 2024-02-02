# from django import forms
# from .models import Ad

# class AdForm(ModelForm):
#     class Meta:
#         model = Ad
#         fields = '__all__'  
        
        # This will include all fields of the model
        # Alternatively, you can specify only the fields you want:
        # fields = ['title', 'description', 'price', 'posted_by']



# class AdForm(ModelForm):
#     class Meta:
#         model = Ad
#         fields = '__all__'
#         widgets = {
#             'description': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
#         }



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