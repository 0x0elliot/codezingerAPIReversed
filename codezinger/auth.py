from requests import Session
from . import config, URL

class Auth:
    URL = URL
    def __init__(self):
        self.email = config.EMAIL
        self.password = config.PASSWORD
        self.session = Session()

    def login(self):
        login_endpoint = self.URL + "/auth/login"
        body = dict(
            username=self.email,
            password=self.password,
            rememberMe=True,
            forcedLogin=True,
            login_device_data=dict(
                os="Windows",
                browser="Chrome",
                brwoserVersion="99.0.4844.84"
            )
        )
        r = self.session.post(
            login_endpoint,
            data=body
        )

        if r.status_code == 406:
            print(r.json())
            raise Exception("Invalid credentials.")

        return r.json()