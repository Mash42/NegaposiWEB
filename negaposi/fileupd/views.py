from django.shortcuts import render
from django.http import HttpResponse
from fileupd.forms import PostDataForm
from .models import PostData
from django.views.generic import TemplateView
from django.core.files.storage import default_storage
from negaposi import settings as project_settings
import os


class PostListView(TemplateView):
    template_name = "fileupd/fileupd_list.html"

    def get(self, request, *args, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        post_list = PostData.objects.all()
        context['post_list'] = post_list

        return render(self.request, self.template_name, context)


def post_message(request):
    template_name = "fileupd/fileupd_form.html"
    form = None

    if request.method == 'POST':
        # フォームを受け取る
        form = PostDataForm(request.POST, request.FILES)

        if form.is_valid():
            file_obj = request.FILES['data_file']
            file_name = default_storage.save(file_obj.name, file_obj)
            # これでINSERT文(SQL)を発行してくれる
            PostData.objects.create(name=form.data['name'], email=form.data['email'], content_message=form.data['content_message'],
                                    file_name=file_name, file_path=project_settings.MEDIA_ROOT + os.sep + file_name)
    else:
        form = PostDataForm()

    return render(request, template_name, {'form1': form})
