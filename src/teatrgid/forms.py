from django import forms
from django.template import loader


class TinyMCEInput(forms.Widget):
    class Media:
        js = (
            'packages/tinymce/tinymce.min.js',
            'js/admin/tinymce-widget.js',
        )

    def render(self, name, value, attrs=None):

        if (value is None):
            value = ""

        context = {
            "name": name,
            "value": value,
        }

        template = loader.get_template('admin/tinymce-widget.html')
        return template.render(context)