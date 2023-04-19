from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

from .models import Card, Genre, Comment


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'



class UserSimpleView(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = "id username email".split()

class CommentSerializer(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Comment
        fields = "id text author card".split()


class CardSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    genre_list = serializers.SerializerMethodField()

    class Meta:
        model = Card
        fields = "id title year description genre genre_list comments".split()

    def get_genre_list(self, card):
        return card.get_genre_list_from_m()


class CardCommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Card
        fields = ' author title comments'.split()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['comments'] = CommentSerializer(instance.comments.all(), many=True, context=self.context).data
        return representation


class CardValidateSerializer(serializers.Serializer):
    image = serializers.URLField(required=False, default='')
    title = serializers.CharField(required=True, max_length=250)
    year = serializers.IntegerField(required=False, default=1999)
    author_id = serializers.IntegerField(min_value=1)
    genre = serializers.ListField(child=serializers.IntegerField())

    def validate_title(self, title):
            title_exists = Card.objects.filter(title=title).exists()
            if not title_exists:
                return title
            raise ValidationError('Card with this title already exists')

    def validate_author_id(self, author_id):
        try:
            User.objects.get(id=author_id)
        except User.DoesNotExist:
            raise ValidationError('does not exist')
        return author_id

    def validate_genre(self, genre):
        if len(genre) == Genre.objects.filter(id__in=genre).count():
            return genre
        raise ValidationError('genre does not exist')



class CommentValidateSerializer(serializers.Serializer):
    author_id = serializers.IntegerField(default='Anonymous')
    text = serializers.CharField()
    card_id = serializers.IntegerField()
    def validate_card_id(self, card_id):
        card_exists = Card.objects.filter(id=card_id).exists()
        if card_exists:
            return card_id
        raise ValidationError('Card with this id already exists!')
