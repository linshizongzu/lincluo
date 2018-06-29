#coding:utf-8

from qiniu import Auth,put_file,etag,urlsafe_base64_encode
import qiniu.config

access_key = ''
secret_key = ''

q = Auth(access_key,secret_key)

bucket_name = 'linshi'

token = q.upload_token(bucket_name,None,3600)

localfile = './sync/bbc.jpg'

ret,info = put_file(token,None,localfile)
print(info)
assert ret['key'] == key
assert ret['hash'] == etag(localfile)

def storage(image_data):


if __name__ == '__main__':
	file_name = raw_input("请输入文件名：")
	file = open(file_name,'rb')
	file_data = file.read()
	key = storage(file_data)
	print(key)
	file.close()










