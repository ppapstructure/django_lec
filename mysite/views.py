from django.shortcuts import render
from .models import MainContent
# Create your views here.
def index(request):
    # -pub_date는 오름차순임 가장 최신 상품부터 정렬
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list':content_list}
    return render(request, 'mysite/content_list.html', context)