class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2},
        'sms': {'number': 1000, 'price': 10},
        'voice': {'number': 1000, 'price': 15},
    }

    def update_price(self, service, new_price):
        if service in self.services:
            self.services[service]['price'] = new_price
            return True
        return False

class View(object):
    def list_services(self, services):
        print("Services Provided:")
        for svc in services:
            print(svc)
        print()

    def list_pricing(self, services):
        print("Pricing for Services:")
        for svc in services:
            print(f"For {services[svc]['number']} {svc} message you pay $ {services[svc]['price']}")
        print()

    def get_bid_input(self):
        return input("What service do you want to bid? email, sms, or voice : ").lower()

    def get_price_input(self):
        while True:
            try:
                price = float(input("Enter the price you want (in $): "))
                return price
            except ValueError:
                print("Invalid input. Please enter a numeric price.")

    def display_bid_result(self, service, price):
        print(f"Price according to your bid:")
        print(f"For {Model.services[service]['number']} {service} message you pay $ {price}")
        print()

class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def show_services_and_pricing(self):
        services = self.model.services.keys()
        self.view.list_services(services)
        self.view.list_pricing(self.model.services)

    def handle_bid(self):
        service_to_bid = self.view.get_bid_input()
        if service_to_bid in self.model.services:
            bid_price = self.view.get_price_input()
            if self.model.update_price(service_to_bid, bid_price):
                self.view.display_bid_result(service_to_bid, bid_price)
            else:
                print("Failed to update price.")
        else:
            print("Invalid service selected.")

    def run(self):
        self.show_services_and_pricing()
        self.handle_bid()
        self.show_services_and_pricing() # Show updated pricing

# Instansiasi dan menjalankan program
controller = Controller()
controller.run()