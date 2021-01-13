"""Api documentation view implementations."""

# Django
from django.shortcuts import render

# Project
from apidocumentation.tree_model import ApiDocumentationTreeModel


def api_documentation(request):
    return render(request, 'apidocumentation/content.html', {'tree_model': ApiDocumentationTreeModel})
