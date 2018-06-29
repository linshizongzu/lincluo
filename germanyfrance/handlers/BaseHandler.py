#conding:utf-8

from tornado.web import RequestHandler
from utils.session import Session 

class BaseHandler(RequestHandler):
	"""docstring for BaseHandler"""
	# def __init__(self, arg):
	# 	super(BaseHandler, self).__init__()
	# 	self.arg = arg
	def prepare(self):
		self.xsrf_token
		if self.request.headers.get("Content-Type","").startswith("application/json"):
			self.json_args = json.loads(self.request.body)
		else:
			self.json_args = None

	def write_error(self,status_code,**kwargs):
		pass
	def set_default_headers(self):
		self.set_header("Content-Type","application/json;charset=UTF-8")
	def initialize(self):
		pass
	def on_finish(self):
		pass
	def get_current_user(self):
		self.session = Session(self)
		return self.session.data
	@property
	def redis(self):
		return self.application.redis
	@property
	def db(self):
		return self.application.db

class StaticFileHandler(tornado.web.StaticFileHandler):
	"""docstring for StaticFileHandler"""
	def __init__(self, *args,**kwargs):
		super(StaticFileHandler, self).__init__(*args,**kwargs)
		
		














