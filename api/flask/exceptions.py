class FlaskApiException(Exception):
	pass

class RecordNotExistException(FlaskApiException):
	pass