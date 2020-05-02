from django.urls import path
from . import views
urlpatterns = [
   path('products', views.ProductViews.as_view()),
   path('products/<int:pk>',views.DeleteProductView.as_view()),
   path('categories', views.CategoryViews.as_view()),
   path('categories/<int:pk>', views.DeleteCategoryView.as_view()),
   path('comments', views.CommentViews.as_view()), 
   path('comments/<int:pk>', views.DeleteCommentView.as_view())
]

