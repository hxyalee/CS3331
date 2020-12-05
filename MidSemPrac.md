1. Assume that 10 clients (each running on a separate machine) are simultaneously communicating with a web server using HTTP1.1 and requesting 5 objects each (do not consider a separate index page). Assume that the web server has sufficient resources to service all received requests simultaneously. How many sockets are simultaneously open on each client machine and on the web server? Provide a short explanation.
* Since HTTP 1.1 is used, (persistence with pipelining), all objects will be requested and transmitted over a single TCP connection between each client and the server. Thus, each client will have one TCP socket open. <br/> The server will have 10 clients open simultaneously. Thus, the server will have 10 socekts open, 1 socket to communicate with each socket. In total, there will be 11 socekts open at the server.

2. Assume that 10 clients (each running on a separate machine) are simultaneously communicating with a web server using HTTP1.1 and requesting 5 objects each (do not consider a separate index page). Assume that the web server has sufficient resources to service all received requests simultaneously. How many sockets are simultaneously open on each client machine and on the web server? Provide a short explanation.
* Since HTTP 1.0 is used (non-persistent), each object will be requested and transmitted over a distinct TCP connection between each client and server. Hence, each client will have five TCP sockets open. <br/> The server will have 50 sockets open simultaneously (5 x 10). In addition, the server will have a welcome socket open. Hence, there will be 51 sockets open at the server.

3. Why isn’t SMTP used by a user agent to retrieve e-mail from the mail server?  What is typically used instead?
* SMTP is a push protocol, whereas receiving email requires *pull* semantics. IMAP, POP, and HTTP are typically used for a client to retrieve e-mail.

4. Suppose every link in the network carries two classes of traffic – voice over IP calls and e-mail messages, with a separate queue for each class.  When deciding which packet to send next, the router first selects the head of the queue containing the voice traffic, and only sends an e-mail packet if the voice queue is empty.  Does the e-mail traffic have any effect on the performance experienced by the voice calls?  If so, what can be done to minimize the effects?
* Yes, the email traffic can still have an effect. If no VoIP packets are present, the router starts transmitting an email packet. A VoIP packet that arrives while the email packet is in flight must wait for the ongoing transmission to complete, introducing delay related to the size of the email packet. Limiting the maximum size of packets can help reduce the effect.

5. Given *m* packets, *n* hops, *p* processing delay, *0* queueing delay, *t* transmission delay, and *pa* propagation delay, how long will it take for the server to receive all packets?
* (m - 1)(p + t) + n * (p + t + pa)

6. Advantages and disadvantages of using a text-based header instead of binary format
* Advantage: Readability for human
* Disadvantage: Consumes more space, and hence decreases efficiency

7. Reasons on why CDNs have been more widely deployed than Web Caching
* Web cache cannot cache dynamic contents like movies and games
* You cannot require the users to build a cache server for you. Only ISPs can create web cache server. Hence, CDNs are more scalable


8. Suppose that a sender and receiver are connected via a point-to-point link that has 1 Mbps bandwidth and a one-way propagation delay of 4.5 ms. Assume that the sender always has data for transmission and that the size of each data packet is 125 Bytes. Neglect any headers. Also, assume that the size of Ack packets is negligible. Answer each of the following for both go-back-n and selective-repeat sliding window schemes.
	1. Assuming that the link is error-free, what should be the size of the window (in terms of the number of packets) to achieve a throughput of 0.8 Mbps.
	* The time to transmit one data packet, T = 125 x 8 bits /1Mbps = 1ms

	* RTT = 2 x one-way propagation delay = 9ms

	* As discussed in the lecture slides on this topic, the utilization of the link when a sliding window protocol with window size N, is given by,

	* U = NT/(T + RTT)

	* Achieving a throughput of 0.8Mbps on a 1Mbps link implies that the utilisation should 0.8.

	* Thus, 0.8 = N x 1ms /1ms + 9ms. This results in N = 8 packets. 
	2. What is the minimum number of bits needed to represent the sequence numbers corresponding to the above window size? Recall that an n bit sequence number results in a range of sequence numbers from 0 to 2<sup>n-1</sup>.
	* Go-back-N:

		* To achieve a window size of 8 with GBN, we will need 9 unique sequence numbers (1 more than the window size). Thus, it is necessary to have a 4-bit sequence number space in GBN.

	* Selective repeat:

		* As was discussed in the lecture notes, with SR, the window size must be less than or equal to half the size of the sequence number space. Thus, in order to accommodate a window size of 8, we need at least 16 unique numbers, which implies that SR would require a 4-bit sequence number space.