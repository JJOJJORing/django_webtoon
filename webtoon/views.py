from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .naver_webtoon import *
from .daum_webtoon import *
from django.views.generic import ListView, DetailView
from .models import *
from django.utils import timezone


# Create your views here.
def naver_webtoon_crw(reqeust):
    naver_webtoon()
    return HttpResponse("네이버 웹툰 크롤링 완료")


def daum_webtoon_crw(request):
    daum_webtoon()
    return HttpResponse("다음 웹툰 크롤링 완료")


class WebtoonList(ListView):
    model = WebToon
    paginate_by = 30

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return WebToon.objects.filter(webtoon_name__contains=query)
        else:
            return WebToon.objects.filter(site_name='네이버')


class DaumWebtoonList(ListView):
    model = WebToon
    paginate_by = 30

    def get_queryset(self):
        return WebToon.objects.filter(site_name='다음')


class WebtoonDetailView(DetailView):
    template_name = "webtoon/webtoon_detail.html"
    def get_object(self, queryset=None):
        webtoon_id = self.kwargs['pk']
        webtoon = WebToon.objects.get(pk=webtoon_id)
        webtoon.webtoon_views += 1
        webtoon.save()

        commentList = Comment.objects.filter(webtoon_id=webtoon_id)
        # 딕셔너리로 웹툰과 댓글을 같이 묶어 넘긴다
        webtoon_object = {
            'webtoon': webtoon,
            'comment': commentList
        }

        return webtoon_object


def addComment(request, pk):
    comment = Comment()
    comment.webtoon_id = pk
    comment.comment_text = request.POST['comment_text']
    comment.create_date_time = timezone.now()

    comment.save()

    return HttpResponseRedirect('/detail/' + pk)
