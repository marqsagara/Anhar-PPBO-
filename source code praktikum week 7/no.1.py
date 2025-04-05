class Passenger:
    TITLES = ("Mr", "Mrs", "Ms")  # Class attribute

    def __init__(self, title, fname, lname):
        if title not in self.TITLES:
            raise ValueError("%s is not a valid title." % title)

        self.title = title  # Instance attribute
        self.fname = fname  # Instance attribute
        self.lname = lname  # Instance attribute

# Pembuatan Objek
p1 = Passenger("Dr", "Kiewlamphone", "Souvanlith")

# Mengakses class attribute drari object
print(p1.TITLES)  

# Mengakses class attribute dari kelas
print(Passenger.TITLES)  

# Mengakses instance attribute dari objek
print(p1.title)  

#mengakses instance attribute dari kelas
print (Passenger.title)

