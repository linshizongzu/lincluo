#conding:utf-8

from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
	"""docstring for BaseHandler"""
	def __init__(self, arg):
		super(BaseHandler, self).__init__()
		self.arg = arg
	def prepare(self):
		pass
	def write_error(self,status_code,**kwargs):
		pass
	def set_default_headers(self):
		pass
	def initialize(self):
		pass
	def on_finish(self):
		pass
	@property
	def redis(self):
		return self.application.redis
	@property
	def db(self):
		return self.application.db
