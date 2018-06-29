#coding:utf-8
import os
# Application配置参数
settings = {
	"static_path":os.path.join(os.path.dirname(__file__),"static"),
	"template":os.path.join(os.path.dirname(__file__),"template"),
	"cookid_seceret":"xGAJJnjBQcmE4iGaInaTm0IlAXBZkUHkp3+bzldmlc4=",
	"xsrf_cookies":True,
	"debug":True,
	
}


# mysql
mysql_options = dict(
	host = "127.0.0.1",
	database = "cluo",
	user = "root",
	password = "linshi",


)

SESSION_EXPIRES_SECONDS = 86400 #session数据有效期,秒
#redis
redis_options = dic(
	host = "127.0.0.1",
	port = 6379
)
log_file = os.path.join(os.path.dirname(__file__),"logs/log")
log_level = "debug"

session_expires_seconds = 86400
passwd_hash_key = "linshi@$^*" #密码加密salt

image_url_prefix = "http://linzhiying.bkt.clouddn.com/" #7牛图片的域名



