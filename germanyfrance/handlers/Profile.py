#coding:utf-8

from .BaseHandler import BaseHandler
from utils.common import storage
class AvatarHandler(BaseHandler):
	"""docstring for AvatarHandler"""
	def post(self):
		try:
			image = self.request.files["avatar"][0]["body"]
	    except Exception as e:
		#
			logging.error(e)
			return self.write("")
		try:
			key = storage(image_data)
		except Exception as e:
			logging.error(e)
			return self.write("")
		try:
			self.db.execute("update ")
		except Exception as e:
			logging.error(e)

		return image_url