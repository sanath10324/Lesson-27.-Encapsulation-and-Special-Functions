class myClass:
    __privateVar = 27;

    def __privateMeth(self):
        print("I am inside clas myclass")

    def hello(self):
        print("Private Variable Value:",myClass.__privateVar)

foo = myClass()
foo.hello()
foo.__privateMeth