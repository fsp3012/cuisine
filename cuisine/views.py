from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from .models import Cuisine, Comment
from .forms import  CommentForm
from django.core.mail import send_mail

# Create your views here.

# Cuisine_list view as a class-based view
class CuisineListView(ListView):
    queryset = Cuisine.objects.all()
    context_object_name = 'cuisines'
    paginate_by = 3 # 3 posts in each page
    template_name = 'cuisine/cuisine/list.html'

#Cuisine_detail view as a class-based view
class CuisineDetailView(DetailView):
    model = Cuisine
    context_object_name = 'cuisine'
    template_name = 'cuisine/cuisine/detail.html'

# =========================================================================================

# Cuisine_list view as a function-based view
def Cuisine_list(request):
    """function to implement the logic of the list view for Cuisine"""
    object_list = Cuisine.objects.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        cuisines = paginator.page(page)
    except PageNotAnInteger:
        cuisines = paginator.page(1)
    except EmptyPage:
        cuisines = paginator.page(paginator.num_pages)
    return render(
        request,
        'cuisine/cuisine/list.html',
        {'page': page, 'cuisines': cuisines}
    )
        
    

# Cuisine_detail view as a function-based view
def Cuisine_detail(request, cuisine):
    """function to implement the logic of the detail view for Cuisine"""
    cuisineClicked = get_object_or_404(
        Cuisine,
        slug=cuisine,
        status='published'
    )
    # List of active comments for this post
    comments = cuisineClicked.comments.filter(active=True)
    commented = False
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.cuisine = cuisineClicked
            # Save the comment to the database
            new_comment.save()
            commented = True
    else:
        comment_form = CommentForm()
    return render(
        request,
        "cuisine/cuisine/detail.html",
    
            {
            'cuisine': cuisineClicked,
            'comments': comments,
            'commented': commented,
            'comment_form': comment_form,
            }

    )