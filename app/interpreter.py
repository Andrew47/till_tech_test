import json

class Interpreter(object):
    """Interprets the JSON doc"""
    def shopName(self):
        return self.read_json_file()[0]['shopName']

    def address(self):
        return self.read_json_file()[0]['address']

    def phone(self):
        return self.read_json_file()[0]['phone']

    def price(self, item):
        return self.read_json_file()[0]['prices'][0][item]

    def read_json_file(self):
        with open('hipstercoffee.json') as data_file:
            return json.load(data_file)
