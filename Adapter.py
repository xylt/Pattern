# coding=utf-8


class OldCourse(object):

    def show(self):
        print("show description")
        print("show teather of course")
        print("show labs")


class Page(object):

    def __init__(self, course):
        self.course = course

    def render(self):
        self.course.show()


class NewCourse(object):

    def show_desc(self):
        print("show description")

    def show_teacher(self):
        print("show teather of course")

    def show_labs(self):
        print("show labs")


class Adapter(object):

    def __init__(self, course):
        self.course = course

    def show(self):
        self.course.show_desc()
        self.course.show_teacher()
        self.course.show_labs()


if __name__ == '__main__':
    old_course = OldCourse()
    page = Page(old_course)
    page.render()
    print("")
    new_course = NewCourse()
    adapter = Adapter(new_course)
    page = Page(adapter)
    page.render()
