class Foo(object):
    def foo(self):
        return "Fail"

class Bar(object):
    def bar(self):
        # Bar depends on Foo instance so that when calling Foo() specific mock instance should be returned
        foo = Foo()
        return foo.foo()