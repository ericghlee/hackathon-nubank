from django import template
from django.template import loader
from django import forms

register = template.Library()


class MaterializeFileInput(forms.FileInput):
    def render(self, name, value, attrs=None):
        template = loader.get_template('renders/file_field.html')
        url = getattr(value, 'url', None)
        context = {
            'url': url,
            'id_for_label': ''.join(['id_', name]),
            'name': name,
        }
        return template.render(context)


@register.filter(name='is_file_field')
def is_file_field(field):
    widget = field.field.widget
    types = (MaterializeFileInput, forms.FileInput, forms.ClearableFileInput)
    return isinstance(widget, types)
