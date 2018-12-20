from django.contrib import admin
from django import forms
from organisations.models import Organisation, OrganisationDivisionSet
from .common import CustomOrganisationChoiceField


class OrganisationDivisionSetAdminForm(forms.ModelForm):
    organisation = CustomOrganisationChoiceField(queryset=Organisation.objects.all())

    class Meta:
        model = OrganisationDivisionSet
        fields = "__all__"


class OrganisationDivisionSetAdmin(admin.ModelAdmin):
    ordering = ("organisation", "start_date")
    search_fields = (
        "organisation__official_name",
        "organisation__common_name",
        "organisation__official_identifier",
        "short_title",
    )
    form = OrganisationDivisionSetAdminForm
