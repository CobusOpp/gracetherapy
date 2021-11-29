
from .models import Post, Category

def cat_list(request):
    cat_menu = Category.objects.all()
    
    return {
        'cat_menu' : cat_menu,
    }
    
    