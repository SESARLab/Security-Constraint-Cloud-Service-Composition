import paramiko
from userManager import users,us
from driver import Driver



class SSHClient(object):
    def ssh_connect(self, hostname, port, username, password=None, private_key=None, private_key_passphrase=None):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if private_key:
            private_key = paramiko.RSAKey.from_private_key(private_key, password=private_key_passphrase)
        ssh_client.connect(hostname, port, username=username, password=password, pkey=private_key)
        return ssh_client

class EmptyDriver(Driver,SSHClient):
    def ssh_connection(self,inputs=None):
        ssh_connection_ti = self.testinstances.get("connect_to_server", None)
        assert not ssh_connection_ti is None

        hostname = ssh_connection_ti.get("hostname")
        port = ssh_connection_ti.get("port")
        username = ssh_connection_ti.get("username")
        password = ssh_connection_ti.get("password", None)
        assert not password is None

        self.ssh_connection = self.ssh_connect(
            hostname=hostname,
            username=username,
            port=port,
            password=password
        )
        return True


    def log_connection(self, inputs=None):
        logs_ti = self.testinstances.get("logs", None)
        _stdin, _stdout, _stderr = self.ssh_connection.exec_command("cat "+logs_ti.get("log_path"))
        out = _stdout.readlines()
        return out

    def log_analysis(self,inputs=None):

        model = [
            {"sequence": ["login(cred)", "log(failure)"], "p": 0.05, "count": 0, "flow":0},
            {"sequence": ["login(cred)", "log(success)", "*"], "p": 0.95, "count": 0,"flow":0},
            {"sequence": ["login(cred)", "log(success)", "assign_role(doctor/nurse)", "access(public_data)", "*"],
             "p": 0.98, "count": 0,"flow":1},
            {"sequence": ["login(cred)", "log(success)", "assign_role(doctor/nurse)", "access(private_data)", "*"],
             "p": 0.02, "count": 0,"flow":1}

        ]

        #cambiare lettura log out
        #leggere out
        myfile=inputs.split("\n")
        for line in myfile:
            for u in us:
                if u in line:
                    users[u].append({"line": line, "operation": line.split(" ")[3]})
        total_seq = 0
        for u in us:
            matcher = None
            for line in users[u]:
                if line["operation"] == "login(cred)":
                    print("....")
                    total_seq += 1
                    if matcher is not None:
                        for m in range(0, len(matcher)):
                            if matcher[m] is not None:
                                model[m]["count"] += 1
                    matcher = [0, 0, 0, 0]
                for s in range(0, len(model)):
                    if matcher[s] is not None and (
                                matcher[s] >= len(model[s]["sequence"]) or model[s]["sequence"][matcher[s]] == "*" or
                            line["operation"] == model[s]["sequence"][matcher[s]]):
                        matcher[s] += 1
                    else:
                        matcher[s] = None
            if matcher is not None:
                for m in range(0, len(matcher)):
                    if matcher[m] is not None:
                        model[m]["count"] += 1
        frequency=[0]*model[len(model)-1]["flow"]
        for m in model:
            frequency[m["flow"]]+=m["count"]
        for m in model:
            if m["p"] > (m["count"]/frequency[m["flow"]]):
                result=False
        return result

    def close_ssh_connection(self, inputs):
        try:
            self.ssh_connection.close()
        except:
            pass
        return inputs

    def rollback(self, inputs):
        self.result.put_value("exception", "The probe exit because an exception")
        return False
    def appendAtomics(self):
        self.appendAtomic(self.ssh_connect, self.close_ssh_connection)
        self.appendAtomic(self.log_connection,self.rollback)
        self.appendAtomic(self.log_analysis,self.rollback)
        self.appendAtomic(self.close_ssh_connection,self.rollback)

