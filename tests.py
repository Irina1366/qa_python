import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):


        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_books(self, collector):
        
        collector.add_new_book('Ворона на мосту')
        assert collector.books_genre['Ворона на мосту'] == ''

    def test_add_new_book_length_more_40(self, collector):    
        collector.add_new_book("Что делать, если ваш кот хочет вас убить, а у вас лапки")
        assert "Что делать, если ваш кот хочет вас убить, а у вас лапки" not in collector.books_genre

    def test_add_new_book_length_is_0(self, collector):
        collector.add_new_book("")
        assert "" not in collector.books_genre

    def test_get_list_of_favorites_books_have_books(self, collector_with_name):
        collector_with_name.add_book_in_favorites('Зов ктулху')
        collector_with_name.add_book_in_favorites('Алладин')
        assert 'Алладин' and 'Зов ктулху' in collector_with_name.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Ворона на мосту')
        collector.add_book_in_favorites('Ворона на мосту')
        collector.delete_book_from_favorites('Ворона на мосту')
        assert 'Ворона на мосту' not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Ворона на мосту')
        collector.add_book_in_favorites('Ворона на мосту')
        assert 'Ворона на мосту' in collector.get_list_of_favorites_books()

    def test_add_duplicate_book_in_favorites(self, collector):
        collector.add_new_book('Ворона на мосту')
        collector.add_book_in_favorites('Ворона на мосту')
        collector.add_book_in_favorites('Ворона на мосту')
        assert collector.get_list_of_favorites_books().count('Ворона на мосту') == 1

    def test_get_books_genre(self, collector_with_name):
        assert collector_with_name.get_books_genre() == {
        'Убийство в восточном экспрессе': 'Детективы', 
        'Зов ктулху': 'Ужасы',
        'Алладин': 'Мультфильмы',
        'Денискины рассказы': 'Комедии',
        'Путешествие к центру земли': 'Фантастика',
        'Рассказы о Шерлоке Холмсе': 'Детективы'
        }

    def test_get_books_with_specific_genre(self, collector_with_name):
        assert collector_with_name.get_books_with_specific_genre('Детективы') == ['Убийство в восточном экспрессе', 
                                                                                  'Рассказы о Шерлоке Холмсе']

    def test_set_book_genre(self, collector):
        collector.add_new_book('Убийство в восточном экспрессе')
        collector.set_book_genre('Убийство в восточном экспрессе', 'Детективы')
        assert collector.get_book_genre('Убийство в восточном экспрессе') == 'Детективы'

    def test_set_book_genre_invalid(self,collector):
        collector.add_new_book('Ворона на мосту')
        collector.set_book_genre('Ворона на мосту', 'Поэзия')
        assert collector.get_book_genre('Ворона на мосту') == ''

    def test_get_books_for_children(self, collector_with_name):
        assert 'Алладин' and 'Путешествие к центру земли' and 'Денискины рассказы' in collector_with_name.get_books_for_children()

    def test_get_books_for_children_list_is_no_age_rating(self, collector_with_name):       
        assert 'Убийство в восточном экспрессе' and 'Зов ктулху' not in collector_with_name.get_books_for_children()


