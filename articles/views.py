from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request) :
    # DB에 전체 게시글 조회를 요청하고 쿼리셋을 응답받아 저장
    articles = Article.objects.all()
    # print(articles)
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)


# def new(request) :
#     form = ArticleForm()
#     context = {
#         'form' : form,
#     }
#     return render(request, 'articles/new.html', context)


# def create(request) :
#     # new에서 보낸 사용자 데이터를 받음
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')
#     # 받은 데이터를 DB에 저장
#     # 1
#     # article = Article()
#     # article.title = title
#     # article.content = content
#     # article.save()
#     form = ArticleForm(request.POST)
#     if form.is_valid():
#         article = form.save()
#         return redirect("articles:detail", article.pk)
#     context = {
#         'form' : form,
#     }
#     return render(request, 'articles/new.html', context)
    
#     # 2
    # article = Article(title=title, content=content)
    # 저장 전에 유효성 검사 진행
    # article.save()
    
    # 3
    # Article.objects.create(title=title, content=content)

    # 결과 페이지 반환
    # return render(request, 'articles/create.html')

    # 이동 URL 반환
    # return redirect("articles:index")

    # 생성한 글의 단일 조회 주소로 이동 응답


def create(request) :
    # HTTP requests method POST 라면
    if request.method == 'POST' :
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect("articles:detail", article.pk)
        context = {
            'form' : form,
        }
    
    # POST가 아니라면
    else :
        form = ArticleForm()

    context = {
        'form' : form,
    }
    return render(request, 'articles/new.html', context)


def delete(request, pk) :
    # 삭제할 데이터 조회
    article = Article.objects.get(pk = pk)
    
    # 조회한 데이터 삭제(DELETE)
    article.delete()

    # 전체 조회 페이지 이동
    return redirect("articles:index")


# def edit(request, pk) :
#     # 수정할 데이터 조회
#     article = Article.objects.get(pk = pk)
#     form = ArticleForm(instance=article)

#     context = {
#         'article' : article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context)


# def update(request, pk) :
#     # 데이터 조회
#     article = Article.objects.get(pk = pk)

#     # 데이터 수정
#     # 사용자가 입력한 form 데이터 저장
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')
    
#     # 조회한 데이터(article)의 필드값 변경
#     # article.title = title
#     # article.content = content

#     # 데이터 저장
#     # article.save()

#     form = ArticleForm(request.POST, instance=article)
#     if form.is_valid():
#         form.save()
#         return redirect('articles:detail', article.pk)
#     context = {
#         'form' : form,
#         'article' : article,
#     }
#     return render(request, 'articles/edit.html', context)


def update(request, pk) :
    article = Article.objects.get(pk = pk)
    if request.method == 'POST' :
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)

    else :
        form = ArticleForm(instance=article)

    context = {
        'article' : article,
        'form' : form,
    }
    return render(request, 'articles/edit.html', context)