from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    edition = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        authors = ", ".join([author.last_name for author in self.authors.all()])
        return f"{authors} - {self.title} ({self.edition}e, {self.year})"


class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    number = models.IntegerField(unique=True)

    def __str__(self):
        authors = ", ".join([author.last_name for author in self.book.authors.all()])
        return f"{authors} - {self.book.title}: {self.number} {self.title}"


class Section(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    number = models.IntegerField()

    class Meta:
        unique_together = ["chapter", "number"]

    def __str__(self):
        return f"{self.chapter.number}.{self.number} {self.title}"


class Problem(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    number = models.IntegerField()

    class Meta:
        unique_together = ["section", "number"]

    def __str__(self):
        authors = ", ".join(
            [author.last_name for author in self.section.chapter.book.authors.all()]
        )
        return f"{authors} {self.section.chapter.number}.{self.number} ({self.section.title})"
