from rest_framework import serializers

from core.db_models.subject_db_model import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        read_only_fields = ['id',]
