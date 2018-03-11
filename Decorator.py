# coding=utf-8

from functools import wraps

HOST_DOCKER = 0


def docker_host_required(f):
    @wraps(f)
    def wrapper(*args, **kwarg):
        if args[0].type != HOST_DOCKER:
            raise Exception("NOT docker host")
        else:
            return f(*args, **kwarg)
    return wrapper


class Host(object):
    def __init__(self, type):
        self.type = type

    @docker_host_required
    def create_container(self):
        print("create container")


if __name__ == '__main__':
    host = Host(HOST_DOCKER)
    host.create_container()
    print("")

    host = Host(1)
    host.create_container()
