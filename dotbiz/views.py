from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from django.views.decorators.cache import cache_control
from django.urls import reverse_lazy
from django.db.models import Q as __
import os
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext


def handler404(request, *args, **argv):
    response = render(request, '404.html')
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, '500.html')
    response.status_code = 500
    return response


def handler400(request, *args, **kwargs):
    response = render(request, '400.html')
    response.status_code = 400
    return response


def handler403(request, *args, **kwargs):
    response = render(request, '403.html')


page_link = 'page_link'
category_link = 'category_link'


@cache_control(no_cache=True, must_revalidate=True, private=True, max_age=0)
def redirect_page(req, page_link):
    return redirect('main-list-admin')


def redirect_page_zero(req):
    return redirect('main-list-admin')


def redirect_category(req, category_link):
    return redirect('cat-list-admin')


def redirect_category_zero(req):
    return redirect('cat-list-admin')


def post(req):
    item = Post.objects.all()
    con = {
        'post': item
    }
    return render(req, 'blog.html', con)


""" Upload File Views Here """


class AdminFileUpload(CreateView):
    model = UploadedFile
    form_class = FileUploadForm
    template_name = 'admini/file_up.html'
    success_url = reverse_lazy('file-list')


class AdminFileList(ListView):
    model = UploadedFile
    paginate_by = 100
    ordering = ['-id']
    template_name = 'admini/img.html'


class AdminFileListCanDelete(ListView):
    model = UploadedFile
    paginate_by = 100
    ordering = ['-id']
    template_name = 'admini/img_delete.html'


def DeleteFile(req, pk):
    if req.method == 'POST':
        file = UploadedFile.objects.get(pk=pk)
        file.delete()
    return redirect('file-list')


