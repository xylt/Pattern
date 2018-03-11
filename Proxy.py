# coding=utf-8

from time import sleep


class Redis(object):
    def __init__(self):
        self.cache = dict()

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value):
        self.cache[key] = value


class Image(object):
    def __init__(self, name):
        self.name = name

    @property
    def url(self):
        sleep(2)
        return "https://dn-syl-static.qbox.me/img/logo-transparent.png"


class Page(object):
    def __init__(self, image):
        self.image = image

    def render(self):
        print(self.image.url)


redis = Redis()


class ImageProxy(object):
    def __init__(self, image):
        self.image = image

    @property
    def url(self):
        addr = redis.get(self.image.name)
        if not addr:
            addr = self.image.url
            print("Set url in redis cache!")
            redis.set(self.image.name, addr)
        else:
            print("Get url from redis cache!")

        return addr


if __name__ == '__main__':
    img = Image(name="logo")
    proxy = ImageProxy(img)
    page = Page(proxy)
    # first access
    page.render()
    print("")
    # seconed access
    page.render()
