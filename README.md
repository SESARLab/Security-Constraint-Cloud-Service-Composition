# Security-Constraint-Cloud-Service-Composition
Modeling Time, Probability, and Configuration Constraints for Continuous Cloud Service Certification M. Anisettic, C.A. Ardagnac, E. Damianib, N. El Ioinia, F. Gaudenzic
***
## Abstract 

Cloud computing proposes a paradigm shift where resources and services are allocated, provisioned, and accessed at runtime and on demand. New business opportunities emerge for service providers and their customers, at a price of an increased uncertainty on how their data are managed and their applications operate once stored/deployed in the cloud. This scenario calls for assurance solutions that formally assess the working of the cloud and its services/pro- cesses. Current assurance techniques increasingly rely on model-based verifica- tion, but fall short to provide sound checks on the validity and correctness of their assessment over time. The approach in this paper aims to close this gap catching unexpected behaviors emerging when a verified service is deployed in the target cloud. We focus on certification-based assurance techniques, which provide customers with verifiable and formal evidence on the behavior of cloud services/processes. We present a trustworthy cloud certification scheme based on the continuous verification of model correctness against real and synthetic service execution traces, according to time, probability, and configuration con- straints, and attack flows. We test the effectiveness of our approach in a real scenario involving ATOS SA eHealth application deployed on top of open source IaaS OpenStack.
***
#### Model Generator
Model generator is available [here](https://github.com/SESARLab/Security-Constraint-Cloud-Service-Composition/tree/master/FSModel) and provides functionalities for i) generating random models and ii) perturbing random models at various degrees (e.g., add new paths, remove existing paths)


#### Property:
1. [Time Constraints - “Access Performance”](https://github.com/SESARLab/Security-Constraint-Cloud-Service-Composition/tree/master/time%20constraints)
2. [Probability Constraints - “Authorization-Based Privacy”](https://github.com/SESARLab/Security-Constraint-Cloud-Service-Composition/tree/master/probability%20constraints)
3. [Configuration Constraints - “Storage Confidentiality”](https://github.com/SESARLab/Security-Constraint-Cloud-Service-Composition/tree/master/configuration%20constraints)
