class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationary):

    def draw(self):
        print('Запуск отрисовки ручкой.')


class Pencil(Stationary):

    def draw(self):
        print('Запуск отрисовки карандашом.')


class Handle(Stationary):

    def draw(self):
        print('Запуск отрисовки маркером.')


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')
stationery_knife = Stationary('канцелярский нож')

pen.draw()
pencil.draw()
handle.draw()
stationery_knife.draw()
