

class Singleton:
    instance = None

    @classmethod
    def getInstance(cls):
        if cls.instance == None:
            cls.instance = cls()
        return cls.instance

s1 = Singleton.getInstance()
s2 = Singleton.getInstance()

print(s1 is s2)  # True




