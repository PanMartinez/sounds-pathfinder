from starlette import status


ERROR_CODES = {
    "AUTH_ERROR": "AUTH_ERROR",
}


class ErrorBase(Exception):
    status_code: status = ""
    error_code: ERROR_CODES = ""

    def __str__(self):
        return f"{self.status_code}: {self.error_code}"
