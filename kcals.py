class Product:
    #kcal in 100g
    def __init__(self):
        self.list = []

    def add(self, name, kcal):
        s = {'name': name, 'kcal': kcal}
        self.list.append(s)

    def get_kcal(self, pr):
        for i in self.list:
            print(pr)
            if i['name'] == pr:
                return i

    def get_nam(self, name):
        for i in self.list:
            if i['name'] == name:
                return i

    def count(self):
        return len(self.list)

    def display_all(self):
        s = ''
        for i in self.list:
            s = s+'name: '+i['name']+' kcal: '+str(i['kcal'])+'\n'

        return s