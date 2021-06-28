import django_filters
from django_filters import CharFilter, ChoiceFilter
from .models import Note


class NoteFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name", lookup_expr="icontains")
    label = CharFilter(field_name="label", lookup_expr="icontains")
    user = CharFilter(field_name="user", lookup_expr="icontains")
    class Meta:
        model = Note
        fields = '__all__'
        exclude = [ 'file', 'coverImage', 'uploadedBy', 'dateUploaded', 'impressions', 'description' ]


