from rest_framework import serializers

from core.db_models.faculty_db_model import Faculty


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['id', 'name', 'score',]
        read_only_fields = ['id',]