def download(req, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/file')
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response
    raise Http404


""" End Here"""


# register, login, logout
def register_view(req):
    form = CreateUserForm()

    if req.method == "POST":
        form = CreateUserForm(req.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(req, 'account has been created for ' + user)
            return redirect('login')

    con = {'form': form}
    return render(req, 'register.html', con)


def login_view(req):
    template = 'admini/login.html'
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(req, username=username, password=password)

        if user is not None:
            if not user.is_staff:
                messages.warning(req, 'Access Denied You Just a Common User')
                return render(req, template)
            else:
                if not user.is_superuser:
                    messages.warning(req, 'Access Denied You Just a Staff ')
                    return render(req, template)
                else:
                    login(req, user)
                    return redirect('admin-home')
        else:
            messages.info(req, 'username or password is incorrect')
            return render(req, template)

    con = {}
    return render(req, template, con)


def AdminLogout(req):
    logout(req)
    return redirect('login')


# end of control


# wpcp-admin/
def AdminShowDashboardPage(req):
    return render(req, 'admini/index.html')


class AdminDashboardView(TemplateView):
    template_name = 'admini/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AdminDashboardView, self).get_context_data(*args, **kwargs)
        c_post = Post.objects.all().count()
        c_post_active = Post.objects.filter(stats='ACTIVE').count()
        c_sub = SubPage.objects.all().count()
        c_sub_active = SubPage.objects.filter(stats='ACTIVE').count()
        c_cat = Category.objects.all().count()
        c_file = UploadedFile.objects.all().count()

        context['post'] = c_post
        context['active'] = c_post_active
        context['sub_page'] = c_sub
        context['sub_active'] = c_sub_active
        context['category'] = c_cat
        context['file'] = c_file
        return context


# end main page


"""
    wpcp-admin/page
    model = Post
"""


class AdminCreatePost(CreateView):
    model = Post
    form_class = AdminCreatePostForms
    template_name = 'admini/add_page.html'
    success_url = reverse_lazy('main-list-admin')


class AdminUpdatePost(UpdateView):
    model = Post
    query_pk_and_slug = True
    slug_field = page_link
    slug_url_kwarg = page_link
    form_class = UpdatePostForms
    template_name = 'admini/edit.html'
    success_url = reverse_lazy('main-list-admin')


class AdminShowAllPostList(ListView):
    model = Post
    template_name = 'admini/table.html'
    ordering = ['title']
    paginate_by = 15

    def get_queryset(self):
        qq = self.request.GET.get('q')
        if qq is not None:
            object_list = Post.objects.filter(
                __(title__icontains=qq) | __(title_tag__icontains=qq) | __(page_link__icontains=qq) |
                __(body__icontains=qq) | __(meta_keyword__icontains=qq) | __(meta_description__icontains=qq)
            )
        else:
            object_list = Post.objects.all()

        return object_list


class AdminPreviewPost(DetailView):
    model = Post
    query_pk_and_slug = True
    slug_field = page_link
    slug_url_kwarg = page_link
    template_name = 'admin_prev/post.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AdminPreviewPost, self).get_context_data(*args, **kwargs)
        code = Post.objects.get(page_link=self.kwargs['page_link'])
        get_cat = code.category
        related = Post.objects.filter(category=get_cat, stats='ACTIVE')
        subPage = SubPage.objects.filter(parent_page=code, stats='ACTIVE')

        main = IndexEditor.objects.get(pk=1)
        links = SideLinkForIndex.objects.all()
        latest = Post.objects.all().order_by('-update_date')[:4]
        dd_tag = DropdownTag.objects.all()

        context['dd_tag'] = dd_tag
        context['cat'] = get_cat
        context['sub_page'] = subPage
        context['related'] = related
        context['latest'] = latest
        context['main'] = main
        context['links'] = links
        return context


class AdminDeletePost(DeleteView):
    model = Post
    query_pk_and_slug = True
    slug_url_kwarg = page_link
    slug_field = page_link
    template_name = 'admini/delete.html'
    success_url = reverse_lazy('main-list-admin')


def AdminPostStatsUpdatetoDisable(req, pk):
    item_to_update = Post.objects.filter(pk=pk)
    if item_to_update.exists():
        if req.user:
            item_to_update.update(stats="DISABLED")
    return redirect('main-list-admin')


def AdminPostStatsUpdatetoActive(req, pk):
    item_to_update = Post.objects.filter(pk=pk)
    if item_to_update.exists():
        if req.user:
            item_to_update.update(stats="ACTIVE")
    return redirect('main-list-admin')


"""
    end of model = Post
"""
#
#
#
#


"""
    wpcp-admin/category
    model = Category
"""


class AdminAddCategory(CreateView):
    model = Category
    form_class = AdminAddMoreCategory
    template_name = 'admini/add_category.html'
    success_url = reverse_lazy('cat-list-admin')


class AdminUpdateCategory(UpdateView):
    model = Category
    query_pk_and_slug = True
    slug_field = category_link
    slug_url_kwarg = category_link
    form_class = AdminUpdateCategory
    template_name = 'admini/edit_cat.html'
    success_url = reverse_lazy('cat-list-admin')


class AdminShowAllCategoryList(ListView):
    model = Category
    template_name = 'admini/cat_list.html'
    paginate_by = 10
    ordering = ['id']

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            object_list = Category.objects.filter(
                __(name__icontains=query) | __(category_tag__icontains=query) |
                __(category_content__icontains=query) | __(meta_keyword__icontains=query) |
                __(meta_description__icontains=query) | __(category_link__icontains=query)
            )
        else:
            object_list = Category.objects.all()

        return object_list


class AdminDeleteCategory(DeleteView):
    model = Category
    query_pk_and_slug = True
    slug_field = category_link
    slug_url_kwarg = category_link
    template_name = 'admini/delete_cat.html'
    success_url = reverse_lazy('cat-list-admin')


class AdminPreviewCategory(DetailView):
    model = Category
    query_pk_and_slug = True
    slug_field = category_link
    slug_url_kwarg = category_link
    template_name = 'admin_prev/cate.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AdminPreviewCategory, self).get_context_data(*args, **kwargs)
        related = Post.objects.filter(category=Category.objects.get(category_link=self.kwargs[category_link]),
                                      stats='ACTIVE')

        main = IndexEditor.objects.get(pk=1)
        links = SideLinkForIndex.objects.all()
        latest = Post.objects.all().order_by('-update_date')[:4]
        dd_tag = DropdownTag.objects.all()

        context['dd_tag'] = dd_tag
        context['related'] = related
        context['latest'] = latest
        context['main'] = main
        context['links'] = links
        return context


def AdminUpdateCategoryStatsToDisable(req, pk):
    item_to_update = Category.objects.filter(pk=pk)
    if item_to_update.exists():
        if req.user:
            item_to_update.update(stats="DISABLED")
    return redirect('cat-list-admin')


def AdminUpdateCategoryStatsToActive(req, pk):
    item_to_update = Category.objects.filter(pk=pk)
    if item_to_update.exists():
        if req.user:
            item_to_update.update(stats="ACTIVE")
    return redirect('cat-list-admin')


"""
    end of model = Category
"""

"""
    wpcp-admin/SubPage
    model = SubPage
"""


class AdminCreateSubPage(CreateView):
    query_pk_and_slug = True
    slug_field = 'page_link'
    slug_url_kwarg = 'page_link'
    model = SubPage
    form_class = AdminCreateSubPageForm
    template_name = 'admini/add_sub_page.html'

    def get_success_url(self):
        return reverse('sub-list-admin')

    def form_valid(self, form):
        form.instance.parent_page_id = Post.objects.get(page_link=self.kwargs[page_link]).pk
        b = HttpResponseRedirect(self.get_success_url())
        return super(AdminCreateSubPage, self).form_valid(form) and b


# def AdminCreateSubPage(request, page_link):
#     r = Post.objects.filter(parent_check="PARENT")
#     q = Post.objects.filter(page_link=page_link).values_list('id')
#     # if q.is_exists():
#     #     q = q.first()
#     # r = r.first()
#
#     # unique_note = get_object_or_404(Post)
#     form = AdminCreateSubPageForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.instance.user = request.user
#         form.save()
#         return redirect('sub-list-admin')
#
#     context = {
#         'form': form,
#         'par_page': q,
#         'pare': r
#     }
#
#     return render(request, 'admini/add_sub_page.html', context)


class AdminShowAllSubPageList(ListView):
    model = SubPage
    template_name = 'admini/table_sub.html'
    ordering = ['-parent_page']
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            object_list = SubPage.objects.filter(
                __(title__icontains=query) | __(title_tag__icontains=query) | __(page_link__icontains=query) |
                __(body__icontains=query) | __(meta_keyword__icontains=query) | __(meta_description__icontains=query)
            )
        else:
            object_list = SubPage.objects.all()

        return object_list


class AdminUpdateSubPage(UpdateView):
    model = SubPage
    query_pk_and_slug = True
    slug_field = page_link
    slug_url_kwarg = page_link
    form_class = AdminCreateSubPageForm
    template_name = 'admini/edit_sub.html'
    success_url = reverse_lazy('sub-list-admin')


class AdminDeleteSupPage(DeleteView):
    model = SubPage
    slug_field = page_link
    query_pk_and_slug = True
    slug_url_kwarg = page_link
    template_name = 'admini/delete_sub.html'
    success_url = reverse_lazy('sub-list-admin')


class AdminPreviewSubPage(DetailView):
    model = SubPage
    slug_field = page_link
    slug_url_kwarg = page_link
    query_pk_and_slug = True
    template_name = 'admin_prev/subpage.html'
    context_object_name = 'post'

    def get_context_data(self, *args, **kwargs):
        context = super(AdminPreviewSubPage, self).get_context_data(*args, **kwargs)
        sub = SubPage.objects.get(page_link=self.kwargs['page_link'])
        main_title = Post.objects.get(title=sub.parent_page)
        related = SubPage.objects.filter(parent_page=main_title, stats='ACTIVE')
        related2 = Post.objects.filter(category=main_title.category)
        main = IndexEditor.objects.get(pk=1)
        links = SideLinkForIndex.objects.all()
        latest = Post.objects.all().order_by('-update_date')[:4]
        dd_tag = DropdownTag.objects.all()

        context['dd_tag'] = dd_tag
        context['related'] = related
        context['related2'] = related2
        context['main_title'] = main_title
        context['latest'] = latest
        context['main'] = main
        context['links'] = links
        return context


def AdminDisableSubPage(req, pk):
    item_to_update = SubPage.objects.filter(pk=pk)
    if item_to_update.exists():
        if req.user:
            item_to_update.update(stats='DISABLED')
    return redirect('sub-list-admin')


def AdminActivateSubPage(req, pk):
    item_to_update = SubPage.objects.filter(pk=pk)
    if item_to_update.exists():
        if req.user:
            item_to_update.update(stats='ACTIVE')
    return redirect('sub-list-admin')


"""
    end of model = SubPage
"""

#
#
"""
    Edit Index here
"""


class AdminEditDashboard(TemplateView):
    template_name = 'index_edit/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AdminEditDashboard, self).get_context_data(*args, **kwargs)
        total_link = SideLinkForIndex.objects.all().count()
        dd_content = DropdownURL.objects.all().count()
        dd_tag = DropdownTag.objects.all().count()
        files = UploadedFile.objects.all().count()
        Post_ = Post.objects.filter(stats='ACTIVE').count()
        Post_ = int(Post_)
        subpage = SubPage.objects.filter(stats='ACTIVE').count()
        subpage = int(subpage)
        cate = Category.objects.filter(stats='ACTIVE').count()
        cate = int(cate)
        act_page = Post_ + subpage + cate

        context['dd_tag'] = dd_tag
        context['act_page'] = act_page
        context['files'] = files
        context['links'] = total_link
        context['dd_content'] = dd_content
        return context


def AdminEditIndex(req):
    indexer = get_object_or_404(IndexEditor, pk=1)
    form = IndexEditorForm(req.POST or None, req.FILES or None, instance=indexer)
    template = 'index_edit/edit_home.html'

    if form.is_valid():
        form.save()
        return redirect('edit-index-dashboard')

    context = {
        'form': form,
    }

    return render(req, template, context)


class AdminLinkList(ListView):
    model = SideLinkForIndex
    ordering = ['name']
    paginate_by = 10
    template_name = 'index_edit/table.html'

    def get_queryset(self):
        qq = self.request.GET.get('q')
        if qq is not None:
            object_list = SideLinkForIndex.objects.filter(
                __(name__icontains=qq) | __(url__icontains=qq)
            )
        else:
            object_list = SideLinkForIndex.objects.all()

        return object_list


class AdminAddSideLinks(CreateView):
    model = SideLinkForIndex
    form_class = CreateLinksIndexForm
    template_name = 'index_edit/add_link.html'
    success_url = reverse_lazy('admin-link-list')


class AdminEditLinks(UpdateView):
    model = SideLinkForIndex
    form_class = EditLinkIndexForm
    template_name = 'index_edit/add_link.html'
    success_url = reverse_lazy('admin-link-list')


class AdminDeleteLinks(DeleteView):
    model = SideLinkForIndex
    template_name = 'index_edit/delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('admin-link-list')


class AdminAddDropdownURL(CreateView):
    model = DropdownURL
    form_class = AddDropdownURL
    template_name = 'index_edit/add_dd_url.html'
    success_url = reverse_lazy('dd-url-list')


class AdminListDropdownURL(ListView):
    model = DropdownURL
    ordering = ['id']
    paginate_by = 15
    template_name = 'index_edit/table_dd.html'

    def get_queryset(self):
        qq = self.request.GET.get('q')
        if qq is not None:
            object_list = DropdownURL.objects.filter(
                __(name__icontains=qq) | __(url__icontains=qq)
            )
        else:
            object_list = DropdownURL.objects.all()

        return object_list


class AdminEditDropdownURL(UpdateView):
    model = DropdownURL
    form_class = EditDropdownURL
    template_name = 'index_edit/edit.html'
    success_url = reverse_lazy('dd-url-list')


class AdminDeleteDropdownURL(DeleteView):
    model = DropdownURL
    context_object_name = 'post'
    template_name = 'index_edit/delete.html'
    success_url = reverse_lazy('dd-url-list')


class AdminListDropdownTag(ListView):
    model = DropdownTag
    ordering = ['id']
    paginate_by = 15
    template_name = 'index_edit/table_tag.html'

    def get_queryset(self):
        qq = self.request.GET.get('q')

        if qq is not None:
            uri = DropdownURL.objects.filter(url__icontains=qq)
            object_list = DropdownTag.objects.filter(
                __(name__icontains=qq) | __(links__in=uri)
            )
        else:
            object_list = DropdownTag.objects.all()

        return object_list


class AdminAddDropdownTag(CreateView):
    model = DropdownTag
    form_class = AddDropdownTag
    success_url = reverse_lazy('dd-tag-list')
    template_name = 'index_edit/add_dd_tag.html'


class AdminEditDropdownTag(UpdateView):
    model = DropdownTag
    form_class = EditDropdownTag
    success_url = reverse_lazy('dd-tag-list')
    template_name = 'index_edit/edit_dd_tag.html'


class AdminDeleteDropdownTag(DeleteView):
    model = DropdownTag
    success_url = reverse_lazy('dd-tag-list')
    template_name = 'index_edit/delete.html'
    context_object_name = 'post'


"""
    End Of Edit Index
"""

#
#

"""
    user Post view
"""


class UserViewPost(DetailView):
    query_pk_and_slug = True
    model = Post
    slug_field = page_link
    slug_url_kwarg = page_link
    template_name = 'user/post.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UserViewPost, self).get_context_data(*args, **kwargs)
        code = Post.objects.get(page_link=self.kwargs['page_link'])
        get_cat = code.category
        cat = Category.objects.get(name=get_cat)
        related = Post.objects.filter(category=get_cat, stats='ACTIVE')
        subPage = SubPage.objects.filter(parent_page=code, stats='ACTIVE')
        main = IndexEditor.objects.get(pk=1)
        links = SideLinkForIndex.objects.all()
        latest = Post.objects.all().order_by('-update_date')[:4]
        dd_tag = DropdownTag.objects.all()
        ceker = Post.objects.get(page_link=self.kwargs[page_link])

        context['ceker'] = ceker
        context['dd_tag'] = dd_tag
        context['cat'] = cat
        context['sub_page'] = subPage
        context['related'] = related
        context['latest'] = latest
        context['main'] = main
        context['links'] = links
        return context


def userview(req, page_link):
    template = 'admini/preview_user.html'
    post = Post.objects.filter(page_link=page_link)

    if post.exists():
        post = post.first()

    link = SubPage.objects.all()
    link = link.filter(parent_page=post.pk)
    con = {
        'post': post,
        'links': link,
    }
    return render(req, template, con)


def UserViewSubPage(req, page_link, sub_page_link):
    template = 'admini/preview_user.html'
    post = Post.objects.filter(page_link=page_link)
    subpage = SubPage.objects.filter(page_link=sub_page_link)
    con = {
        'post': post,
        'subpage': subpage
    }
    return render(req, template, con)


class UserViewSubPageData(DetailView):
    model = SubPage
    query_pk_and_slug = True
    slug_field = page_link
    slug_url_kwarg = page_link
    template_name = 'user/subpage.html'
    context_object_name = 'post'

    def get_context_data(self, *args, **kwargs):
        context = super(UserViewSubPageData, self).get_context_data(*args, **kwargs)
        sub = SubPage.objects.get(page_link=self.kwargs['page_link'])
        main_title = Post.objects.get(title=sub.parent_page)
        related = SubPage.objects.filter(parent_page=main_title, stats='ACTIVE')
        related2 = Post.objects.filter(category=main_title.category)
        main = IndexEditor.objects.get(pk=1)
        links = SideLinkForIndex.objects.all()
        latest = Post.objects.all().order_by('-update_date')[:4]
        dd_tag = DropdownTag.objects.all()
        ceker = SubPage.objects.get(page_link=self.kwargs[page_link])

        context['ceker'] = ceker
        context['dd_tag'] = dd_tag
        context['related'] = related
        context['related2'] = related2
        context['main_title'] = main_title
        context['latest'] = latest
        context['main'] = main
        context['links'] = links
        return context


class testing(TemplateView):
    template_name = '404.html'

    # def get_context_data(self, *args, **kwargs):
    #     con = super(testing, self).get_context_data(*args, **kwargs)
    #     main = IndexEditor.objects.get(pk=1)
    #     links = SideLinkForIndex.objects.all()
    #     dd_tag = DropdownTag.objects.all()
    #     sub_latest = SubPage.objects.all().order_by('-update_date')[:3]
    #     older = Post.objects.all().order_by('update_date')
    #
    #     con['sub_latest'] = sub_latest
    #     con['dd_tag'] = dd_tag
    #     con['main'] = main
    #     con['links'] = links
    #     con['older'] = older
    #     return con


class index(TemplateView):
    template_name = 'user/index.html'

    def get_context_data(self, *args, **kwargs):
        con = super(index, self).get_context_data(*args, **kwargs)
        main = IndexEditor.objects.get(pk=1)
        links = SideLinkForIndex.objects.all()
        latest = Post.objects.all().filter(stats='ACTIVE').order_by('-update_date')[:4]
        dd_tag = DropdownTag.objects.all()
        sub_latest = SubPage.objects.all().filter(stats='ACTIVE').order_by('-update_date')[:3]

        con['sub_latest'] = sub_latest
        con['dd_tag'] = dd_tag
        con['latest'] = latest
        con['main'] = main
        con['links'] = links
        return con


class UserCategoryView(DetailView):
    query_pk_and_slug = True
    model = Category
    slug_field = category_link
    slug_url_kwarg = category_link
    template_name = 'user/cate.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UserCategoryView, self).get_context_data(*args, **kwargs)
        related = Post.objects.filter(category=Category.objects.get(category_link=self.kwargs[category_link]),
                                      stats='ACTIVE')
        ceker = Category.objects.get(category_link=self.kwargs[category_link])
        main = IndexEditor.objects.get(pk=1)
        links = SideLinkForIndex.objects.all()
        latest = Post.objects.all().order_by('-update_date')[:4]
        dd_tag = DropdownTag.objects.all()

        context['dd_tag'] = dd_tag
        context['ceker'] = ceker
        context['related'] = related
        context['latest'] = latest
        context['main'] = main
        context['links'] = links
        return context


class SearchResultView(ListView):
    model = Post
    template_name = 'user/result.html'
    ordering = ['title']
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super(SearchResultView, self).get_context_data(*args, **kwargs)
        main = IndexEditor.objects.get(pk=1)
        links = SideLinkForIndex.objects.all()
        dd_tag = DropdownTag.objects.all()

        context['dd_tag'] = dd_tag
        context['main'] = main
        context['links'] = links
        return context

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q is not None:
            object_list = Post.objects.filter(
                __(title__icontains=q) | __(quote__icontains=q) | __(body__icontains=q) |
                __(meta_keyword__icontains=q) | __(meta_description__icontains=q) | __(page_link__icontains=q) |
                __(update_date__icontains=q)
            )
            object_list = object_list.filter(stats='ACTIVE')
        else:
            object_list = Post.objects.filter(stats='ACTIVE')

        return object_list


class OlderPost(ListView):
    model = Post
    ordering = ['update_date']
    template_name = 'user/older.html'

    def get_context_data(self, *args, **kwargs):
        context = super(OlderPost, self).get_context_data(*args, **kwargs)
        main = IndexEditor.objects.get(pk=1)
        links = SideLinkForIndex.objects.all()
        dd_tag = DropdownTag.objects.all()

        context['dd_tag'] = dd_tag
        context['links'] = links
        context['main'] = main
        return context

    def get_queryset(self):
        qq = self.request.GET.get('q')

        if qq is not None:
            object_list = Post.objects.filter(
                __(title__icontains=qq) | __(title_tag__icontains=qq) | __(quote__icontains=qq) |
                __(body__icontains=qq) | __(meta_keyword__icontains=qq) | __(meta_description__icontains=qq)
            )
            object_list.filter(stats='ACTIVE')
        else:
            object_list = Post.objects.filter(stats='ACTIVE')

        return object_list
