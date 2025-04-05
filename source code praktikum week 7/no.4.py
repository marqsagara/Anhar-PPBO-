def uppercase_class(cls):
    cls.TITLES = tuple(title.upper() for title in cls.TITLES)
    return cls

@uppercase_class
class Passenger:
    TITLES = ("Mr", "Mrs", "Ms")

    def __init__(self, title, fname, lname):
        if title not in self.TITLES:
            raise ValueError(f"{title} is not a valid title.")

        self.title = title
        self.fname = fname
        self.lname = lname

# Pembuatan objek
p1 = Passenger("MR", "Kiewlamphone", "Souvanlith")
print(p1.TITLES)  # Output: ('MR', 'MRS', 'MS')
