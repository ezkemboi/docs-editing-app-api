from rest_framework import serializers
from .models import DefaultTemplate

# Here is docs on serializers 
# https://www.django-rest-framework.org/api-guide/fields/
# Creation of more validations for the fields here e.g required fields should be mentioned. 

class TemplateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    created = serializers.DateTimeField()
    documenttype = serializers.CharField()
    title = serializers.CharField()
    introduction = serializers.CharField()
    abstract = serializers.CharField()
    literaturereview = serializers.CharField()
    conclusion = serializers.CharField()
    references = serializers.CharField()

    class Meta:
        model = DefaultTemplate
        fields = (
            'slug', 'created', 'documenttype', 'title',
            'introduction', 'abstract', 'literaturereview',
            'conclusion', 'references'
        )

    def create(self, validation_data):
        # Creating a template
        return DefaultTemplate.objects.create(**validation_data)
    
    def update(self, instance, validation_data):
        # Update a template details
        instance.documenttype = validated_data.get('documenttype', instance.documenttype)
        instance.title = validated_data.get('title', instance.title)
        instance.introduction = validated_data.get('introduction', instance.introduction)
        instance.abstract = validated_data.get('abstract', instance.abstract)
        instance.literaturereview = validated_data.get('literaturereview', instance.literaturereview)
        instance.conclusion = validated_data.get('conclusion', instance.conclusion)
        instance.references = validated_data.get('references', instance.references)
        instance.save()
        return instance

    def delete(self, slug):
        # Delete a template from the list of existing documents
        return {"message": "Document deleted"}
