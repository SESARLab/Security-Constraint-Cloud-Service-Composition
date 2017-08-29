# Probability Constraints - “Authorization-Based Privacy”


* **Goal.** The goal of the certification process is to check that every access to eHealth satisfies the defined RBAC (role-based access control) policies. Also, it aims to verify that the BG scenario is not abused by checking probability constraints.
* **Scenario.** eHealth users (e.g., nurses, doctors) request access to resources for which they are authorized (possibly in a BG scenario). Access requests are collected in a log for a predefined window of time.
* **ToC.** It consists of the eHealth application and insists on guest domain in Figure 9.4 It mainly focuses on the flow described in Example 3.3.



## Execution:

```
$ pip install -r requirements.txt
$ cat test.json|python entrypoint.py```

### Output Example


```output:```