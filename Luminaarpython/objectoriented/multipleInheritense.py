class Parent:
    def m1(self):
        print("inside parent1")


class Child:
    def m2(self):
        print("inside child")


class SubChild(Parent,Child):
    def m3(self):
        print("inside subchild")

#parent
p=Parent()
p.m1()
#child
c=Child()
c.m2()
#Subchild
sb=SubChild()
sb.m1()
sb.m2()
sb.m3()