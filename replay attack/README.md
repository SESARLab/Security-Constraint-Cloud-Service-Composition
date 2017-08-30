# Configuration Constraints - “Storage Confidentiality”


* **Goal.** The goal of the certification process is to check if stored data are managed in a secure way, making eHealth robust against unauthorized access to sensitive information. To address this requirement eHealth secured the virtual storage by using infrastructure-layer encryption mechanisms.
* **Scenario.** The eHealth application requires an encrypted storage to store its information before being attached to VMs (e.g., at deployment time, while scal- ing, or for load balancing). Cinder manages the persistent storage, and Nova provides an encryption mechanism and features to attach it to VMs. Cinder and Nova use an encryption function based on Dm-Crypt (Benjamin et al. (2013)), which prevents unauthorized access to sensitive information creating a Linux Unified Key Setup (LUKS) storage.
* **ToC.** It includes Nova and Cinder services, and insists on security domains data and management in Figure 9.

## Execution:

```
$ pip install -r requirements.txt
$ cat test.json|python entrypoint.py
```