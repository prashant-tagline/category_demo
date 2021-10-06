from django.shortcuts import render
from .models import SubCategory, Category, Item
from django.http import HttpResponse
import json
from django.views.generic.base import TemplateView
from django.views.generic import ListView



def get_subcategory(request):
    '''return all sub-categories'''
    result = list(SubCategory.objects.exclude(parent_category_id__isnull=True).values('id', 'category'))
    return HttpResponse(json.dumps(result), content_type="application/json")


class Home(TemplateView):
    '''
        Return all Categories and Sub-Categories for navbar
    '''
    template_name = 'index.html'


class ItemListView(ListView):
    '''
        List all item related to sub-category
    '''
    template_name = 'items/items.html'
    model = Item    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)        
        items = Item.objects.filter(sub_category__slug=self.kwargs['slug'].lower())
        video_urls = []
        image_urls = []
        url = ''
        for item in items:
            if 'youtube' in item.item_url:
                if 'watch?v=' in item.item_url:
                    url = item.item_url.replace('watch?v=', 'embed/')
                    uid = url.split('/')[-1] 
                    video_urls.append({'video_url':url,'uid':uid})
            elif 'youtu' in item.item_url:
                url = 'https://www.youtube.com/embed/' + item.item_url.split('/')[-1]                
                video_urls.append({'video_url':url,'uid':item.item_url.split('/')[-1]})                
            else:
                image_urls.append(item.item_url)   
        
        context['video_urls'] = video_urls
        context['image_urls'] = image_urls
        return context


