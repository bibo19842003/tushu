from rest_framework import serializers
from .models import Author, Sort, Publish, Bookinfor, Bookmember, Consume, Inoutrecord


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class SortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sort
        fields = '__all__'

class PublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = '__all__'

class BookinforSerializer(serializers.ModelSerializer):
    publisher = PublishSerializer(read_only=True)
    author_text = AuthorSerializer(read_only=True)
#    author_text = serializers.HyperlinkedIdentityField(view_name="article:detail")
    class Meta:
        model = Bookinfor
        fields = '__all__'

class BookmemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmember
        fields = '__all__'

class ConsumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consume
        fields = '__all__'

class InoutrecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inoutrecord
        fields = '__all__'



