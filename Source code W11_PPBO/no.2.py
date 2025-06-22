class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2},
        'sms': {'number': 1000, 'price': 10},
        'voice': {'number': 1000, 'price': 15},
    }

class View(object):
    def __init__(self, language="en"):
        self.language = language
        self.translations = {
            "en": {
                "services_provided": "Services Provided:",
                "pricing_for_services": "Pricing for Services:",
                "for": "For",
                "message_you_pay": "message you pay $",
                "choose_language": "Choose language (1 for English, 2 for Indonesia): ",
                "invalid_input": "Invalid input. Using default language (English).",
            },
            "id": {
                "services_provided": "Layanan yang Tersedia:",
                "pricing_for_services": "Harga Layanan:",
                "for": "Untuk",
                "message_you_pay": "pesan Anda membayar $",
                "choose_language": "Pilih bahasa (1 untuk Inggris, 2 untuk Indonesia): ",
                "invalid_input": "Input tidak valid. Menggunakan bahasa умолчанию (Inggris).",
            },
        }
        self.current_translation = self.translations[self.language]

    def set_language(self, language_code):
        if language_code in self.translations:
            self.language = language_code
            self.current_translation = self.translations[self.language]
        else:
            print(self.translations["en"]["invalid_input"])
            self.language = "en"
            self.current_translation = self.translations["en"]

    def list_services(self, services):
        print(self.current_translation["services_provided"])
        for svc in services:
            print(svc, '')

    def list_pricing(self, services):
        print(self.current_translation["pricing_for_services"])
        for svc in services:
            print(self.current_translation["for"], Model.services[svc]['number'],
                  svc, self.current_translation["message_you_pay"],
                  Model.services[svc]['price'])

class Controller(object):
    def __init__(self):
        self.view = View()
        self.model = Model()

    def set_language(self, choice):
        if choice == '1':
            self.view.set_language("en")
        elif choice == '2':
            self.view.set_language("id")
        else:
            self.view.set_language("en") # Default to English for invalid input

    def get_services(self):
        services = self.model.services.keys()
        return self.view.list_services(services)

    def get_pricing(self):
        services = self.model.services.keys()
        return self.view.list_pricing(services)

#Instansiasi objek dan pemilihan bahasa
controller = Controller()
language_choice = input(controller.view.current_translation["choose_language"])
controller.set_language(language_choice)

# Menampilkan layanan dan harga sesuai bahasa yang dipilih
controller.get_services()
print("\n")
controller.get_pricing()