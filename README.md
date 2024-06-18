## Event driven autoscaling using Pod Identity and KEDA


Orchestration platforms like Amazon EKS have streamlined the process of building, securing, operating, and maintaining container-based applications, allowing organizations to focus on development. As customers increasingly adopt event-driven deployment, they can scale Kubernetes deployments based on various event sources. This approach, combined with autoscaling, can lead to significant cost savings by providing on-demand compute resources and efficient scaling based on application logic. Kubernetes supports cluster-level autoscaling with the Cluster Autoscaler and application-level autoscaling with the Horizontal Pod Autoscaler (HPA) and Vertical Pod Autoscaler (VPA), which scale pods based on CPU and memory usage. However, for complex scenarios like event-driven autoscaling, metrics related to application logic are crucial.

KEDA (Kubernetes-based Event Driven Autoscaler) enhances Kubernetes by enabling autoscaling based on events, such as custom metrics thresholds or messages in a message queue. KEDA is lightweight and integrates seamlessly with any Kubernetes cluster, working alongside standard components like the HPA. Additionally, AWS provides IAM Role for Service Accounts (IRSA) to support diverse Kubernetes deployment options, including Amazon EKS in the cloud, EKS Anywhere, Red Hat OpenShift Service on AWS (ROSA), and self-managed Kubernetes clusters on EC2. IRSA leverages AWS IAM constructs like OpenID Connect (OIDC) identity providers and IAM trust policies to ensure it operates across different environments without relying directly on EKS services or APIs.

Amazon EKS Pod Identity, introduced in November 2023 during AWS re:Invent, simplifies the process for Kubernetes service accounts to assume IAM roles without requiring OIDC providers. EKS Pod Identity also supports features not available in IRSA, such as IAM role session tags, which make permissions more intuitive and simplify access management for administrators. By implementing KEDA with pod identity in these environments, businesses can achieve efficient event-driven autoscaling, ensuring applications scale based on demand, optimizing resource utilization, and reducing costs. This solution demonstrates the integration of Pod Identity with Kubernetes Event Driven Architecture (KEDA), showcasing how the keda-operator service account and TriggerAuthentication can be utilized. It also details setting up a trust relationship between two IAM roles to enable KEDA's functionality for monitoring messages in the event queues and adjusting scaling for the destination Kubernetes objects.


# Target architecture

<p align="center">
  <img  src="https://github.com/aws-samples/event-driven-autoscaling-using-podidentity-and-keda/blob/main/img/keda-pod-identity.png?raw=true">
</p>


The key aspect of this architecture is the use of the EKS Pod Identity Addon to provide secure access to the SQS queue to the keda operator. The KEDA operator can then use the SQS queue metrics to automatically scale the application deployment as needed.This enables automatic scaling of the application based on the SQS queue metrics.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

## Contributors
- Dipen Desai
- Kamal Joshi
- Mahendra Revanasiddappa
- Abhay Diwan
