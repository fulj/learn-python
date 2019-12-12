class Foo:
  def bar(self, message):
    print(message)

Foo().bar("Hello, Python.")

class FooParent:
  def bar(self, message):
    print(message)
class FooChild(FooParent):
  def bar(self, message):
      super(FooChild, self).bar(message)
    # FooParent.bar(self, message)

FooChild().bar("Hello, Python..")