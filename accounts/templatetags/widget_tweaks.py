from django import template as A
B=A.Library()
@B.filter
def C(form_widget,css_class):return form_widget.as_widget(attrs={'class':css_class})