import web

urls = (
    '/', 'Index',
    '/borrar', 'Borrar',
    '/editar', 'Editar',
    '/insertar', 'Insertar',
    '/lista', 'Lista',
    '/ver', 'Ver'
)
app = web.application(urls, globals()) 
render = web.template.render('views')

class Index:
    def GET(self):
        return render.index()

class Borrar:
    def GET(self):
        return render.borrar()

class Editar:
    def GET(self):
        return render.editar()

class Insertar:
    def GET(self):
        return render.insertar()

class Lista:
    def GET(self):
        return render.lista()

if __name__ == "__main__":
    app.run()