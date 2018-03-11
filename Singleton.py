# coding = utf-8

class Singleton:
    """
    singleton partten + decorated(no pthread)
    """

    def __init__(self, cls):
        self._cls = cls

    def Instance(self):
        """
        return real instance
        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self, *args, **kwargs):
        raise TypeError("Singletons must be accessed through 'Instance()'.")


@Singleton
class A(object):
    """
    class of need singleton
    """
    def __init__(self):
        pass

    def display(self):
        """
        return current instance id
        """
        return id(self)

if __name__ == '__main__':
    s1 = A.Instance()
    s2 = A.Instance()
    print(id(s1), s1.display())
    print(id(s2), s2.display())
    print(s1 is s2)