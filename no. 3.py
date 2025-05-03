class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)  # Perbaikan di sini
        return cls._instance

    def __init__(self, nama="Default"):
        if not hasattr(self, '_initialized'):
            self.nama = nama
            self._initialized = True

# Contoh Penggunaan
a = Singleton("Objek A")
b = Singleton("Objek B")

print(a is b)
print(a.nama)
print(b.nama)

b.nama = "Diubah lewat b"
print(a.nama)
print(b.nama)
