#coding:utf-8

from utils.response_code import RET

def require_logined(fun):
	@functools.wraps(fun)
	def wrapper(request_handler_obj,*args,**kwargs):
		if  request_handler_obj.get_current_user():
			fun(request_handler_obj,*args,**kwargs)
		else:
			request_handler_obj.write(dict=(errno=
				RET.SESSIONERR,errmsg="用户未登陆"))
	return wrapper
