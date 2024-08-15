from starlette import status

from soundfinder.exceptions.common import ErrorBase, ERROR_CODES


class AuthError(ErrorBase):
    def __init__(self):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.error_code = ERROR_CODES["AUTH_ERROR"]
        self.headers = ({"WWW-Authenticate": "Bearer"},)


auth_error = AuthError()
