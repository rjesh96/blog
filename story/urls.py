from django.contrib import admin
from django.urls import path
from.import views

app_name='story'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.story_list, name='story_list'),
    path('search/',views.search_story, name='story_search'),
    path('<slug:category_slug>', views.story_list, name='story_by_category'),
    path('<int:id>/', views.story_detail, name='story_detail'),
    path('search/',views.search_story, name='story_search')

]
