import os
from django.http import Http404
from django.shortcuts import render
from django.views.generic import View
from django.template.loader import render_to_string


class PageView(View):
    def get(self, request, slug, *args, **kwargs):
        page_template_path = 'backend/templates/page/pages/{}.html'.format(slug)

        if not os.path.exists(page_template_path):
            raise Http404('Static page "{}" not found.'.format(slug))

        return render(request, 'backend/templates/page/generic.html', context={
            'content': render_to_string(page_template_path)
        })

