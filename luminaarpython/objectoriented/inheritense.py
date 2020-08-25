# parent


# child


# -----------------------------------------------
# super


# sub


# ------------------------------------------------
# base


# derived


# ------------------------------------

class Parent:
    def phone(self):
        print("have phone")


class Child(Parent):
    pass


c = Child()
c.phone()
