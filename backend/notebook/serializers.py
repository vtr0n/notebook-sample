from rest_framework import serializers
from notebook.models import Notebook


class NotebookSerializer(serializers.ModelSerializer):
    """Notebook serializer"""
    class Meta:
        model = Notebook
        fields = ['id', 'message']