class _CCP(object):
	"""docstring for _CCP"""
	def __init__(self):
		self.rest = REST(_serverIP,_serverPort,_softVersion)
		self.rest.setAccount(_accountSid,_accountToken)
		self.rest.setAppId(_appId)
	@classmethod
	def instance(cls):
		if not hasattr(cls,"_instance"):
			cls._instance = cls()
		return cls._instance
	def sendTemplateSMS(self,to,datas,tempId):
		return self.rest.sendTemplateSMS(to,datas,tempId)
ccp = _CCP.instance()

if __name__ == '__main__':
	ccp.sendTemplateSMS("17759615754",['12345',5],1)

class CCP(object):
	"""docstring for CCP"""
	def __init__(self, arg):
		super(CCP, self).__init__()
		self.arg = arg
		
		