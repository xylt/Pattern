# coding=utf-8

import abc


class Subject(object):
    """
    Observered
    """
    def __init__(self):
        self._observer = []

    def attach(self, observer):
        if observer not in self._observer:
            self._observer.append(observer)

    def detach(self, observer):
        try:
            self._observer.remove(observer)
        except ValueError:
            pass

    def notify(self):
        for observer in self._observer:
            observer.update(self)


class Course(Subject):
    def __init__(self):
        super(Course, self).__init__()
        self._message = None

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, msg):
        self._message = msg
        self.notify()


class Observer(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def update(self, subject):
        pass


class UserObserver(Observer):
    def update(self, subject):
        print("User observer: %s" % subject.message)


class OrgObserver(Observer):
    def update(self, subject):
        print("Organization observer: %s" % subject.message)


if __name__ == '__main__':
    # init observer
    user = UserObserver()
    org = OrgObserver()
    # init course
    course = Course()

    course.attach(user)
    course.attach(org)

    course.message = "2 observer"

    course.detach(user)

    course.message = "1 observer"
