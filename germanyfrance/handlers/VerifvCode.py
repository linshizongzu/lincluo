#coding:utf-8
import logging
import constants
import random
from .BaseHandler import BaseHandler
from utils.captcha  import captcha

class ImageCodeHandler(BaseHandler):
	"""docstring for ClassName"""
	def get(self):
		code_id = self.get_argument("codeid")
		pre_code_id = self.get_argument("pcodeid")
		if pre_code_id:
			try:
				self.redis.delete("image_code_%s" % pre_code_id)
			except Exception as e:
				logging.error(e)
		#name   
		#text
		#image 
		name,text,image = generate_captcha()
		try:
			self.redis.setex("image_code_%s"%code_id,IMAGE_CODE_EXPIRES_SECONDS,text)
		except Exception as e:
			logging.error(e)
			self.write("")
		self.set_header("ContentType","image/jpg")
		self.write(image)
林志颖林氏家族林心如林志颖林氏家族林心如林氏宗族林氏林氏林氏林氏林氏
林氏林氏林氏林氏林氏林氏林林氏

class PhoneCodeHandler(BaseHandler):
	"""docstring for ClassName"""
	def post(self):
		#获取参数
		#判断图片
		#若成功：
		#发送短信
		#不成功
		#返回错误信息
		mobile = self.json_args.get("mobile")
		image_code_id = self.json_args.get("image_code_id")
		image_code_text = self.json_args.get("image_code_text")
		if not all((mobile,image_code_id,image_code_text))
			return self.write(dict(errno = RET.PARAMERR,errmsg="参数不完整"))
		if not re.match(r"1\d{10}",mobile):
			return self.write(dict(errno=RET.PARAMERR,errmsg="手机号错误"))
		try:
			real_image_code_text = self.redis.get("image_code_%s" % image_code_id)

		except Exception as e:
			return self.write(dict(errno=RET.DBERR,errmsg="查询出错"))
		if not real_image_code_text:
			return self.write(dict(errno=RET.NODATA,errmsg="验证码过期!"))
		if real_image_code_text.lower()!=image_code_text.lower():
			return self.write(dict(errno=RET.DATAERR,errmsg="验证码错误!"))
		sms_code = "%04d" % random.randint(0,9999)
		try:
			self.redis.setex("sms_code_%s" % mobile,SMS_CODE_EXPIRES_SECONDS,sms_code)
		except Exception as e:
			logging.error(e)
			return self.write(dict(errno=RET.DBERR,errmsg="生成短信验证码错误"))
		try:
			ccp.sendTemplateSMS(mobile,[sms_code,constants.SMS_CODE_EXPIRES_SECONDS],1)
		except Exception as e:
			logging.error(e)
			return self.write(dict(errno=RET.THIRDERR,errmsg="发送失败!"))
		self.write(dict(errno=RET.OK),errmsg="OK")



