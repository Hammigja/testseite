# coding=utf-8
import os

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = ["Geschwindichkeit: 49 - 65 km/h ", "Lebenserwartung: 20-26 Jahre", "Gewicht: 90-310kg",
                 "Höhe: 70-120 cm", "Wissenschaftlicher Name: Panther tigries"]
        self.render("template.html", title="Die Tieger", items=items)


class UnterseiteHandler(tornado.web.RequestHandler):
    def get(self):
        items = []
        self.render("unterseite.html", title="Tieger Bilder", items=items)


class Unterseite2Handler(tornado.web.RequestHandler):
    def get(self):
        load_unterseite2(self)


class AadItemHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        new_line = self.get_argument("new_line")
        add_line('data.txt', new_line)


class DeleteItemHandler(tornado.web.RequestHandler):
    def post(self):
        zeile = self.get_argument("zeile")
        delete_row('data.txt', zeile)
        self.write('True')
        #print zeile


class DeleteAllHandler(tornado.web.RequestHandler):
    def post(self):
        delete_all('data.txt')
        self.write('True')


def load_unterseite2(self):
    # print new_line
    items = read_data('data.txt')
    # print items
    self.render("unterseite2.html", title="Übungseite", items=items)


def add_line(file, new_line):
    with open(file, "a+")as f:
        f.write(str(new_line + '\n'))


def delete_row(file, zeile):
    items = read_data(file)
    del items[int(zeile)]
    write_data(file, items)


def delete_all(file):
    items = {}
    write_data(file, items)

def write_data(file, items):
    # os.remove(file)
    with open(file, 'w+') as f:
        for zeile, inhalt in items.iteritems():
            print inhalt
            f.write(str(inhalt + '\n'))


def read_data(file):
    # read data from file and return list of data
    content = {}
    if os.path.isfile(file):
        with open(file) as f:
            content = f.readlines()

    _content = {}
    i = 0
    for zeile in content:
        i += 1
        _content[i] = zeile.replace('\n', '')

    return _content


if __name__ == "__main__":
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "debug": True
    }
    app = tornado.web.Application([
        (r"/", MainHandler),
        (r"/template.html", MainHandler),
        (r"/unterseite.html", UnterseiteHandler),
        (r"/unterseite2.html", Unterseite2Handler),
        (r"/delete_item", DeleteItemHandler),
        (r"/add_item", AadItemHandler),
        (r"/delete_all", DeleteAllHandler),
    ], **settings)
    app.listen(8888)
    print 'Listening on port 8888...'
    tornado.ioloop.IOLoop.current().start()
