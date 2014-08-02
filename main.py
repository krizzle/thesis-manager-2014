import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

MAIN_PAGE_FOOTER_TEMPLATE = """\
    <form action="/sign?%s" method="post">
      <div><textarea name="content" rows="3" cols="60"></textarea></div>
      <div><input type="submit" value="Sign Guestbook"></div>
    </form>
    <hr>
    <form>Guestbook name:
      <input value="%s" name="guestbook_name">
      <input type="submit" value="switch">
    </form>
    <a href="%s">%s</a>
  </body>
</html>
"""

DEFAULT_GUESTBOOK_NAME = 'My_Guestbook'
DEFAULT_GUESTBOOK_NAME1 = 'James_Guestbook'
DEFAULT_GUESTBOOK_NAME2 = 'Krizzle_Guestbook'

# We set a parent key on the 'Greetings' to ensure that they are all in the same
# entity group. Queries across the single entity group will be consistent.
# However, the write rate should be limited to ~1/second.

def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME):
    """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
    return ndb.Key('Guestbook', guestbook_name)

def guestbook_key1(guestbook_name1=DEFAULT_GUESTBOOK_NAME1):
    """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
    return ndb.Key('Guestbook1', guestbook_name1)

def guestbook_key2(guestbook_name2=DEFAULT_GUESTBOOK_NAME2):
    """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
    return ndb.Key('Guestbook2', guestbook_name2)

class Greeting(ndb.Model):
    """Models an individual Guestbook entry."""
    author = ndb.UserProperty()
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

class Greeting1(ndb.Model):
    """Models an individual Guestbook entry."""
    author = ndb.UserProperty()
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

class Greeting2(ndb.Model):
    """Models an individual Guestbook entry."""
    author = ndb.UserProperty()
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

class Student(ndb.Model):
    first = ndb.StringProperty(indexed=False)
    last = ndb.StringProperty(indexed=False)
    studno = ndb.StringProperty(indexed=False)
    emailadd = ndb.StringProperty(indexed=False)

class Thesis(ndb.Model):
    title = ndb.StringProperty(indexed=False)
    description = ndb.StringProperty(indexed=False)
    year = ndb.StringProperty(indexed=False)
    status = ndb.StringProperty(indexed=False)

class Adviser(ndb.Model):
    nametitle = ndb.StringProperty(indexed=False)
    firstname = ndb.StringProperty(indexed=False)
    lastname = ndb.StringProperty(indexed=False)
    dept = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)
    phone = ndb.StringProperty(indexed=False)

class MainPage(webapp2.RequestHandler):

    def get(self):
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        greetings_query = Greeting.query(
            ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
        greetings = greetings_query.fetch(10)
        user = users.get_current_user()

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Hello, '+user.nickname()+'!'
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
            url_linktext = 'Login'

        template_values = {
            'greetings': greetings,
            'guestbook_name': urllib.quote_plus(guestbook_name),
            'url': url,
            'url_linktext': url_linktext,
            'urlname': urlname,
            'name': name
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

class MemberOnePage(webapp2.RequestHandler):

    def get(self):
        guestbook_name1 = self.request.get('guestbook_name1',
                                          DEFAULT_GUESTBOOK_NAME1)
        greetings_query1 = Greeting1.query(
            ancestor=guestbook_key1(guestbook_name1)).order(-Greeting1.date)
        greetings1 = greetings_query1.fetch(10)
        user = users.get_current_user()

        if users.get_current_user():
            url1 = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Hello, '+user.nickname()+'!'
            url_linktext1 = 'Logout'
        else:
            url1 = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
            url_linktext1 = 'Login'

        template_values = {
            'greetings1': greetings1,
            'guestbook_name1': urllib.quote_plus(guestbook_name1),
            'url1': url1,
            'url_linktext1': url_linktext1,
            'urlname': urlname,
            'name': name
        }

        template = JINJA_ENVIRONMENT.get_template('member_one.html')
        self.response.write(template.render(template_values))

class MemberTwoPage(webapp2.RequestHandler):

    def get(self):
        guestbook_name2 = self.request.get('guestbook_name2',
                                          DEFAULT_GUESTBOOK_NAME2)
        greetings_query2 = Greeting2.query(
            ancestor=guestbook_key2(guestbook_name2)).order(-Greeting2.date)
        greetings2 = greetings_query2.fetch(10)
        user = users.get_current_user()

        if users.get_current_user():
            url2 = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Hello, '+user.nickname()+'!'
            url_linktext2 = 'Logout'
        else:
            url2 = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
            url_linktext2 = 'Login'

        template_values = {
            'greetings2': greetings2,
            'guestbook_name2': urllib.quote_plus(guestbook_name2),
            'url2': url2,
            'url_linktext2': url_linktext2,
            'urlname': urlname,
            'name': name
        }

        template = JINJA_ENVIRONMENT.get_template('member_two.html')
        self.response.write(template.render(template_values))


class Guestbook(webapp2.RequestHandler):
    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each Greeting
        # is in the same entity group. Queries across the single entity group
        # will be consistent. However, the write rate to a single entity group
        # should be limited to ~1/second.
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        greeting = Greeting(parent=guestbook_key(guestbook_name))

        if users.get_current_user():
            greeting.author = users.get_current_user()

        greeting.content = self.request.get('content')
        greeting.put()

        query_params = {'guestbook_name': guestbook_name}
        self.redirect('/?' + urllib.urlencode(query_params))

class Guestbook1(webapp2.RequestHandler):

    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each Greeting
        # is in the same entity group. Queries across the single entity group
        # will be consistent. However, the write rate to a single entity group
        # should be limited to ~1/second.
        guestbook_name1 = self.request.get('guestbook_name1',
                                          DEFAULT_GUESTBOOK_NAME1)
        greeting1 = Greeting1(parent=guestbook_key1(guestbook_name1))

        if users.get_current_user():
            greeting1.author = users.get_current_user()

        greeting1.content = self.request.get('content')
        greeting1.put()

        query_params1 = {'guestbook_name1': guestbook_name1}
        self.redirect('/module-1/1?' + urllib.urlencode(query_params1))

class Guestbook2(webapp2.RequestHandler):

    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each Greeting
        # is in the same entity group. Queries across the single entity group
        # will be consistent. However, the write rate to a single entity group
        # should be limited to ~1/second.
        guestbook_name2 = self.request.get('guestbook_name2',
                                          DEFAULT_GUESTBOOK_NAME2)
        greeting2 = Greeting2(parent=guestbook_key2(guestbook_name2))

        if users.get_current_user():
            greeting2.author = users.get_current_user()

        greeting2.content = self.request.get('content')
        greeting2.put()

        query_params2 = {'guestbook_name2': guestbook_name2}
        self.redirect('/module-1/2?' + urllib.urlencode(query_params2))

class RecordPageHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Hello, '+user.nickname()+'!'
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
        template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
        }
        template = JINJA_ENVIRONMENT.get_template('home.html')
        self.response.write(template.render(template_values))

class StudentSuccessHandler(webapp2.RequestHandler):
    def get(self):
    	user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Hello, '+user.nickname()+'!'
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
        template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
        }
        template = JINJA_ENVIRONMENT.get_template('ssuccess.html')
        self.response.write(template.render(template_values))

class ThesisSuccessHandler(webapp2.RequestHandler):
    def get(self):
    	user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Hello, '+user.nickname()+'!'
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
        template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
        }
        template = JINJA_ENVIRONMENT.get_template('tsuccess.html')
        self.response.write(template.render(template_values))

class AdviserSuccessHandler(webapp2.RequestHandler):
    def get(self):
    	user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Hello, '+user.nickname()+'!'
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
        template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
        }
        template = JINJA_ENVIRONMENT.get_template('asuccess.html')
        self.response.write(template.render(template_values))

class StudentListHandler(webapp2.RequestHandler):
    def get(self):
        studentt = Student.query().fetch()
        user = users.get_current_user()

        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Hello, '+user.nickname()+'!'
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''

        template_values = {
            'all_student': studentt,
            'url': url,
            'urlname': urlname,
            'name': name
        }

        template = JINJA_ENVIRONMENT.get_template('slist.html')
        self.response.write(template.render(template_values))

class StudentNewHandler(webapp2.RequestHandler):
    def get(self):
    	user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Hello, '+user.nickname()+'!'
            template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
            }
            template = JINJA_ENVIRONMENT.get_template('snew.html')
            self.response.write(template.render(template_values))
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
            template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
            }
            template = JINJA_ENVIRONMENT.get_template('login.html')
            self.response.write(template.render(template_values))

    def post(self):
        student = Student()
        student.first = self.request.get('first')
        student.last = self.request.get('last')
        student.studno = self.request.get('studno')
        student.emailadd = self.request.get('emailadd')
        student.put()
        self.redirect('/student/success')

class StudentViewHandler(webapp2.RequestHandler):
    def get(self, tid):
        studen = Student.query().fetch()
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Hello, '+user.nickname()+'!'
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
        template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
        }

        template_values = {
            "urlid": tid,
            "all_studen": studen,
            'url': url,
            'urlname': urlname,
            'name': name
        }
        template = JINJA_ENVIRONMENT.get_template('sview.html')
        self.response.write(template.render(template_values))

class StudentEditHandler(webapp2.RequestHandler):
    def get(self, tid):
        student = Student.query().fetch()
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Hello, '+user.nickname()+'!'
            template_values = {
            "urlid": tid,
            "all_student": student,
            'url': url,
            'urlname': urlname,
            'name': name
            }
            template = JINJA_ENVIRONMENT.get_template('sedit.html')
            self.response.write(template.render(template_values))

        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
            template_values = {
            "urlid": tid,
            "all_student": student,
            'url': url,
            'urlname': urlname,
            'name': name
            }
            template = JINJA_ENVIRONMENT.get_template('login.html')
            self.response.write(template.render(template_values))

    def post(self, tid):
        student = Adviser()
        student = Student.get_by_id(long(tid))
        student.first = self.request.get('first')
        student.last = self.request.get('last')
        student.studno = self.request.get('studno')
        student.emailadd = self.request.get('emailadd')
        student.put()
        self.redirect('/student/success')

class ThesisNewHandler(webapp2.RequestHandler):
    def get(self):
    	user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Hello, '+user.nickname()+'!'
            template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
            }
            template = JINJA_ENVIRONMENT.get_template('tnew.html')
            self.response.write(template.render(template_values))
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
            template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
            }
            template = JINJA_ENVIRONMENT.get_template('login.html')
            self.response.write(template.render(template_values))

    def post(self):
        thesis = Thesis()
        thesis.title = self.request.get('title')
        thesis.description = self.request.get('description')
        thesis.year = self.request.get('year')
        thesis.status = self.request.get('status')
        thesis.put()
        self.redirect('/thesis/success')

class ThesisListHandler(webapp2.RequestHandler):
    def get(self):
        thesiss = Thesis.query().fetch()
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Hello, '+user.nickname()+'!'
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''
        template_values = {
        	'all_thesis': thesiss,
            'url': url,
            'urlname': urlname,
            'name': name
        }

        template = JINJA_ENVIRONMENT.get_template('tlist.html')
        self.response.write(template.render(template_values))

class ThesisViewHandler(webapp2.RequestHandler):
    def get(self, tid):
        thesi = Thesis.query().fetch()
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Hello, '+user.nickname()+'!'

        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''

        template_values = {
            "urlid": tid,
            "all_thesi": thesi,
            'url': url,
            'urlname': urlname,
            'name': name
        }
        template = JINJA_ENVIRONMENT.get_template('tview.html')
        self.response.write(template.render(template_values))

class ThesisEditHandler(webapp2.RequestHandler):
    def get(self, tid):
        thesis = Thesis.query().fetch()
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Hello, '+user.nickname()+'!'
            template_values = {
            "urlid": tid,
            "all_thesis": thesis,
            'url': url,
            'urlname': urlname,
            'name': name
            }
            template = JINJA_ENVIRONMENT.get_template('tedit.html')
            self.response.write(template.render(template_values))
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''

            template_values = {
            "urlid": tid,
            "all_thesis": thesis,
            'url': url,
            'urlname': urlname,
            'name': name
            }
            template = JINJA_ENVIRONMENT.get_template('login.html')
            self.response.write(template.render(template_values))

    def post(self, tid):
        thesis = Thesis()
        thesis = Thesis.get_by_id(long(tid))
        thesis.title = self.request.get('title')
        thesis.description = self.request.get('description')
        thesis.year = self.request.get('year')
        thesis.status = self.request.get('status')
        thesis.put()
        self.redirect('/thesis/success')


class AdviserNewHandler(webapp2.RequestHandler):
    def get(self):
    	user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Hello, '+user.nickname()+'!'
            template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
            }
            template = JINJA_ENVIRONMENT.get_template('anew.html')
            self.response.write(template.render(template_values))
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''

            template_values = {
            'url': url,
            'urlname': urlname,
            'name': name
            }
            template = JINJA_ENVIRONMENT.get_template('login.html')
            self.response.write(template.render(template_values))

    def post(self):
        adviser = Adviser()
        adviser.nametitle = self.request.get('nametitle')
        adviser.firstname = self.request.get('firstname')
        adviser.lastname = self.request.get('lastname')
        adviser.dept = self.request.get('dept')
        adviser.email = self.request.get('email')
        adviser.phone = self.request.get('phone')
        adviser.put()
        self.redirect('/adviser/success')

class AdviserListHandler(webapp2.RequestHandler):
    def get(self):
        adviserr = Adviser.query().fetch()
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Hello, '+user.nickname()+'!'
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''

        template_values = {
        	'all_adviser': adviserr,
            'url': url,
            'urlname': urlname,
            'name': name
        }

        template = JINJA_ENVIRONMENT.get_template('alist.html')
        self.response.write(template.render(template_values))

class AdviserViewHandler(webapp2.RequestHandler):
    def get(self, tid):
        advise = Adviser.query().fetch()
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Hello, '+user.nickname()+'!'
        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''

        template_values = {
            "urlid": tid,
            "all_advise": advise,
            'url': url,
            'urlname': urlname,
            'name': name
        }
        template = JINJA_ENVIRONMENT.get_template('aview.html')
        self.response.write(template.render(template_values))

class AdviserEditHandler(webapp2.RequestHandler):
    def get(self, tid):
        adviser = Adviser.query().fetch()
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            urlname = 'Logout'
            name = 'Hello, '+user.nickname()+'!'
            template_values = {
            "urlid": tid,
            "all_adviser": adviser,
            'url': url,
            'urlname': urlname,
            'name': name
            }
            template = JINJA_ENVIRONMENT.get_template('aedit.html')
            self.response.write(template.render(template_values))

        else:
            url = users.create_login_url(self.request.uri)
            urlname = 'Login'
            name = ''

            template_values = {
            "urlid": tid,
            "all_adviser": adviser,
            'url': url,
            'urlname': urlname,
            'name': name
            }
            template = JINJA_ENVIRONMENT.get_template('login.html')
            self.response.write(template.render(template_values))

    def post(self, tid):
        adviser = Adviser()
        adviser = Adviser.get_by_id(long(tid))
        adviser.nametitle = self.request.get('nametitle')
        adviser.firstname = self.request.get('firstname')
        adviser.lastname = self.request.get('lastname')
        adviser.dept = self.request.get('dept')
        adviser.email = self.request.get('email')
        adviser.phone = self.request.get('phone')
        adviser.put()
        self.redirect('/adviser/success')


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
    ('/sign1', Guestbook1),
    ('/sign2', Guestbook2),
    ('/module-1/1', MemberOnePage),
    ('/module-1/2', MemberTwoPage),
    ('/records', RecordPageHandler),
    ('/student/new', StudentNewHandler),
    ('/student/list', StudentListHandler),
    ('/student/success', StudentSuccessHandler),
    ('/student/view/([^/]+)', StudentViewHandler),
    ('/student/edit/([^/]+)', StudentEditHandler),
    ('/thesis/new', ThesisNewHandler),
    ('/thesis/list', ThesisListHandler),
    ('/thesis/success', ThesisSuccessHandler),
    ('/thesis/view/([^/]+)', ThesisViewHandler),
    ('/thesis/edit/([^/]+)', ThesisEditHandler),
    ('/adviser/new', AdviserNewHandler),
    ('/adviser/list', AdviserListHandler),
    ('/adviser/success', AdviserSuccessHandler),
    ('/adviser/view/([^/]+)', AdviserViewHandler),
    ('/adviser/edit/([^/]+)', AdviserEditHandler)
], debug=True)