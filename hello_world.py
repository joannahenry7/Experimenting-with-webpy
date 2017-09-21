import web

urls = (
    "/(.*)/", "redirect",
    "/(.*)", "hello"
)

app = web.application(urls, globals())

render = web.template.render('templates/')


class redirect:
    def GET(self, path):
        web.seeother('/' + path)


class hello:
    def GET(self, name):
        # i = web.input(name=None)
        return render.index(name)


if __name__ == "__main__":
    app.run()
