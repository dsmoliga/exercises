class Result:
    def __init__(self, message, value=0):
        self.is_success = None
        self.message = message
        self.value = value

    def is_ok(self):
        return self.is_success


class Ok(Result):
    def __init__(self, message, value=None):
        super().__init__(message, value)
        self.is_success = True


class Error(Result):
    def __init__(self, message, value=None):
        super().__init__(message, value)
        self.is_success = False
