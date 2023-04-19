from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .serializer import *
from .models import *
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import rest_framework as filter
from django_filters.rest_framework import DjangoFilterBackend


class GenreModelViewSet(ModelViewSet):
    queryset = Genre.objects.filter()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'


class CharFilterInFilter(filter.BaseInFilter, filter.CharFilter):
    pass


class CardFilter(filter.FilterSet):
    genre = CharFilterInFilter(field_name='genre__id', lookup_expr='in')
    year = filter.RangeFilter()

    class Meta:
        model = Card
        fields = 'genre year'.split()


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['id', 'title']
    filterset_class = CardFilter
    permission_classes = ([IsAuthenticatedOrReadOnly])


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = ([IsAuthenticatedOrReadOnly])

    # def create_comment(self, serializer):
    #     serializer.save(author=self.request.user)


