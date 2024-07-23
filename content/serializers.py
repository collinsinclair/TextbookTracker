from rest_framework import serializers

from .models import Author, Book, Chapter, Problem, Section


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "first_name", "last_name"]


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ["id", "title", "authors", "edition", "year"]


class ChapterSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Chapter
        fields = ["id", "book", "title", "number"]


class SectionSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer()

    class Meta:
        model = Section
        fields = ["id", "chapter", "title", "number", "started", "completed"]


class ProblemSerializer(serializers.ModelSerializer):
    section = SectionSerializer()

    class Meta:
        model = Problem
        fields = ["id", "section", "number", "done"]
