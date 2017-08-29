# Time Constraints - “Access Performance”


* **Goal.** The goal of the certification process is to check whether the response time of function access(private_data) is under a given threshold mi (mi=500ms in our example). Time is measured from outside the application as a nurse or a doctor interacts with the application.
* **Scenario.** A user logs into the eHealth application during an emergency situ- ation and requires private data of a patience not under her control.
* **ToC.** It consists of the eHealth application with particular focus on function ac- cess(private_data). It insists on guest and data domains in Figure 9. In fact, to access data, the system uses the whole architecture: the request passes through the EAS, accesses the DS, and has an impact on the whole infrastructure, using storage, network and computational power.


## Execution:

```cat test.json|python entrypoint.py```

### Output Example


```output:```