#coding:utf-8

import logging 
from .BaseHandler import BaseHandler

class IndexHandler(BaseHandler):
	"""docstring for IndexHandler"""
	def  get(self):
		 logging.debug("debug msg")
		 logging.info("info msg")
		 logging.warning("warning msg")
		 logging.error("error msg")
		 print("print msg")

		 self.write("hello 林志颖德国c罗")