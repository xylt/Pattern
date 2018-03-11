# coding=utf-8

import random
import abc

class Product_A_1(object):

    def get_info(self):
        return "A_1"

    def __str__(self):
        return "A_1"


class Product_A_2(object):

    def get_info(self):
        return "A_2"

    def __str__(self):
        return "A_2"


class Product_B_1(object):

    def get_info(self):
        return "B_1"

    def __str__(self):
        return "B_1"


class Product_B_2(object):

    def get_info(self):
        return "B_2"

    def __str__(self):
        return "B_2"


class Factory(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_product_1(self):
        pass

    @abc.abstractmethod
    def create_product_2(self):
        pass


class ProductAFactory(Factory):

    def create_product_1(self):
        return Product_A_1()

    def create_product_2(self):
        return Product_A_2()


class ProductBFactory(Factory):

    def create_product_1(self):
        return Product_B_1()

    def create_product_2(self):
        return Product_B_2()


def get_factory():
    """
    random select a factory
    """
    return random.choice([ProductAFactory, ProductBFactory])()

if __name__ == '__main__':
    factory = get_factory()
    product1 = factory.create_product_1()
    product2 = factory.create_product_2()
    print(product1.get_info())
    print(product2.get_info())
