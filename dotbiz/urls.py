from django.urls import path
from .views import *
from django.shortcuts import redirect


def sub_redirect(req):
    return redirect('sub-list-admin')


def file_redirect(req):
    return redirect('file-list')


def user_redirect_post(req):
    return redirect('/')


def link_redirect(req):
    return redirect('admin-link-list')


def dropdown_redirect(req):
    return redirect('list-dd-content')


def temp404(req):
    return render(req, '404.html')


def temp403(req):
    return render(req, '403.html')


def temp400(req):
    return render(req, '400.html')


def temp500(req):
    return render(req, '500.html')


urlpatterns = [
    # yang ini untuk control para guest
    path('', index.as_view(), name='index'),

    # yang ini untuk control admin yang akan di bagi-bagi

    # 1. login, logout dan register. tapi register di umpetin aja
    path('wpcp-admin/register', register_view, name='register'),
    path('wpcp-admin/login/', login_view, name='login'),
    path('wpcp-admin/logout/', AdminLogout, name='logout'),

    # 2. Cma nampil Dashboard doang
    # path('wpcp-admin/', AdminShowDashboardPage, name='admin-home'),
    path('wpcp-admin/', AdminDashboardView.as_view(), name='admin-home'),

    # 3. Post page
    path('wpcp-admin/page/', redirect_page_zero, name='redirected'),
    path('wpcp-admin/page/<slug:page_link>/', redirect_page, name='redirected'),
    path('wpcp-admin/page-list/', AdminShowAllPostList.as_view(), name='main-list-admin'),
    path('wpcp-admin/create-main-page/', AdminCreatePost.as_view(), name='create-admin'),
    path('wpcp-admin/page/<slug:page_link>/edit/', AdminUpdatePost.as_view(), name='edit-admin'),
    path('wpcp-admin/page/<slug:page_link>/delete/', AdminDeletePost.as_view(), name='delete-admin'),
    path('wpcp-admin/page/<slug:page_link>/preview/', AdminPreviewPost.as_view(), name='view-admin'),
    path('wpcp-admin/page/disable/<int:pk>/stats/', AdminPostStatsUpdatetoDisable, name='disable-admin'),
    path('wpcp-admin/page/enable/<int:pk>/stats/', AdminPostStatsUpdatetoActive, name='active-admin'),

    # 4. Category page
    path('wpcp-admin/category/', redirect_category_zero, name='redirected'),
    path('wpcp-admin/category/<slug:category_link>/', redirect_category, name='redirected'),
    path('wpcp-admin/add-category/', AdminAddCategory.as_view(), name='add-cat-admin'),
    path('wpcp-admin/category-list/', AdminShowAllCategoryList.as_view(), name='cat-list-admin'),
    path('wpcp-admin/category/<slug:category_link>/edit/', AdminUpdateCategory.as_view(), name='cat-edit-admin'),
    path('wpcp-admin/category/<slug:category_link>/delete/', AdminDeleteCategory.as_view(), name='cat-delete-admin'),
    path('wpcp-admin/category/<slug:category_link>/preview/', AdminPreviewCategory.as_view(), name='cat-preview-admin'),
    path('wpcp-admin/category/enable/<int:pk>/stats/', AdminUpdateCategoryStatsToActive, name='cat-enable'),
    path('wpcp-admin/category/disable/<int:pk>/stats/', AdminUpdateCategoryStatsToDisable, name='cat-disable'),

    # 5. sub page
    # path('wpcp-admin/subpage/<slug:page_link>/create', AdminCreateSubPage.as_view(), name="sub-create-admin"),
    path('wpcp-admin/subpage', sub_redirect, name='redirected'),
    path('wpcp-admin/subpage/<slug:page_link>', sub_redirect, name='redirected'),
    path('wpcp-admin/subpage-list/', AdminShowAllSubPageList.as_view(), name='sub-list-admin'),
    # path('wpcp-admin/subpage/<slug:page_link>/create/', AdminCreateSubPage, name="sub-create-admin"),
    path('wpcp-admin/page/<slug:page_link>/create/', AdminCreateSubPage.as_view(), name="sub-create-admin"),
    path('wpcp-admin/subpage/<slug:page_link>/edit/', AdminUpdateSubPage.as_view(), name="sub-edit-admin"),
    path('wpcp-admin/subpage/<slug:page_link>/delete/', AdminDeleteSupPage.as_view(), name="sub-delete-admin"),
    path('wpcp-admin/subpage/<slug:page_link>/preview/', AdminPreviewSubPage.as_view(), name="sub-preview-admin"),
    path('wpcp-admin/subpage/<int:pk>/disable/', AdminDisableSubPage, name='disable-sub-admin'),
    path('wpcp-admin/subpage/<int:pk>/active/', AdminActivateSubPage, name='activate-sub-admin'),

    # file control
    path('wpcp-admin/file', file_redirect, name='redirected'),
    path('wpcp-admin/file/<int:pk>', file_redirect, name='redirected'),
    path('wpcp-admin/file/upload/', AdminFileUpload.as_view(), name='file-upload'),
    path('wpcp-admin/file-list/', AdminFileList.as_view(), name='file-list'),
    path('wpcp-admin/file-list/delete-allow/', AdminFileListCanDelete.as_view(), name='file-list-del'),
    path('wpcp-admin/file/<int:pk>/delete/', DeleteFile, name='delete-file'),

    # Index Home Template
    path('wpcp-admin-indexer/', AdminEditDashboard.as_view(), name='edit-index-dashboard'),
    path('wpcp-admin-indexer/home/', AdminEditIndex, name='admin-edit-index'),
    path('wpcp-admin-indexer/link-list/', AdminLinkList.as_view(), name='admin-link-list'),
    path('wpcp-admin-indexer/add-link/', AdminAddSideLinks.as_view(), name='admin-add-link'),
    path('wpcp-admin-indexer/link/<int:pk>/edit/', AdminEditLinks.as_view(), name='admin-edit-link'),
    path('wpcp-admin-indexer/link/<int:pk>/delete/', AdminDeleteLinks.as_view(), name='admin-delete-link'),
    path('wpcp-admin-indexer/dropdown-url/', AdminListDropdownURL.as_view(), name='dd-url-list'),
    path('wpcp-admin-indexer/dropdown-url/add/', AdminAddDropdownURL.as_view(), name='add-dd-content'),
    path('wpcp-admin-indexer/dropdown-url/<int:pk>/edit/', AdminEditDropdownURL.as_view(), name='edit-dd-url'),
    path('wpcp-admin-indexer/dropdown-url/<int:pk>/delete/', AdminDeleteDropdownURL.as_view(), name='del-dd-url'),
    path('wpcp-admin-indexer/dropdown-tag/', AdminListDropdownTag.as_view(), name='dd-tag-list'),
    path('wpcp-admin-indexer/dropdown-tag/add/', AdminAddDropdownTag.as_view(), name='add-dd-tag'),
    path('wpcp-admin-indexer/dropdown-tag/<int:pk>/edit/', AdminEditDropdownTag.as_view(), name='edit-dd-tag'),
    path('wpcp-admin-indexer/dropdown-tag/<int:pk>/delete/', AdminDeleteDropdownTag.as_view(), name='del-dd-tag'),

    # index home redirect
    path('wpcp-admin-indexer/link/', link_redirect, name='link-redirect'),
    path('wpcp-admin-indexer/link/<int:pk>/', link_redirect, name='link-redirect'),
    path('wpcp-admin-indexer/dropdown-content/', dropdown_redirect, name='dd-redirect'),
    path('wpcp-admin-indexer/dropdown-content/<int:pk>/', dropdown_redirect, name='dd-redirect'),

    # just error
    path('404/', temp404, name='404'),
    path('400/', temp400, name='400'),
    path('403/', temp403, name='403'),
    path('500/', temp500, name='500'),

    # user views
    path('sub/', user_redirect_post),
    path('category/', user_redirect_post),
    path('search/', user_redirect_post),
    path('search/Q', SearchResultView.as_view(), name='res'),
    path('<page_link>/', UserViewPost.as_view(), name='view-post'),
    path('sub/<page_link>/', UserViewSubPageData.as_view(), name='view-subpage'),
    path('category/<slug:category_link>/', UserCategoryView.as_view(), name='view-category'),
    path('post/older/', OlderPost.as_view(), name='older-post'),


    # Testing disini
    path('wpcp-admin/testing/', testing.as_view(), name='testing'),

]
def temp500(req):
    return render(req, '500.html')




