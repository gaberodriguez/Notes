# [START imports]
import os

import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)


# [END imports]



# [START main_page]
class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
    	t = jinja_env.get_template(template)
    	return t.render(params)

    def render(self, template, **kw):
    	self.write(self.render_str(template, **kw))

#class addproduct(webapp2.RequestHandler):
#    def get(self):
#        template = JINJA_ENVIROMENT.get_template('stage1.html')
#        self.response.write(template.render())


class MainPage(Handler):
    def get(self):
       self.render("stage1.html")

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ], debug=True)
