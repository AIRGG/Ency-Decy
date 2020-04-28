import os, random
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken

class EncyDecy(object):
	"""docstring for EncyDecy"""
	def __init__(self, mypass):
		password = bytes(mypass.encode())
		salt = b'^%$#ASIN@SALTNYA%^*}<?!?^%!|'
		# salt = b'\xb4-\xe8L8\xbe\xaa\xfc\x04\xac\xec\x1b\xb0\xd2\xa6\xc2\xf8xc0\x00\xc4\xc1^\x08<\xbb\xba=\xfb\xf7_\x7fy{n[\xc64p\xf8\x11\xfe\xf1\xd3\x07\xee5\xa9Vf\xd9\x95\xe8^TZ\x92N\x7f\x81"\xe1\x19'
		kdf = PBKDF2HMAC(
		    algorithm=hashes.SHA256(),
		    length=32,
		    salt=salt,
		    iterations=100,
		    backend=default_backend()
		)
		key = base64.urlsafe_b64encode(kdf.derive(password))
		f = Fernet(key)
		self.fernet = f
		self.tmpname = "rahasia"
	
	def ency(self, message):
		return self.fernet.encrypt(message.encode())
		pass

	def decy(self, encymsg):
		try:
			return self.fernet.decrypt(encymsg.encode())
		except Exception as e:
			print(e, "apa")
			return False
		# except InvalidToken as e:
		# 	return False
		pass

	def encyFile(self, pathToFile):
		try:
			with open(pathToFile, 'rb') as f:
				data = f.read()
			encrypted = self.fernet.encrypt(data)
			out = "{}.{}".format(os.path.basename(pathToFile), self.tmpname)
			with open(out, 'wb') as f:
				f.write(encrypted)
		except Exception as e:
			return False
		pass

	def decyFile(self, pathToFile):
		try:
			with open(pathToFile, 'rb') as f:
				data = f.read()
			decrypted = self.fernet.decrypt(data)
			out = pathToFile.split(".{}".format(pathToFile.split(".")[-1]))[0]
			with open(out, 'wb') as f:
				f.write(decrypted)
		except Exception as e:
			return False