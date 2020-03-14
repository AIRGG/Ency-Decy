import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken

class EncyDecy(object):
	"""docstring for EncyDecy"""
	def __init__(self, mypass):
		# self.mypass = mypass
		# mypass = self.mypass
		password = mypass.encode()
		salt = b'^%$#ASIN@SALTNYA%^*}<?!?^%!|'
		kdf = PBKDF2HMAC(
		    algorithm=hashes.SHA256(),
		    length=32,
		    salt=salt,
		    iterations=100000,
		    backend=default_backend()
		)
		key = base64.urlsafe_b64encode(kdf.derive(password))
		f = Fernet(key)
		self.fernet = f
	
	def ency(self, message):
		return self.fernet.encrypt(message.encode())
		pass

	def decy(self, encymsg):
		try:
			return self.fernet.decrypt(encymsg.encode())
		except Exception as e:
			return False
		# except InvalidToken as e:
		# 	return False
		pass