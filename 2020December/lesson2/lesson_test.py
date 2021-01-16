import pytest
from datetime import datetime
from .Lesson.lesson import Lesson


@pytest.fixture(scope="function")
def create_lesson_one():
    lesson = Lesson(lesson_name='lesson1',
                    lesson_date='2020-12-21',
                    course_name="Python QA Engineer",
                    module="Introduction",
                    link='')
    return lesson


@pytest.fixture(scope="class")
def create_lesson_two():
    lesson2 = Lesson(lesson_name='lesson2',
                     lesson_date='2020-12-28',
                     course_name="Python QA Engineer",
                     module="Introduction",
                     link='')
    return lesson2


@pytest.mark.skipif(2 == 2, reason="2 == 2")
def test_exit():
    assert 1 - 1 == 0


class TestLesson:

    @pytest.mark.smoke
    def test_lesson_one(self, create_lesson_one, create_lesson_two, set_time):
        """
        проверка того что лекция 1 раньше чем лекция 2
        """
        assert datetime.fromisoformat(create_lesson_one.get_lesson_date()) < \
               datetime.fromisoformat(create_lesson_two.get_lesson_date())

    @pytest.mark.smoke
    def test_lesson_two(self, create_lesson_one, create_lesson_two):
        """
        TODO: "Проверить что оба объекта lesson относятся к одному модулю"
        """
        assert create_lesson_one.get_module() == create_lesson_two.get_module()
