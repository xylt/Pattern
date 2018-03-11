# coding=utf-8

import abc


class Fishing(object):

    __metaclass__ = abc.ABCMeta

    def finishing(self):
        self.prepare_bait()
        self.go_to_riverbank()
        self.find_location()
        print("start fishing")

    @abc.abstractmethod
    def prepare_bait(self):
        pass

    @abc.abstractmethod
    def go_to_riverbank(self):
        pass

    @abc.abstractmethod
    def find_location(self):
        pass


class JohnFishing(Fishing):
    def prepare_bait(self):
        print("buy bait")

    def go_to_riverbank(self):
        print("to river by driving")

    def find_location(self):
        print("select location on the island")


if __name__ == '__main__':
    f = JohnFishing()
    f.finishing()

