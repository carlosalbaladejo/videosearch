from django_elasticsearch_dsl import (
    Document,
    fields,
    Index,
)

from .models import Movie

movie_index = Index('movie')

movie_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@movie_index.doc_type
class MovieDocument(Document):
    class Index:
        title = fields.TextField(
            attr='name',
            fields={
                'suggest': fields.Completion(),
            }
        )

    class Django:
        model = Movie
        fields = [
            'title',
            'file',
        ]
