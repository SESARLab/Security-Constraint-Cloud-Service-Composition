from requests.auth import HTTPBasicAuth
from requests import request
import time
from driver import Driver

class RensponseTime(Driver):
    def login(self,inputs=None):
        #preprare Header for http basic authentication
        login_ti=self.testinstances.get("login", None)
        auth = HTTPBasicAuth(login_ti.get('user'), login_ti.get('password'))
        return auth
    def get_response(self, inputs=None):
        time_m=self.testinstances.get("responsive").get("threshold")
        auth=inputs
        start_time=time.time()
        request.get('https://aes.ehealth.local/access-private-data', auth=auth)
        response_time = time.time() - start_time
        if response_time <= time_m:
            return True
        else:
            return False
    def logout(self, inputs):
        return False
    def rollback(self, inputs):
        self.result.put_value("exception", "The probe exit because an exception")
        return False
    def appendAtomics(self):
        self.appendAtomic(self.login, self.logout)
        self.appendAtomic(self.get_response,self.rollback)

