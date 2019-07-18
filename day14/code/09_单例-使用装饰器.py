

def singleton(cls):  # cls: Dog类
    instance = None

    def inner(*args, **kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args, **kwargs)
        return instance

    return inner

@singleton
class Dog:
    pass

# Dog = singleton(Dog)

d1 = Dog()
d2 = Dog()

print(d1 is d2)  # True






