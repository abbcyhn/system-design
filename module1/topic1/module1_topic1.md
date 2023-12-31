# Different Tiers in Software Architecture

## Educative Questions

* What is a tier?

	* A tier is the logical and physical separation of components in an application or a service. The components are the database, backend application server, user interface, messaging, and caching.

* When should we choose a single tier architecture for our application?

	* When we do not want any network latency.

* Which of the following are the correct reasons to choose a two-tier architecture for our application?

	* When we need to minimize the network latency.
	* When we need control over data in our application.

* Which of the following are correct reasons to choose a three-tier architecture for our application?

	* When we need control over the code/business logic of our application and want it to be secure.
	* When we need control over data in our application.

* Why do software applications have different tiers? Which of the following option(s) are correct?

	* To assign dedicated roles/tasks to different components for a loosely coupled architecture.
	* To make the management, maintenance of the system and the introduction of new features in the application easier.

* Do layers and tiers in an application have the same meaning?

	* No!! Tiers and layers in software architecture have different meanings and cannot be used interchangeably.

## Person1 Questions

* What are Single Responsibility Principle and Separation Of Concerns?
	* Single responsibility principle - means that giving one dedicated responsibility to a component and letting it execute flawlessly.
	* Separation of Concerns - means that keeping components seperate. So, they can be reusable.

* N-tier application is fault tolerance? 
	
	* N-tier application architecture is not inherently fault-tolerant, but it can be designed to achieve fault tolerance depending on how it is implemented.

* How to achieve fault tolerance in an N-tier application?
	
	To achieve fault tolerance in an N-tier application, redundancy and fault-tolerant mechanisms need to be implemented at various levels. Here are a few approaches to make an N-tier application more fault-tolerant:
	* Load balancing: Distributing incoming network traffic across multiple servers helps ensure that no single server is overwhelmed. Load balancers monitor the health of servers and can redirect traffic away from failed or overloaded servers to functioning ones.
	* Redundancy: Implementing redundancy at different tiers helps mitigate the impact of failures. This can involve replicating servers or components and ensuring that backups are available to take over in case of failure.
	* Failover mechanisms: Implementing failover mechanisms allows for seamless transitioning to backup systems or components when failures occur. This ensures continuous availability of the application.
	* Monitoring and fault detection: Implementing monitoring systems to detect faults or failures in the application is crucial. By actively monitoring the health of servers, networks, and components, potential issues can be identified early and appropriate actions can be taken to mitigate them.
	* Graceful degradation: Designing the application to gracefully degrade functionality when certain components or services become unavailable can enhance fault tolerance. It allows the application to continue operating with reduced functionality rather than completely failing.

* Monolithic/MicroServices architecture and 2 tier/3 tier/N tier architectures are different concepts?
	* Yes, while monolithic and microservices architectures primarily pertain to the code-level organization and deployment of an application, 2-tier, 3-tier, and N-tier architectures are higher-level architectural patterns that focus on the overall structure and organization of the application's components and layers.

* When two-tier applications are usefull?
	* Small-scale applications: Two-tier architecture is suitable for small-scale applications with a limited number of users and straightforward business logic. Since there are only two layers—the client layer and the server layer—it simplifies the development and maintenance process.
	* Low network latency: Two-tier applications are advantageous when the client and server are located in close proximity with low network latency. This reduces the time required for data transfer between the client and the server, resulting in faster response times.
	* Limited resources: In environments with limited resources, such as embedded systems or low-powered devices, a two-tier architecture can be employed to optimize resource utilization. The absence of an intermediate layer reduces the computational overhead on the client-side.
	* Single-user applications: When the application is designed to be used by a single user at a time, a two-tier architecture can be suitable. For example, a desktop application that operates on a local database without the need for concurrent access by multiple users can be implemented as a two-tier application.
	* Rapid development: Two-tier architectures are often chosen for rapid application development. The simplicity of the architecture allows developers to focus on core functionality without the added complexity of a multi-tiered infrastructure.

## Person2 Questions
* What is the difference between a layer and a tier?
	* A layer is a logical separation of components in an application. A tier is a physical separation of components in an application.

* What is disadvantages of N-tier architecture?
	* Increased complexity: The complexity of an N-tier architecture is higher than that of a two-tier or three-tier architecture. This can make the development and maintenance process more challenging.
	* Increased latency: Since the application is distributed across multiple servers, the latency is higher than that of a two-tier or three-tier architecture. This can result in slower response times.
	* Increased cost: The cost of implementing and maintaining an N-tier architecture is higher than that of a two-tier or three-tier architecture. This is due to the increased number of servers and components involved.
	* Increased security risks: The increased number of servers and components in an N-tier architecture can increase the security risks. This is because each component is a potential point of failure and can be exploited by malicious actors.