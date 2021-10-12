from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, User

category_choices = Category.objects.all().values_list('name', 'name')
# parent_choices = ParentCheck.objects.all().values_list('sub', 'sub')
parent_choices = [('SINGLE', 'SINGLE'), ('PARENT', 'PARENT'), ]
url_choices = DropdownURL.objects.all().values_list('pk', 'name')

category_choices_list = []
url_choices_list = []

for category in category_choices:
    category_choices_list.append(category)

for url in url_choices:
    url_choices_list.append(url)


# parent_choices_list = []
#
# for parent in parent_choices:
#     parent_choices_list.append(parent)

# main_page_choices_list = []
#
# for main_page in main_page_choices:
#     main_page_choices_list.append(main_page)


def get_main_page_choices_list():
    main_page_choices = Post.objects.filter(parent_check=2).values_list('page_link', 'page_link')
    main_page_choices_list = []
    for main_page in main_page_choices:
        main_page_choices_list.append(main_page)
    return main_page_choices_list


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AdminCreatePostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title', 'title_tag', 'quote', 'header_img', 'page_link', 'category', 'parent_check', 'body',
            'meta_keyword', 'meta_description')

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'id': 'title', 'onchange': 'autotypelink();'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'id': 'title_tag'}),
            'quote': forms.TextInput(attrs={'class': 'form-control', 'id': 'quote', }),
            'header_img': forms.TextInput(attrs={'class': 'form-control', 'id': 'header_img'}),
            'page_link': forms.TextInput(attrs={'class': 'form-control', 'id': 'page_link', 'type': 'hidden'}),
            'category': forms.Select(choices=category_choices_list, attrs={'class': 'form-control', 'id': 'category'}),
            'parent_check': forms.Select(choices=parent_choices, attrs={'class': 'form-control', 'id': 'parent'}),
            'body': forms.Textarea(attrs={'class': 'form-control bdy', 'id': 'body'}),
            'meta_keyword': forms.Textarea(attrs={'class': 'form-control', 'id': 'meta_keyword', 'rows': '4'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'id': 'meta_description', 'rows': '4'}),
        }


class UpdatePostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title', 'title_tag', 'quote', 'header_img', 'page_link', 'category', 'parent_check', 'body',
            'meta_keyword', 'meta_description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'id': 'title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'id': 'title_tag'}),
            'quote': forms.TextInput(attrs={'class': 'form-control', 'id': 'quote', }),
            'header_img': forms.TextInput(attrs={'class': 'form-control', 'id': 'header_img', }),
            'page_link': forms.TextInput(attrs={'class': 'form-control', 'id': 'page_link', }),
            'category': forms.Select(choices=category_choices_list, attrs={'class': 'form-control', 'id': 'category'}),
            'parent_check': forms.Select(choices=parent_choices, attrs={'class': 'form-control', 'id': 'parent'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'id': 'body'}),
            'meta_keyword': forms.Textarea(attrs={'class': 'form-control', 'id': 'meta_keyword', 'rows': '4'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'id': 'meta_description', 'rows': '4'}),
        }


class AdminAddMoreCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'category_tag', 'quote', 'header_img', 'category_link', 'category_content', 'meta_keyword',
                  'meta_description')

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'id': 'name', 'onchange': 'autotypelink();'}),
            'category_tag': forms.TextInput(attrs={'class': 'form-control', 'id': 'category_tag'}),
            'quote': forms.TextInput(attrs={'class': 'form-control', 'id': 'quote'}),
            'header_img': forms.TextInput(attrs={'class': 'form-control', 'id': 'header_img'}),
            'category_link': forms.TextInput(attrs={'class': 'form-control', 'id': 'category_link', 'type': 'hidden'}),
            'category_content': forms.Textarea(attrs={'class': 'form-control', 'id': 'category_content'}),
            'meta_keyword': forms.Textarea(attrs={'class': 'form-control', 'id': 'meta_keyword', 'rows': '4'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'id': 'meta_description', 'rows': '4'}),
        }


class AdminUpdateCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'category_tag', 'quote', 'header_img', 'category_link', 'category_content', 'meta_keyword',
                  'meta_description')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'id': 'name'}),
            'category_tag': forms.TextInput(attrs={'class': 'form-control ', 'id': 'name'}),
            'quote': forms.TextInput(attrs={'class': 'form-control ', 'id': 'quote'}),
            'header_img': forms.TextInput(attrs={'class': 'form-control ', 'id': 'header_img'}),
            'category_link': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'name'}),
            'category_content': forms.Textarea(attrs={'class': 'form-control', 'id': 'name'}),
            'meta_keyword': forms.Textarea(attrs={'class': 'form-control', 'id': 'meta_keyword', 'rows': '4'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'id': 'meta_description', 'rows': '4'}),
        }


class AdminCreateSubPageForm(forms.ModelForm):
    class Meta:
        model = SubPage
        fields = (
            'title', 'title_tag', 'quote', 'header_img', 'page_link', 'body', 'meta_keyword',
            'meta_description')

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'id': 'sub_title', 'onchange': 'autotypelink()'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'id': 'sub_title_tag'}),
            'quote': forms.TextInput(attrs={'class': 'form-control', 'id': 'quote'}),
            'header_img': forms.TextInput(attrs={'class': 'form-control', 'id': 'header_img'}),
            'page_link': forms.TextInput(attrs={'class': 'form-control', 'id': 'sub_page_link', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'id': 'body'}),
            # 'parent_page': forms.Select(choices=get_main_page_choices_list(),
            #                             attrs={'class': 'form-control', 'id': 'parent_page'}),
            'meta_keyword': forms.Textarea(attrs={'class': 'form-control', 'id': 'meta_keyword', 'rows': '4'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'id': 'meta_description', 'rows': '4'}),
        }


class AdminUpdateSubPageForm(forms.ModelForm):
    class Meta:
        model = SubPage
        fields = ('title', 'title_tag', 'page_link', 'body', 'parent_page', 'meta_keyword', 'meta_description')

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'id': 'sub_title', 'onchange': 'autotypelink()'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'sub_title_tag'}),
            'page_link': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'sub_page_link'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'id': 'body'}),
            'parent_page': forms.Select(choices=get_main_page_choices_list(),
                                        attrs={'class': 'form-control', 'id': 'parent_page'}),
            'meta_keyword': forms.Textarea(attrs={'class': 'form-control', 'id': 'meta_keyword', 'rows': '4'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'id': 'meta_description', 'rows': '4'}),
        }


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = '__all__'

        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-control', 'id': 'input-file-now', 'type': 'file'})
        }


class IndexEditorForm(forms.ModelForm):
    class Meta:
        model = IndexEditor
        fields = ('title', 'title_tag', 'brand', 'header_img', 'body_content', 'meta_keyword', 'meta_description',
                  'copyright_content')

        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'id': 'brand'}),
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'id': 'title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'id': 'title_tag'}),
            'header_img': forms.TextInput(attrs={'class': 'form-control', 'id': 'header_img'}),
            'body_content': forms.Textarea(attrs={'class': 'form-control', 'id': 'body_content'}),
            'meta_keyword': forms.Textarea(attrs={'class': 'form-control', 'id': 'meta_keyword', 'rows': '4'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'id': 'meta_description', 'rows': '4'}),
            'copyright_content': forms.Textarea(
                attrs={'class': 'form-control', 'id': 'copyright_content', 'rows': '4'}),
        }


class CreateLinksIndexForm(forms.ModelForm):
    class Meta:
        model = SideLinkForIndex
        fields = ('name', 'url')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'id': 'url'}),
        }


class EditLinkIndexForm(forms.ModelForm):
    class Meta:
        model = SideLinkForIndex
        fields = ('name', 'url')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'id': 'url'}),
        }


class AddDropdownURL(forms.ModelForm):
    class Meta:
        model = DropdownURL
        fields = ('name', 'url')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'id': 'url'}),
        }


class EditDropdownURL(forms.ModelForm):
    class Meta:
        model = DropdownURL
        fields = ['name', 'url']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'id': 'url'}),
        }


class AddDropdownTag(forms.ModelForm):
    class Meta:
        model = DropdownTag
        fields = ['name', 'links']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'links': forms.CheckboxSelectMultiple(choices=url_choices_list,
                                                  attrs={'class': 'form-check-input', 'id': 'list-unstyled'})
        }


class EditDropdownTag(forms.ModelForm):
    class Meta:
        model = DropdownTag
        fields = ['name', 'links']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'links': forms.CheckboxSelectMultiple(choices=url_choices_list,
                                                  attrs={'class': 'form-check-input', 'id': 'list-unstyled'})
        }