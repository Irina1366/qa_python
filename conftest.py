import pytest

from main import BooksCollector

@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector 

@pytest.fixture
def collector_with_name():
    collector_with_name = BooksCollector()   
    collector_with_name.books_genre = {
        'Убийство в восточном экспрессе': 'Детективы', 
        'Зов ктулху': 'Ужасы',
        'Алладин': 'Мультфильмы',
        'Денискины рассказы': 'Комедии',
        'Путешествие к центру земли': 'Фантастика',
        'Рассказы о Шерлоке Холмсе': 'Детективы'
        }
    return collector_with_name 
