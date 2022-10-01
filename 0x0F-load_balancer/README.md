# Load Balancing.
A load balancer acts as the “traffic cop” sitting in front of your servers and routing client requests across all servers capable of fulfilling those requests in a manner that maximizes speed and capacity utilization and ensures that no one server is overworked, which could degrade performance. If a single server goes down, the load balancer redirects traffic to the remaining online servers. When a new server is added to the server group, the load balancer automatically starts to send requests to it.
![image](https://user-images.githubusercontent.com/99282239/193420527-72533575-8f9f-4852-bc03-ffa3b81a9a13.png)

## Common Load Balancing methods/algorithms
- Round Robin
- Least Connection
- Least Time
