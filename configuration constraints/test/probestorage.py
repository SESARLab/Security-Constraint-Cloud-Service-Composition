from keystoneauth1 import loading
from keystoneauth1 import session
from cinderclient import client
from driver import Driver

class StorageProbe(Driver):
    def authentication(self,inputs=None):
        loader = loading.get_plugin_loader('password')
        auth = loader.load_from_options(
            auth_url=self.testinstances["openstack credential"]["OS_AUTH_URL"],
            username=self.testinstances["openstack credential"]["OS_USERNAME"],
            password=self.testinstances["openstack credential"]["OS_PASSWORD"],
            project_id=self.testinstances["openstack credential"]["OS_PROJECT_ID"],
            user_domain_name=self.testinstances["openstack credential"]["OS_USER_DOMAIN_NAME"]
        )
        sess = session.Session(auth=auth)
        return sess
    def check_volumes(self, inputs=None):
        encrypted_type=self.testinstances.get("volumes").get("encrypted type")
        volumes_ti=self.testinstances.get("volumes").get("list")
        volumes=volumes_ti.split(',')
        sess=inputs
        cinder = client.Client('2', session=sess)
        volume_list = cinder.volumes.list()
        for v in volume_list:
            if v.name in volumes:
                if v.types != encrypted_type:
                    return False
    def rollback(self, inputs):
        self.result.put_value("exception", "The probe exit because an exception")
        return False
    def appendAtomics(self):
        self.appendAtomic(self.authentication, self.rollback)
        self.appendAtomic(self.check_volumes,self.rollback)

