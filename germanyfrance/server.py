#coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import config
import torndb
import  redis

from tornado.options import define,options
from tornado.web import RequestHandler
from urls import urls
from handlers.Passport import IndexHandler

define("port",type=int,default=8000,help="run server on the given port")

class Application(tornado.web.Application):
	"""docstring for Application"""
	def __init__(self, *arg,**kwargs):
		super(Application, self).__init__(*arg,**kwargs)
		#tornado.web.Application.__init__(self)
		# self.db = torndb.connect(
		# 	host = config.mysql_options["host"],
		# 	database = config.mysql_options["database"],
		# 	user = config.mysql_options["user"],
		# 	password = config.mysql_options["password"] 

		# 	)
		self.db = torndb.Connection(**config.mysql_options);
		#self.redis = redis.StrictRedis(**config.redis_opitons);


		

def main():
	
	options.log_file_prefix = config.log_file
	options.logging = config.log_level
	tornado.options.parse_command_line()

	app = Application(
	 	urls,**config.settings
	 	)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
	main()
