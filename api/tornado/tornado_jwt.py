# import jwt
#json web token crsf xss
#header + payload +sercet

# sercet_key = ''
# options = 

'''
---------------
header
---------------
alg 加密格式
typ 类型

---------------
payload
---------------
iss 签发者
sub 面向的用户
aud 接收jwt的另一方
exp jwt过期时间
nbf 定义在什么时间之前
iat 签发时间
jti 唯一身份标识

---------------
secret
---------------

'''
from itsdangerous import BadTimeSignature, SignatureExpired
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
 
APP_SECRET_KEY="secret"
MAX_TOKEN_AGE=1800
token_generator = Serializer(APP_SECRET_KEY, expires_in=MAX_TOKEN_AGE)
 
def generate_auth_token(userid):
  access_token = token_generator.dumps({"userid":userid})
  return access_token


def get_identity(access_token):
	token = token_generator.loads(access_token)
	return token['userid']


def verify_token(token):
  try:
    user_auth = token_generator.loads(token)
  except SignatureExpired as e:
    raise e
  except BadTimeSignature as e:
    raise e
  return user_auth


if __name__=='__main__':
	c=generate_auth_token(12)
	print(c)
	print(get_identity(c))
	print(verify_token(c))


