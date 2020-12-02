# Introduction to Computer Networks
* What is the internet? *Nuts and Bolts view*
	* Millions of connected computing devices
		* *hosts* = *end systems*
		* running *network apps*
	* *Communication links*
		* Fiber, copper, radio, satellite
		* Transmission rate: *bandwidth*
	* *Packet switches*: forward packets (chunks of data)
		* *routers* and link-layer *slink layer switches*
	* Internet: *Network of networks*
		* Interconnected ISPs
	* *Protocols* control sending, receiving or messages
		* TCP, IP, HTTP, Skype, 802.11
	* Internet standards
		* RFC: Request For Comments
		* IETF: Internet Engineering Task Force
* Whats the internet? *A Service view*
	* Infrastructure that provides services to application	
		* Web, VoIP, email, games, e-commerce, social network, etc
	* Provides programming interface to apps	
		* Hooks that allow sending and receiving app programs to *connect* to internet
		* Provides service options, analogous to postal service
* Whats a protocol?
	* Define *format, order of messages sent and recieved* among network entities, and *actions taken* on message transmission, receipt
	* TCP connection requested → TCP connection response  <br /> GET Request <Some URL> → <Response>

* A closer look at network structure
	* *Network edge*
		* Hosts: Clients and servers
		* Servers are often in data centers
	* *Access networks and physical media*: Wired, wireless communication links
	* *Network core*:
		* Interconnected routers
		* Network of networks

* Access networks and physical media
	* How to connect end systems to edge router?
		* Residential access nets
		* Institutional access networks (School, Company)
		* Mobile access networks
	> Keep in mind: Bandwidth (bits per second) of access network? Shared or dedicated?


* Access net: digital subscriber line (DSL)
	* Use existing telephone line to center office DSLAM
		* Data over DSL phone lines goes to internet
		* Voice over DSL phone line goes to telephone net
	* High-pass filter for data
	* Low-pass filter for voice
	* ADSL over POTS
		* Voice, data transmitted at different frequencies over *dedicated* line to central office
	* Different data rates for upload and download (ADSL)
	* Distance from DSLAM matters 

* Access net: cable network
	* *Frequency division multiplexing*	
		* Different channels transmitted in different frequency bands
	* HFC: Hybrid Fiber Coax
		* Asymmetric: up to 30Mbps downstream transmission rate; 2Mbps upstream transmission rate
	* Network of cable, fiber attaches homes to ISP router
		* Homes *share access network* to cable headend
		* Unlike DSL, which has dedicated access to central office

* Fiber to the home/premise/curb
	* Fully optical fiber path all the way to the home (or premise or curb)
		* NBN, Google, Verizon FIOS
		* \~30Mbps to 1Gbps
* Enterprise Access Networks (Ethernet)
	* Typically used in companies, universities, etc
	* 10Mbps, 100 Mbps, 1Gbps, 10Gbps transmission rates
	* Today, end systems typically connect to ethernet switch
* Wireless Access Network
	* Shared wireless access network connects end system to router
		* Via base station aka *access point*
	* Wireless LANs:
		* Within building (100ft)
		* 802.11 b/g/n (WiFi)
		* 802.11 ac
	* Wide-area wireless access
		* Proviced by telco (cellular) operator; 10s km
		* Between 10 and 100 Mbps
		* 4G, 5G
* Physical media
	* Bit
		* Propagates between transmitter/receiver pairs
	* Physical link
		* What lies between transmitter and receiver
	* Guided media
		* Signals propagate in solid media: copper, fiber, coax
	* Unguided media
		* Signals propagate freely; e.g. radio
	
	* Twisted pair (TP)
		* Two insulated copper wires
	* Coaxial cable
		* Two concentric copper condictors
		* Broadband:
			* Multiple channels on cable
			* HFC
	* Fiber Optic Cable
		* Glass fiber carrying light pulses, each pulse a bit
		* High speed operation
			* High-speed point-to-point transmission
		* Low error rate:
			* Repeaters spaced far apart 
			* Immune to electromagnetic noises
	* Radio
		* Signal carried in electromagnetic spectrum
		* Propagation environment effects
			* Reflection
			* Obstruction by objects
			* Interference
		* *Radio link types*
			* Terrestrial microwave
			* LAN (e.g. WiFi)
			* Wide-area (e.g. cellular)
			* Satellite


* The network core
	* Mesh of interconnected routers/switches
	* Two forms of switched networks
		* Circuit switching: used in the legacy telephone networks
			* End to end resourfces allocated tom reserved for *call* between source and destination
			* Dedicated resources: no sharing
				* Circuit like (guaranteed) performance
			* Circuit segment idle if not used by call (no sharing)
			* Commonly used in traditional telephone networks
			* Why is it not feasible?
				* Inefficient
					* Computer communications tends to be very bursty. For example, viewing a sequence of web pages
					* Dedicated circuit cannot be used or shared in periods of silence
					* Cannot adopt to network dynamics
				* Fixed data rate
					* Computers communicate at very diverse rates. For example, viewing a video vs using telnet for web browsing
					* Fixed data rate is not useful
				* Connection state maintenance
					* Requires per communication state to maintained that is a considerable overhead
					* Not scalable
		* Packet switching: used in the internet
			* Data is sent as chunks of formatted bits (Packets)
			* Packets consist of *header* and *payload*
				* Payload is the data being carried
				* Header holds instructions to the network for how to handle packet (think of the header as an API)
				* Switches *forward* packets based on their headers
				* Each packets travel independently
					* No notion of packets belonging to a *circuit*
				* No link resources are reserved in advance. Instead, packet switching leverages **statistical multiplexing**
					* Statistical multuplexing relies on the assumption that not all flows burst at the same time
					* Use queue on transient overload
					* Can't really do anything on persistent overload; will eventually drop packets
			> Time to process the packet at the switch is relatively negligible
			> Cut through switching -- transmitting as soon as the packet processes the header
			* We will always assume a switch processes/forwards a packet after it has received it entirely
				* **Store and forward** switching

	* Packet switching vs Circuit switching
		* Packet switching allows more users to use network
			* example:
				* 1Mb/s link
				* Each user: 
					* 100kb/s when *active*
					* active 10% of time
				* Circuit switching
					* 10 users
				* Packet switching
					* With 35 users, probability > 10 active users at the same time is less than 0.0004
		* Is packet switching a *slam dunk winner*?
			* Great for bursty data
				* Resource sharing
				* Simpler, no call setup
			* Excessive congestion possible: Packet delay and loss
				* Protocols needed for reliable data transfer, congestion control
			> How to provide circuit like behaviour?
				> Bandwidth guarantees needed for audio/video apps
				> Still an unsolved problem

* Internet structure: network of networks
	* End systems connect to internet via *access ISPs* (Internet service providers)
		* Residential, company, and university ISPs
	* Access ISPs in turn must be interconnected
		* So that any two hosts can send packets to each other
	* Resulting network of networks is very complex
		* Evolution was driven by *economics* and *national policies*
	> Connecting each access ISPs to each other directly doesn't scale; O(n<sup>2</sup>) connections;

* How do loss and delay occur?
	* Packets *queue* in router buffers
		* Packet arribal rate to link (temporarily) exceeds output link capacity
		* Packets queue, wait for turn
* Four sources of packet delay
	* Nodal processing
		* Check bit errors
		* Determine output link
		* typically < msec
	* Queueing delay
		* Time waiting at output link for transmission
		* Depends on congestion levels of router
		* Packet arrival rate = a packets/sec
		* Packet length = L bits
		* Link bandwidth = R bits/sec
		* Every second, aL buts arrive to queue
		* Every second, R bits leave the router
		* if aL > R, queue will fill up and packets will get dropped
	* Transmission delay
		* L: packet length (bits)
		* R: Link bandwidth (bps)
		* d<sub>trans</sub> = L/R
	* Propagation delay
		* d: length of physical link
		* s: propagation speed in medium (\~2 x 10<sup>8</sup> m/sec)
		* d<sub>prop</sub>=d/s
	* **Add them all to get the total delay**
* *Real* Internet delays and routes
	* *Traceroute:* Provides delay measurement from source to router along end to end internet path towards destination. For all *i*:
		* Sends three packets that will reach router *i* on path towards destination
		* Router *i* will run packets to sender
		* Sender times interval between transmission and reply

* Throughput
	* Rate (bits/time unit) at which bits transferred betweem sender/receiver
		* Instantaneous -- rate at given point of time
		* Average -- rate over long period of time
		> bottleneck link -- link on end to end patj tjat constrains end to end throughput

* Tasks in networking
	* What does it take to send packet across?
		* Prepare data (Application)
		* Ensure that packet gets to destination process (Transport)
		* Deliver packets across global network (Network)
		* Delivery packets within local network to next hop (Datalink)
		* Bits/Packets on wire (Physical)

* Internet protocol stack
	* Application: supporting network applications
		* FTP, SMTP, HTTP, Skype
	* Transport: Process to process data transfer
		* TCP, UDP
	* Network: Routing of datagrams from source to destination
		* IP, routing protocols
	* Link: Data transfer between neighboring network elements
		* Ethernet, 802.11 (WiFi), PPP
	* Physical: buts *on the wire*
	> Each layer depends on layer below and supports the layer above. 
	> Each layer is independent of others
	> Multuple versions in layer: interfaces differ somewhat; components pick which lower-level protocol to use
	> But only one IP layer: unifying protocol

	> **NO layering: each new application has to be re-implemented for every network technology**

* Introducing an intermediate layer provides a *common* abstraction for various network technologies

* Is layering harmful?
	* Layer N may duplicate lower level functionality
		* E.g. Error recovery to retransmit lost data
	* Information hiding may hurt performance
		* E.g. Packet loss due to corruption vs congestion
	* Headers start to get really big
		* E.g. Typically TCP + IP + Ethernet headers add up to 54 bytes
	* Layer violations when the gains too greate to resist
		* E.g. NAT
	* Layer violations when network doesn't trust ends
		* E.g. Firewalls

* Distributing layers across netowrk
	* Layers are simple if only on a single machine
		* Just stack of modules interacting with those above/below
	* But we need to implement layers across machines
		* Hosts
			* Hosts have applications that generate data/messages that are eventually put out pon wire
			* At receiver host bits arrive on wire, mist make it up to application
		* Routers
			* Bits arrive on wire
				* Physical layer necessary
			* Packets must be delivered to next-hop
				* Datalink layer necessary
			* Routers participate in global delivery
				* Network layer necessary
			* Routers don't support reliable delivery
		* Switches
* Logical communication
	* Layers interacts with peer's corresponding layer
* Physical communication
	* Communication goes down to physical network
	* Then from network peer to peer
	* Then up to relevant layer


# Application Layer (Principles, Web, Email)
* Creating a network app
	* Run on different *end systems*
	* Communicate over netowrk
	* Network-core devices do not run user applications
	* Applications on end systems allows for rapid app development
* Interprocess Communication (IPC)
	* Processes talk to each other through interprocess communication
	* On single machine:
		* Shared memory
	* Across machines
		* We need other abstractions (Message passing)
* Sockets
	* Process sends/receives messages to/from its *sockets*
	* Socket analogous to door:
		* Sending process shoves message out the door
		* Sending process relies on transport infrastructure on other side of the door to deliver message to socket at receiving process
	* Application has a few options, OS handles the details
* Addressing processes
	* To receive messages, process must have an *identifier*
	* Host device has unique 32-bit IP address
	* Does IP address of host on which process runs suffice for identifying the process?
		* No, many processes can be running on the same host
	* Identifier includes both *IP Address* and *Port numbers* associated with process on host
		* E.g. HTTP server: 80; mail server: 25
* Client-server architecture
	* Server
		* Exports well-defined request/response interface
		* Long lived process that waits for requests
		* Upon receiving request, carries it out
		* Always on
		* Permanent IP Address
		* Static port conventions
		* Data centers for scaling
		* May communicate with other servers to respond
	* Clients
		* Short-lived process that makes requests
		* *User side* of application
		* Initiates the communication
		* May intermittently connected
		* May have dynamic IP addresses
		* Do not communicate directly with each other
* P2P architecture
	* No always on server
	* Arbitrary end systems (peers) directly communicate
	* Symmetric responsibility (unlike client/server)
	* Often used for
		* file sharing
		* games
		* blockchain / cryptocurrencies
		* general *distributed systems*
	* + Peers request service from other peers, provide service in return to other peers
		* *Self scalability -- new peers bring new service capacity, as well as new service demands*
	* + Speed -- Parallelism; less contention
	* + Reliability -- Redundancy; fault tolerance
	* + Geographic distribution
	* - State uncertainty -- no shared memory or clock
	* - Action uncertainty -- mutually conflicting decisions
	* - Distributed algorithms are complex

* App-layer protocol defines
	* Types of messages exchanged
		* e.g. request, response
	* Message syntax
		* What fields in messages and how fields are delineated
	* Message semantics
		* Meaning of information in fields
	* Rules for when and how processes send & respond to messages
	* Open protocols:
		* Defined in RFCs
		* Allows for interoperability
		* e.g. HTTP, SMTP
	* Proprietary prolotols:
		* e.g. Skype

* What transport service does an app need?
	* Data integrity
		* Some apps (file transfer, web transactions) require 100% reliable data transfer
		* Other apps (e.g. audio) can tolerate some loss
	* Timing
		* Some apps (internet telephony, interactive games) require low delay to be *effective*
	* Throughput
		* Some apps (multimedia) require minimum amount of throughput to be *effective*
		* Other apps (*elastic apps*) make use of whatever throughput whey get
	* Security
		* Encryption, data integrity
* Internet transport protocol services
	* TCP service
		* **Reliable transport** between sending and receiving process
		* **Flow control** -- sender won't overwhelm receiver
		* **Congestion control** -- throttle sender when network overloaded
		* **Does not provide** -- timing, minimum throughput guarantee, security
		* **Connection-oriented** -- Setup required between client and server processes
	* UDP Service
		* **Unreliable data transfer** between sending and receiving process
		* **Does not provide** reliability control, flow control, congestion control, timing, throughput guarantee, security, or connection setup
* Web and HTTP
	* Web page consists of *objects*
	* Object can be HTML file, JPEG image, JAVA applet, audio file, etc
	* Webpage consists of base HTML file which includes several referenced objects
	* Each object is addressable by a *URL*
* Uniform Resource Locator (URL)
	* protocol://host-name[:port]/directory-path/resource
		* protocol: http, ftp, smtp, https, etc
		* hostname: DNS name, IP address
		* port: defaults to protocol's standard port
		* directory path: hierarchical, reflecting file system
		* resource: indentifies the desired resource
* HTTP
	* Hypertext transfer protocol
	* Web's application layer protocol
	* Client-server model
		* Client: browser that requests, receives, and *displays* web objects
		* Server: web server sends objects in response to requests
	* Uses TCP:
		* Client initiates TCP connection  (creates socket) to server, port 80
		* Server accepts TCP connection from client
		* HTTP messages (application-layer protocol messages) exchanged between browser (HTTP Client) and web server (HTTP Server)
		* TCP connection closed
	* HTTP is *stateless*
		* Server maintains no information about past client requests
	> Protocols that maintain *state* are complex
		> Past history (state) must be maintained
		> If server/client crashes, their views of *state* may be inconsistent; must be reconciled

	* HTTP request message
		* Two types:
			* *request*
			* *response*
		* HTTP request message:	
			* ASCII (Human readable format)
	* HTTP is all text
		* Makes the protocol simple
			* Easy to delineate messages (\r\n)
			* Human readable
			* No issues about encoding or formatting data
			* Variable length data
		* Not the most efficient
			* Many protocols use binary fields
			* Headers my come in any order
			* Requires string parsing/processing
		* Non-text content needs to be encoded

* User-server state: Cookies
	* Four components
		* Cookie header line of HTTP response message
		* Cookie header line in next HTTP request message
		* Cookie file kept on user's host, managed by user's browser
		* Backend database at website
	* Cons of cookies
		* Cookies permit sites to learn alot about you
		* You may supply name and email to sites
		* 3rd party cookies can follow you across multiple sites

* Performance of HTTP
	* Most web pages have multiple objects
	* New TCP connection per (small) object
	* Page load time (PLT) as the metric
		* From click until user sees page
		* Key measure of web performance
	* Depends on many factors such as
		* Page content/structure
		* Protocols involved
		* Network bandwidth and RTT (round trip time)
	* Performance goals
		* User
			* Fast downloads
			* High availability
		* Content provider
			* Happy users
			* Cost effective infrastructure
		* Network
			* Avoid overload
	* How to improve page load time
		* Reduce content size for transfer
			* Small images; compression
		* Change HTTP to make better use of available bandwidth
			* Persistent connections and pipelining
		* Change HTTP to avoid repeated transfers of the same content
			* Caching and web-proxies
		* Move content closer to the client
			* CDNs
	* *Nonpersistent HTTP*: response time
		* RTT -- time for a small packet to travel from client to server and back
		* HTTP response time
			* One RTT initiate TCP connection
			* one RTT for HTTP request and first few bytes of HTTP response to return
			* File transmission time
			* Non persistent HTTP response time -- 2 RTT + File transmission time
	* HTTP/1.0
		* Non persistent -- one TCP connection tofetch one web resource
		* Fairly poor PLT
		* 2 Scenarios:
			* Multiple TCP connections setups to the *same server*
			* Sequential requests/responses even when resources are located on *different servers*
		* Multiple TCP slow-start phases
	* *Concurrent requests & responses*
		* Use multiple connections in parallel
		* Does not necessarily maintain order of responses
	* *Persistent HTTP*
		* Server leaves TCP connection open after sending response
		* Subsequent HTTP messages between same client/server are sent over the same TCP connection
		* Allow TCP to learn more accurate RTT estimate
		* ALlow TCP congestion window to increate
		* **Persistent without pipelining**
			* Client issues new request only when previous response has been received
			* One RTT for each referenced object
		* **Persistent with pipelining**
			* Introduced in HTTP/1.1
			* Client sends requests as soon as it encounters a referenced object
			* As little as one RTT for all referenced objects
	* Caching
		* Why does it work?
			* Exploits locality of reference
		* Where is it used?
			* Client
			* Forward proxies
			* Reverse Proxies
			* CDN
		* Web caches (Proxy server)
			* User sets browser: web accesses via cache
			* Browser sends all HTTP requests to cache
				* Object in cache: cache returns object
				* Else cache requests object from origin server, then returns the object to client
			* Why web caching?
				* Reduce response time for client request
				* Reduce traffic on an institution's access link
				* Internet dense with caches: enables *poor* content providers to effectively distribute content
		* Conditional GET
			* Dont send object if cache has up-to-date cached version
				* No object transmission delay
				* Lower link utilization
			* *Cache*: specify date of cached copy in HTTP request
			* *Server*: response contains no object if cached cached copy is up to date
	* Replication
		* Replicate popular website across many machines
			* Spread load on servers
			* Places content closer to clinets
			* Helps when content isnt cachable
		* Problem
			* Want to direct client to particular replica
				* Balance load across server replicas
				* Pair clients with nearby servers
			* Expensive
		* Solution:
			* DNS returns different addresses based on client's geolocation, server load, etc
	* CDN
		* Caching and replication as a service
		* Integrate forward and reverse caching functionality
		* Large scale distributed storage infrastructure 
		* Combination of (pull) caching and (push) replication
			* Push: Direct result of clients' requests
			* Push: Expectation of high access rate
		* Also do some processing
			* Handle dynamic web pages
			* Transcoding
	* HTTPs
		* HTTP is insecure
		* HTTP Basic authentication: password sent using base 64 encoding -- can be converted to plain text readily
		* HTTPs: HTTP over a connection encrypted by Transport Layer Security (TLS)
		* Provides
			* Authentication
			* Bidirectional encryption
		* Widely used in place of plain vanila HTTP
	* Issues with HTTP
		* Head of line blocking
			* *Slow* objects delay later requests
			* Example objects from remote storages vs from local memory
		* Browsers often open multiple TCP connections for parallel transfers
			* Increases throughput and reduces impact of HOL blocking
			* Increases load on servers and network
		* HTTP headers are big
			* Overheads higher for small objects
		* Objects have dependencies, different priorities
			* Javascript vs Images
			* Extra RTTs for *dependent* objects
	* HTTP/2
		* Google SPDY -> HTTP/2
		* Binary instead of text
			* Efficient to parse, more compact and much less error prone
		* Responses are multiplexed over a single TCP connection
			* Server can send response data whenever it is ready
			* *Fast* objects can bypass *slow* objects -- avoid HOL blocking
			* Fewer handshakes, more traffic (Helps congestion control)
		* Multiplexing uses prioritized flow-controlled schemes
			* Urgent responses can bypass non-critical responses
		* Single TCP connection
		* HTTP headers are compressed
		* Push feature allows server to push embedded objects to the client without waiting for request
			* Saves RTT
* Electronic mail (E-Mail)
	* Three major components
	1. User agents
		* Mail reader
		* Composing, editing, reading mail messages
		* Outgoing incoming messages stored on server
	2. Mail server
		* *Mailbox* contains incoming messages for a user
		* *Message queue* of outgoing (to be sent) mail messages
		* *SMTP Protocol* between mail servers to send email messages
			* Client -- sending mail server
			* Server -- receiving mail server
	3. Simple mail transfer protocol: SMTP
		* Uses TCP to reliably transfer email message from client to server, port 25
		* Direct transferL Sending server to receiving server
		* Three phases of transfer:
			* Handshaking (greeting)
			* Transfer of messages
			* Closure
		* Command/response interaction (like HTTP, FTP)
			* Commands: ASCII text
			* Response: Status code and phrase
		* Messages must be in 7-bit ASCII
		* Uses persistent connections
		* Requires message (header & body) to be in 7-bit ASCII
		* SMTP server uses CRLF.CRLF to determine end of message
		> HTTP: Push SMTP: Pull
		> Both have ASCII command/response interaction, status codes
		> HTTP: Each object encapsulated in its own response message
		> SMTP: Multiple objects sent in multipart message
	* Why send to a receipient server directly instead of sending it to a sender's mail server?
		* Receipient server might not be ready to receive; sender server can store and wait
	* Why do we have a separate receiver's mail server? Cant the recipient run the mail server on their own end system?
		
# Application Layer (DNS, P2P, Video Streaming, and CDN)
* Domain Name System (DNS)
	* Internet hosts, routers:
		* IP address - used for addressing datagrams
		* *name* - e.g. *yahoo.com*
	* Distributed databse
		* Implemented in hierarchy of many *name servers*
	* Application-layer protocol 
		* Hosts, name servers communicate to *resolve* names (address/name translation)
		> Core internet function, implemented as application-layer protocol
		> Complexity at network's edge
	* DNS Services
		* Hostname to IP address translation
		* Indirection
		* Host aliasing
			* Canonical, alisa names
		* Mail server aliasing
		* Local distribution
			* Replicated web servers: many IP addresses correspond to one name
			* Content Distribution Networks: use IP address of requesting host to find best suitable server
	* Goals:
		* No naming conflicts
		* Scalable 
			* Many names
			* (Secondary) frequent updates
		* Distributed, autonomous administration
			* Ability to update my own *domains'* names
			* Dont have to track everybody's updates
		* Highly available
	* Key idea: Hierarchy
		* Three intertwined hierarchies
		1. Hierarchical namespace
			* root -> [edu -> [berkeley, ucla] , com, gov, org, ... ] \(Top level domains)
			* Name is leaf-to-root path
				* *instr.eecs.berkeley.edu.*
		2. Hierarchically administered
			* A *zone* corresponds to a distinct contiguous portion of the DNS name space that is managed by an administrative authority
				* e.g. UCB controls the names \*.berkeley.edu
		3. (Distributed) hierarchy of servers
			* Top of hierarchy: Root servers
				* Location hardwired into other servers
				* 13 root servers
				* Replicated via any-casting (network will deliver DNS messages to the closest replica)
			* Next level: Top-level domain (TLD) servers
				* .com .edu, etc (several new TLDs introduced recently)
				* Managed professionally
				* TLD
					* Responsible for com, org, net, edu, aero, museums, and all top level country domains (uk, fr, etc)
					* Network soluations maintains servers for .com TLD
					* Educause for .edu  TLD
			* Bottom level: Authoratative DNS servers
				* Store the name-to-address mapping
				* Maintained by the corresponding administrative authority
			* Each server stores a small subset of the total DNS database
			* An authoritative DNS server stores *resource records* for all DNS names in the domain that it has authority for
			* Each server can discover the server(s) that are responsible for the other portions of the hierarchy
				* Every server knows the root server(s)
				* Root server(s) knows about all top-level domains
			* Authorative DNS servers
				* Organization's own DNS server(s), providing authoritative hostname to IP mappings for organization's named hosts
				* Can be maintained by organization or service provider
		* Local DNS name server
			* Does not strictly belong to hierarchy
			* Each ISP has one 
				* Also called *default name server* or *DNS resolver*
			* Hosts configured with local DNS server address (e.g. /etc/resolv.conf) or learn server via host configuration protocol (eg. DHCP)
			* Client application
				* Obtain DNS name 
				* Do gethostbyname() to trigger DNS request to its local DNS server
			* When host makes DNS query, the query is sent to its local DNS server
				* Has local cache of recent name-to-address translation pairs
				* Acts as proxy, forwards query into hierarchy
	* Caching, updating records
		* Once (any) name server learns mapping, it *caches* mapping
			* Cache entries timeout (disappear) after some time (TTL)
			* TLD servers typically cached in local name servers
				* Thus, root name servers not often visited
		* Subsequent requests need not burden DNS
		* Cached entries may be *out of date* (best effort name-to-address translation)
			* If name host changes IP address, may not be known internet wide until all TLLs expire
		* Negative caching (optional)			
			* Remember things that dont work
				* Misspellings
			* These can take a long time to fail for the first time
			* Good to remember that they dont work
	* DNS records
		* DNS: Distributed db storing resource records (RR)
			* RR format: (name, value, type, ttl)
		* type=A
			* name is hostname
			* value is IP address
		* type=NS
			* name is domain
			* value is hostname of authoritative name server for this domain
		* type=CNAME
			* name is alias name for some *canonical* name
			* value is canonical name
		* type=MX
			* value is name of mailserver associated with name
	* DNS protocol, messages
		* *query* and *reply* messages, both with same message format
		* message header
			* identification: 16 bit # for query, reply to query uses same #
			* flags:
				* query or reply
				* recursion or desired
				* recursion available
				* reply is authoritative
			* name, type fields for query
			* RR in response to query
			* Records for authoritative servers
			* Additional *helpful* info that may be used
	* Inserting records into DNS
		> Example: "Network Uptopia"
		* Register name *networkutopia.com* at DNS registar (e.g. Network Solutions)
			* Provide names, IP addresses of authoritative name server(primary and secondary)
			* Registar inserts two RRs into .com TLD server:  (*networkutopia.com, dns1.networkutopia.com, NS)(dns1.networkutopia.com, 212.212.212.1, A*)
		* Create authoritative server type A record for *www.networkutopia.com*; type MX record for *networkutopia.com*
		> Never store mappings in root server
		* These records are stored in the authritative server (dns1.networkutopia.com in this case)
	* Updating DNS records
		* Remember that old records may be cached in other DNS servers (for up to TTL)
		* General guidelines:
			* Record the current TTL value of the record
			* Lower the TTL of the record to a low value (e.g. 30 seconds)
			* Wait the length of the previous TTL
			* Update the record
			* Wait for some time (e.g. 1 hour)
			* Change the TTL back to your previous time
	* Reliability
		* DNS servers are replicated (primary/secondary)
			* Name services available if at least one replica is up
			* Queries can be load balanced between replicas
		* Usually, UDP used for queries
			* Need reliability: must implement this on top of UDP
			* Spec supports TCP too, but not always implemented
		* DNS uses port 53
		* Try alternative servers on timeout
			* Exponential backoff when retrying same server
		* Same identifier for all queries
			* Dont care which server responds
	* DNS provides indirection
		* Addresses can change underneath
		* Name could map to multiple IP addresses
			* Enables load balancing
			* Reduce latancy by picking nearby servers
		* Multiple names for the same address
	* Reverse DNS
		* IP address -> domain name
		* Special PTR record type to store reverse DNS entries
		* When is it used?
			* Troubleshooting tools such as traceroute and ping
			* *Received* trace header field in SMTP email
			* SMTP servers for validating IP addresses of originating servers
			* Internet forums tracking users
			* System logging monitoring tools
			* Used in load balancing servers/content distribution to determine location of requester
	* Do you trust your DNS server?
		* Censorship
		* Logging
			* IP addresses, websites visited, geolocation data, and more
	* Attacking DNS
		* DDoS attacks
			* Bombard root servers with traffic
				* Not successful til date
				* Traffic filtering
				* Local DNS servers cache IPs of TLD servers, allowing root servers to be bypassed
			* Bombard TLD servers
				* Potentially more dangerous
		* Redirect attacks
			* Man in middle
				* Intercept queries
			* DNS poisoning
				* Send bogus replies to DNS server, which caches
		* Exploit DNS for DDoS
			* Send queries with spoofed source address: target IP
* P2P applications
	* Pure P2P architecture
		* *no* always on server
		* arbitrary end systems directly communicate
		* peers are intermittently connected and change IP addresses
	* File distribution: client server vs P2P
	> How much time to distribute file (size F) from one server to *N* peers?
		> peer upload/download capacity is limited resource
	* Client server:
		* Server transmission: must send (upload) N file copies
			* time to send one copy: F/u<sub>s</sub>
			* time to send N copies: NF/u<sub>s</sub>
		* Client: each client must download file copy
			* d<sub>min</sub>: min client download rate
			* client download time: F/d<sub>min</sub>
	* P2P 
		* Server transmission: Must upload at least one copy
			* time to send one copy: F/u<sub>s</sub>
		* Client: each clients must download file copy
			* Client download time: F/d<sub>min</sub>
		* Clients: as aggregate must downalod NF bits
			* Max upload rate (limiting max download rate) is u<sub>s</sub> + (Sigma)u<sub>i</sub>
	> lecture slides for bit-torrent notes
* Video streaming and CDNs
	* Video traffic: major consumer of internet bandwidth
	* Challenge: Scale, Heterogenity
		* Solution: Distributed, application level infrastructure
* Multimedia: Video
	* Video: sequence of images displayed at constant rate
	* Digital image: array of pixels
		* Each pixel represented by bits
	* CodingL Use redundancy *within* and *between* images to decrease number of bits used to encode image
		* Spactial (within image)
		* Temporal (from one image to next)
	* CBR: constant bit rate
		* Video encoding rate fixed
	* VBR: variable bit rate
		* Video encoding changes as amount of spacial, temporal coding changes
* Streaming multimedia: DASH
	* Dynamic, Adaptove, Streaming over HTTP
	* Server:
		* Divides video file into multiple chunks
		* Each chunk stored, encoded at different rates
		* *manifest file:* provides URLs for different chunks
	* Client:
		* Periodically measures server-to-client bandwidth
		* Consulting manifest, requests one chunk at a time
			* Chooses maximum coding rate sustainable given current bandwidth
			* Can choose different coding rates at different points in time (depending on available bandwidth at time)
		* *intelligence at client*
			* when to request chunk (so that buffer starvation or overflow does not occur)
			* what encoding rate to request (higher quality when more bandwidth available)
			* where to request chunk from (can request from URL server that is *close* to client or high available bandwidth)
* Content Distribution Networks (CDNs)
	* store/serve multiple copies of videos at multiple geographically distributed sites (CDNs)
		* Enter deep: push CDN servers deep into many access networks
			* Close to users
		* Bring home: smaller number of larger clusters in POPs near (but not within) access networks
	* CDN: Stores copies of content at CDN nodes
	* Subscriber requests content from CDN
		* directly to nearby copy, retrieves content
		* may choose different copy if network path congested
		
# Transport Layer
* Network layer
	* What it does: finds paths through network
		* Routing from one end host to another
	* What it doesnt
		* Reliable transfer: *best effort delivery*
		* Guarantee paths
		* Arbitrate transfer rates
* Transport services and protocols
	* Provide *logical communication* between app processes running on different hosts
	* Transport protocols run in end systems
		* sender side: breaks app messages into *segments*, passes to each network layer
		* receiver sideL reassembles segments into messages, passes to app layer
		* Exports services to application that network layer does not provide
* Multiplexing and demultiplexing
	* Mutliplexing at sender
		* Handle data from multiple sockets, add transport header (later used for demultiplexing)
	* Demultiplexing at receiver
		* Use handler info to deliver received segments to correct socket
* Connectionless demultiplexing
	* recall: created socket has host-local port number
	* recall: when creating datagram to send into UDP socket, must specify
		* Destination IP address
		* Destination port
	* When host receives UDP segment
		* checks destination port number in segment
		* directs UDP segment to socket with that port number
	> IP diagrams with *same destination port number* but different source IP addresses and/or source port numbers will be directed to the same socket at destination
* Connection-oriented demultiplexing
	* TCP socket identified by 4-tuple
		* Source IP address
		* Source port number
		* Destination IP address
		* Destination port number
	* Demultiplexing: receiver uses all four values to direct segment to appropriate socket
	* Server host may support many simultaneous TCP sockets
		* Each socket is identified by its own 4-tuple
	* Webservers have different sockets for each connecting client
		* Non-persistent HTTP will have different socket for each request
* User Datagram Protocol: UDP
	* *No frils, bare bones* internet transport protocol
	* *Best effort* service, UDP segments may be
		* Lost
		* Delivered out of order to app
	* *Connectionless*
		* No handshaking between UDP sender, receiver
		* Each UDP segment handled independently of others
	* Why is there UDP?
		* No connection establishment (which can add delay)
		* Simple: no connection state at sender, receiver
		* Small header size
		* No congestion control: UDP cna blast away as fast as desired
	* UDP checksum
		* *Goal*: Detect *errors* in transmitted segment
			* Router memory errors
			* Driver bugs
			* Electromagnetic interference
		* Sender:
			* Treat segment contents, including header fields, as sequence of 16 bit integers
			* Checksum: addition(one's complement sum) of segment contents
			* Sender puts checksum value into UDP checksum field
		* Receiver
			* Add all the received together as 16 bit integers
			* Add that to the checksum
			* If the result is not 1111 1111 1111 1111, there are errors
		* Checksum is the 16 but one's complement of the one's complement sum of a pseudo header of information from the IP header, the UDP header, and the data, padded with zero oectets at the end (if necessary) to make a multiple of two octets
		* Checksum header, data, and pre-pended IP pseudo header
	* UDP Applications
		* Latency sensitive/time critical
			* Quick request/response (DNS, DHCP)
			* Network management (SNMP)
			* Routing updates (RIP)
			* Voice/video chat
			* Gaming
		* Error correction managed by periodic messages
* Reliable data transfer
	* rdt1 1.0: reliable transfer over a reliable channel
		* Underlying channel perfectly reliable
			* No bit errors
			* No loss of packets
		* Transport layer does nothing
	* rdt 2.0: channel with bit errors
		* Underlying channel may flip bits in packet
			* Checksum to detect bit errors
		* How to recover from errors
			* *Acknowledgements*: receiver explicitly tells sender that pkt received OK
			* *Negative acknowledgements*: receiver explicitly tells sender that pkt had errors
			* Sender retransmits pkt on receipt of Negative Aknowledgement
		* New mechanisms in rdt 2.0:
			* Error detection
			* Feedback: control msgs (ACK, NAK) from receiver to sender
			* retransmission
		* Flaw:
			* If acknowledgement or negative acknowledgement is corrupted:
				* Sender doesnt know what happened at receiver
				* Can't just retransmit: possible duplicate
			* Handling duplicates:
				* Sender retransmits current pkt if acknowledgement/negative acknowledgement is corrupted
				* Sender adds *sequence number* to each packet
				* Receiver discards duplicate pkt
	* rdt 2.1: discussion:
		* sender:
			* seq # added to pkt
			* two sequence numbers (0,1) will suffice
			* must check if received ACK/NAK corrupted
			* Twice as much state
				* state must remember whether expected pkt should have seq # 0 or 1
		* receiver:
			* Must check if received packet is duplicate
				* State indicates whether 0 or 1 is expected pkt sequence #
			> Receiver cannot know if its last ACK/NAK received OK at sender
	* rdt 2.2: a NAK-free protocol
		* Same functionality as rdt 2.1, using ACKs only
		* Instread of NAK, receiver sends ACK for last pkt received OK
			* Receiver must explicitly include sequence # of pkt being ACKed
		* Duplicate ACK as sender results in same action as NAK; retransmit current pkt
	* rdt 3.0: channels with errors and loss
		* underlying channel can also loose packets (data, ACK)
			* checksum, sequence number, ACKs, retransmissions will be of help; but not enough
		* Sender waits *reasonable* amount of time for ACK
			* retransmits if no ACK received in this time
			* if pkt (or ACK) just delayed, not lost
				* retransmission will be duplicate, but sequence numbers already handles this
				* receiver must specift sequence number of pkt being ACKed
			* requires countdown timer
			* No retransmission on duplicate ACKs
		* Stop and wait operation
			* not performant as you have to wait
		* Performance:
			* rdt 3.0 is correct, but the performance is bad
			* Network protocol limits the use of physical resources
	* Pipelined protocols
		* Sender allows multiple *in flight*, yet-to-be-acknowledged pkts
			* Range of sequence numbers must be increased
			* Buffering at sender and/or receiver
		* Two generic forms of pipelined (sliding window) protocols: go-back-N, selective repeat
	* Go back N
		* Sender can have up to N unacked packets in pipeline
		* Sender has single timer for oldest unacked packet; when timer expires, retransmit all unacked packets
		* There is no buffer available at Receiver, out of order packets are discarded
		* Receiver only sends *cumulative ack*, doesnt ack new packets if theres a gap
	* Selective repeat
		* Sender can have up to N unacked packets in pipeline
		* Sender maintains timer for each unacked packet, when timer expires, retransmit only that unacked packet
		* Receiver has buffer, can accept out of order packets
		* Receiver sends individual ack for each packet
* TCP
	* Point to point
		* One sender, one receiver
	* Reliable, in order byte stream
		* No *message boundaries*
	* Pipelined
		* TCP vongestion and flow control set window size
	* Send and receive buffers
	* Full duplex data
		* Bidirectional data flow in same connection
		* MSS: Maximum segment size
	* Connection oriented 
		* Handshaking (exchange of control messages) inits sender, receiver state before data exchange
	* Flow controlled
		* Sender will not overwhelm receiver
	* What does TCP do?
		* Checksum
		* Sequence numbers are byte offsets
			* Sequence numbers: byte stream *number* of byte in segments of data
		* Receiver sends cumulative acknowledgements (Like GBN)
		* Receiver can buffer out-of-sequence packets (Like SR)
		* Sender maintains a single retransmission timer (like GBN) and retransmits on timeout
		* Introduces fat retransmit: optimization that uses duplicate ACKs to trigger early retransmission
	* TCP Maximum Segment Size
		* IP Packet
			* No bigger than Maximum Transmission Unit (MTU)
			* E.g. upto 1500 bytes with ethernet
		* TCP Hacket
			* IP packet with a TCP header and data inside
			* TCP header >= 20 bytes long
		* TCP segment
			* No more than maximum segment size (MSS) bytes
			* MSS = MTU - 20 (min IP header) - 20 (min TCP header)
	* ACKing and sequence numbers
		* Sender sends packet
			* Data starts with sequence number X
			* Packets contains B bytes [X, X+1, ...]
		* Upon receipt of packet, receiver sends an ACK
			* If all data prior to X already received:
				* ACK acknowledges X+B
			* If highest in-order byte received is Y s.t. (Y  + 1) < X
				* ACK acknowledges Y + 1
				* Even if this has been acked before
	* Normal pattern
		* Sender: seq no = X; len = B
		* Receiver: ACK = X + B
		* Sender: seq no = X + B; len = B
		* Receiver: ACK = X + 2B
		* Sender: seq no = X + 2B; len = B
		* Seq no of next packet is same as last ACK field
	* Packet loss
		* Sender: seq no = X; len = B
		* Receiver: ACK = X + B
		* Sender: (seq no = X + B; len = B) **LOST**
		* Sender: seq no = X + 2B; len = B
		* Receiver: ACT = X + B	
	* Piggybacking
		* Both sides of connection some data
	* Loss with cumulative ACKs
		* Sender sends packets with 100 bytes and sequence numbers
			* 100, 200, ...
		* Assume the fifth packet (seq no 500) is lost but not others
		* Stream of ACKS will be
			* 200, 300, 400, 500, 500, 500
	* TCP round trip time, timeout
		* How to set TCP timeout value?
			* Longer than RTT
				* BUT RTT varies
			* Too short: premature timeout, unnecessary retransmissions
			* Too long: slow reaction to segment loss and connection has lower throughput
		* How to estimate RTT?
			* Sample RTT: measured time from segment transmission until ACK receipt
				* Ignroe retransmissions
			* Sample RTT will vary, want estimated RTT *smoother*
				* Average several recent measurements, not just current **SAMPLE RTT**
		* Estimated RTT = (1-a) \* EstimatedRTT + a \* SampleRTT
			* Exponential weighted moving average
			* Influence of past sample decreases exponentially fast
			* Typical value: a = 0.125
		* Timeout interval: Estimated RTT + *safety margin*
			* Large variation in estimated RTT --> Larger safety margin
		* Estimate sample RTT deviation from Estimated RTT
		* Timeout interval = EstimatedRTT + 4 \* DevRTT
	* TCP Sender events:
		* Data received from app:
			* Creqte segment with sequence number
			* Sequence numbner is byte-stream number of first data byte in segment
			* Start timer if not already running
				* Think of timer as for oldest unacked segment
				* Expiration interval: TimeOutInterval
		* Timeout:
			* Retransmit segment that caused timeout
			* Restart timer
		* ACK received
			* If acknowledges previous unacked segments:
				* Update what is known to be ACKed
				* Start timer if there are still unacked segments
	* TCP flow control
		* Receiver controls sender, so sender wont overflow receiver's buffer by transmitting too much, too fast
		* Receiver *advertises* free buffer space by including **rwnd** value in TCP header of receiver-to-semder segments
			* *RcvBuffer* size set via packet options (typically 4096 bytes)
			* Many operating systems autoadjust RcvBuffer
		* Sender limits amount of unacked data to receivers rwnd value
		* Guarantees receive buffer will not overflow
		* What if rwnd = 0?
			* Sender would stop sending data
			* Eventually the receive buffer would have space when the application process reads some bytes
			* But how does the receiver advertise the new **rwnd** to the sender?
		* Sender keeps sending TCP segments with one data byte to the receiver
		* These segments are dropped but acknowledged by the receiver with zero-window size
		* Eventually when the buffer empties, non-zero window is advertised
	* Connection management
		* Before exchanging data, sender/receiver *handshake*
			* Agree to establish connection (each knowing the other willing to establish connection)
			* Agree on connection parameters
	* SYN loss and web downloads
		* User clicks on hypertext link:
			* Browser creates a socket and does a *connect*
			* The *connect* triggers the OS to transmit a SYN
			* The *connect* triggers the OS to transmit a SYN
		* If the SYN is lost
			* 1-3 seconds of delay can be very long
			* User may become impatient
			* ... and click the hyperlink again, or click reload
		* User triggers an *abort* of the *connect*
			* Browser creates a new socket and another connect
			* Essentially, forces a faster send of new SYN packet
			* Sometimes very effective, and the page comes quickly
	* TCP: closing a connection
		* Client, server each close their side of connection
			* send TCP segment with FIN bit = 1
		* Respond to received FIN with ACK
			* On receiving FIN, ACK can be combined with own FIN
		* Simultaneous FIN exchanges can be handled
	* Principles of congestion control
		* *congestion*
			* *too many sources sending too much data too fast for network to handle*
			* Different from flow control
			* Manifestations:
				* loss packets (buffer overflow at routers)
				* long delays (queueing in router buffers)
	* Without congestion control:
		* *congestion*
			* Increases delays
				* if delays > RTO. sender retransmits
			* Increases loss rate
				* Dropped packets also retransmitted
			* Increases retransmissions, many unnecessary
				* Wastes capacity of traffic that is never delivered
				* Increase in load results in decrease in useful work donw
			* Increases congestion, cycle continues
	* Const of congestion
		* Knee - point after which
			* Throughput increases slowly
			* Delay increases fast
		* Cliff - point after which
			* Throughput starts to drop to zero
			* Delay apporaches infinity
	* Approaches towards congestion control:
		* End-end congestion control
			* No explicit feedback from network
			* Congestion inferred from end system observed loss, delay
			* Approach taken by TCP
		* Network-assisted congestion control
			* Routers provide feedback to end systems
				* Single bit indicating congestion
				* Explicit rate for sender to send at
	* TCP's approach in a nutshell
		* TCP connection maintains a window
			* Controls number of packets in flight
		* TCP sending rate:
			* *roughly* send cwnd bytes, wait RTT for ACKS, then send more bytes
	* All these windows...
		* Congestion window: CWND
			* How many bytes can be sent without overflowing routers
			* Computed by the sender using congestion control algorithm
		* Flow control window: advertised/receive window (RWND)
			* How many bytes can be sent without overflowing receiver's buffers
			* Determined by the receiver and reported to the sender
		* Sender-side window: minimum(CWND, RWND)
			* Assume for this discussion that RWND >> CWND
	* Detection congestion: infer loss
		* Duplicate ACKs: isolated loss
			* Duplicated ACks indicate network capable of delivering some segments
		* Timeout: much more serious
			* Not enough dup ACKs
			* Must have suffered several losses
	* Rate adjustment
		* Basic structure:
			* Upon receipt of ACK (of new data): increase rate
			* Upon detecton of loss: decrease rate
		* How we increase/decrease the rate depends on the phase of congestion control we're in
			* Discovering available bottleneck bandwidth vs.
			* Adjusting to bandwidth variations
	* TCP slow start (bandwidth discovery)
		* When connection begins, increase rate exponentially, until first loss event
			* initally,cwnd = 1 MSS
			* Double cwnd every RTT (full ACKs)
			* Simpler implementation achieved by incrementing cwnd every ack received
				* CWND  += 1 for each ACK
		* Initial rate is slow but ramps up exponentially fast
	* Adjusting to varying bandwidth
		* Slow start gave an estimate of available bandwidth
		* Now, want to track variations in this available bandwidth, oscillating around its current value
			* Repeated probing (rate increase) and backoff (rate decrease)
			* Known as congestion avoidance
		* TCP usesL *Additive Increase Multiplicative Decrease*
	* AIMD
		* Sender increases transmission rate (window size) probing for usable bandwidth until another congestion event occurs
			* Additive increase
				* Increase CWND by 1 MSS every RTT until loss detected
					* For each successful RTT (all ACKS), CWND = CWND + 1
					* Simple implementation: for each ACK, CWND = CWND + 1/CWND
			* Multiplicative decrease: 
	0			* Cut cwnd in half after loss

# Network Layer: Data Plane
* Internetworking
	* Cerf & Kahn in 1974
		* *A protocol for packet network intercommunication*
		* Foundation for modern internet
	* **Routers** forward **packets** from source to destination
		* May cross many separate networks along the way
	* All packets use a common **internet protocol**
		* Any underlyind data link protocol
		* Any higher layer transport protocol
* Network layer
	* Transport segment from sending to receiving host
	* On sending side, encapsulates segments into datagrams
	* On receiving side, delievers segments to transport layer
	* Every layer protocols in *every* host, router
	* Router examines header fields in all IP datagrams passing through it
	* Two Key network layer functions:
		* Forwarding: moving packets from routers input to appropriate output
		* Routing: determine route taken, by packets from source to destination
* Data plane vs control plane
	* Data plane:
		* Local, per-router function
		* Determines how datagram arriving on router input port is forwarded to router output port
		* Forwarding function
	* Control plane
		* Network wide logic
		* Determines how datagram is routed among routers along end-end path from source host to destination host
		* Two control-pane approaches
			* Traditional routing algorithms: implemented in routers
			* Software-defined networking: centralised (remote) servers
		* Per-router control plane
			* Individual routing algorithm components in each and every router interact in the control plane
		* Logically centralised control plane (SDN)
			* A distinct (typically remove) controller interacts with local control agents (CAs)
	> What service modal for *channel* transporting datagrams for sender to receiver?
	> No guarantee whatsoever is provided by IP layer in TCP/IP protocol stack. Its *best effort service*

* IP Packet Structure
	* Version (4 bits)
		* Indicate the version of IP protocol
		* Necessary to know what other fields to expect
		* Typically 4 (IPv4)
	* Header length (4 bits)
		* Number of 32 bit words in header
		* Typically 5 (for a 20 byte IPv4 header)
		* Can be more when IP options are used
	* Total length (16 bits)
		* Number of bytes in the packet
		* Maximum size is 65,535 bytes (2<sup>16</sup>-1)
		* ... though underlying links may impose smaller limits
	* Source IP Address (32 bits)
	* Destination IP Address (32 bits)
	* Protocol (8 bits)
		* Tells end-host how to handle packet
		* Identifies the higher-level transport protocol
		* Important for demultiplexing at receiving host
	* TTL (Time to leave, 8 bits)
		* Forwarding loops cause packets to cycle for a long time
			* As these accumulate, eventually consume all capacity
		* Decremented at each hop, packet discarded if reaches 0
		* and ... *time exceeded* message is sent to the source
	* Checksum (Header Corruption, 16 bits)
		* Particular form of checksum over packet header
		* If not correct, router discards packets
			* So it doesnt act on bogus information
		* Checksum recalculated at every router
	* Special handling
		* Types of service or Differentiated Services Code Point (8 bits)
			* Allow packets to be treated differently based on needs
			* Has been refined several times
			* Not widely used
* IP fragmentation, reassembly
	* Networks links have MTU (max transfer size) -- largest possible link level frame
		* Different link types, different MTUs
	* Large IP datagram divided (*fragmented*) within net
		* One datagram becomes several datagrams
		* Reassembled only at final destination
		* IP header bits used to identify, order related fragments
* IPv4 Fragmentation procedure
	* Fragmentation
		* Router breaks up datagram in size that output link can support
		* Copies IP header to pieces
		* Adjust length on pieces
		* Set offset to indicate position
		* Set MF (More fragments) flag on pieces except the last
		* Recompute the checksum
	* Re-assembly
		* Receiving host uses identification field with MF and offsets to complete the datagram
		* Fragmentation of fragments also supported
* Path MTU discovery procedure
	* Host
		* Sends a big packet to test whether all routers in path to the destination can support or not
		* Set DF (Do not fragment) flag
	* Routers
		* Drops the packet if its too large (as DF is set)
		* Provides feedback to Host with ICMP message telling the maximum supported size
* IP addressing
	* IP Address: 32-bit interface for host, router, interface
	* Interface: connection between host/router and physical link
		* Routers typically have multiple interfaces
		* Host typically has one or two interfaces
	* IP addresses associated with each interface
	* Networks
		* IP Address:
			* Network part: high order bits
			* Host part: low order bits
		* Whats a network?
			* Device interfaces with same network part of IP address
			* Can physically reach each other without intervening router
	* Allocated as blocks have geographical significance
	* Possible to determine the geographical location of an IP address
* Masking
	* Mask
		* Used in conjunction with the network address to indicate how many higher order bits are used for the network part of the address
			* Bit-wise AND
		* 223.1.1.0 with mask 255.255.255.0
	* Broadcast Address
		* Host part is all 111's
		* e.g. 223.1.1.255
	* Network Address
		* Host part is all 0000's
		* e.g. 223.1.1.0
	* Both of these are not assigned to any host

* Subnetting
	* Dividing the class A, B or C network into more manageable chunks that are suited to your network's size and structure
	* Subnetting allows 3 levels of hierarchy
		* net id,  subnetid, hostid,
	* Original netid remains the same and designates the site
	* Subnetting remains transparent outside the site 
	* The process of subnetting simply extends the point where 1's of Mark stop and 0's start
	* You are sacrificing host ID bits to gain network ID bits

* Classes InterDomain Routing (CIDR)
	* Network portion of address of arbitrary length
	* Address format: a.b.c.d/x where x is # of bits in network oprtion of address

* How does a host get IP addresses?
	* Hard coded by system admin in file
	* DHCP -- Dynamic Host Configuration Protocol
		* Dynamically get address from as server
		* *Plug and play*
* DHCP
	* goal: Allow host to dynamically obtain its IP address from network server when it joins network
	* Can renew its lease on address in use
	* Allows reuse of addresses (only hold address while connected/on)
	* Support for mobile users who want to join network
	* Overview:
		* Host broadcasts *DHCP discover* msg
		* DHCP server responds with *DHCP Offer* msg
		* Host requests IP address: *DHCP request* msg
		* DHCP server sends address *DHCP ack* msg
	* More than IP addresses
		* DHCP can return more than just allocated IP address on subnet
			* Address of first hop router for client
			* Name and IP address of DNS server
			* Network mask (indicating network vs host portion of address)
	* Use port number 67 on server and 68 on client side
	* Usually MAC address is used to identify clients
		* DHCP server cann be confifured with a *registered* list of acceptable MAC addresses
	* DHCP offer message includes IP address, length of lease, subnet mark, DNS servers, default gateway
	* DHCP security holes
		* DoS attack by exhausting pool of IP addresses
		* Masquerading as DHCP server
		* Authentication for DHCP -RFC 3118

* Private addresses
	* Defined in RFC 1918
		* 10.0.0.0/8 (16,777,216 hosts)
		* 172.16.0.0/12 (1,048,576 hosts)
		* 192.168.0.0/16 (65536 hosts)
	* These addresses cannot be routed
		* Anyone can use them
		* Typically used for NAT

* Network Address Translation (NAT)
	* All datagrams leaving local network have same single source NAT IP address: 138.76.29.7, different port numbers
	* Datagrams with source or destination in this network have 10.0.0/24 address for source, destination (as usual)
	* NAT router must:
		* Outgoing diagrams: *replace* source IP address, port # of every outgoing datagram to NAT IP address, new port # 
		* Remember in NAT translation table every source IP address, port # to NAT IP address, new port # translation pair
		* Incoming diatagramsL *replace* NAT IP address, new # in destination fields of every incoming datagram with corresponding source IP address, port # stored in NAT table
	* Advantages
		* Local network uses just one IP address as far as outside world is concerned
			* Range of addresses not needed from ISP: just one IP address for all devices
				* 16-bit port number field: \~ 65000 simultaneous connections with one WAN-side address
			* Can change addresses of devices in local network without notifying outside world
			* Can change ISP without changing addresses of devices in local network
	* Disadvantages
		* NAT violates the architectural model of IP
			* Every IP address uniquely identifies a single node on Internet
			* Routes should onlt process up to layer 3
		* NAT changes the internet from connectionless to a kind of connection-oriented network
		* NAT possibility must taken into account by app designers *e.g. p2p applications*
	* Practical issues
		* Nat modifies port # and IP address
			* Requires recalculation of TCP and IP checksum
		* Some applications embed IP address or port numbers in their message payloads
			* DNS, FTP, SIP, H.323
			* For legacy protocols, NAT must look into these packets and translate the embedded IP addresses/port numbers

* IPv6
	* Motivation:
		* 32-bit address space soon to be completely allocated
		* Header format helps speed processing/forwarding
		* Header changes to facilitate QoS
	* Format
		* Fixed length 40 byte header
		* No fragmentation allowed
		* Priority: identify priority among datagrams in flow (traffic class)
		* Flow label: identify datagrams in same *flow* 
		* Next header: identify upper layer protocol for data
		* Checksum: removed entirely ro reduce processing time at each hop
		* Options: allowed, but outside header, indicated by next header field
		* IMCPv6: new version of IMCP
			* Additional message types: *e.g. Packet to big*
			* Multicast group management functions
	* Transition from IPv4 to IPv6
		* Not all routers can be upgraded simultaneously
			* No *flag days*
			* How will network operate with mixed IPv4 and IPv6 routers?
		* Tunneling: IPv6 datagram carried *payload* in IPv4 datagram among IPv4 routers

# Network Layer: Control Plane
* Network layer functions
	* Forwarding (Data plane):
		* Move packets from router's input to appropriate router output
	* Routing (Control plance):
		* Determine route taken by packets from source to destination
	* Two approaches to structuring network control plane
		* Per-router control (traditional)
			* Individual routing algorithm components in each and every router interact with each other in control plane to compute forwarding tables
		* Logically centralized control (software defined networking)
			* A distinct (typically remote) controller interacts with lcoal control agents (CAs) in routers to compute forwarding tables

* Internet routing
	* Works at two levels
	* Each AS runs *intra-domain* routing protocol that establishes routes within its domain
		* AS -- region of network under a single administrative entity
		* Link state e.g. Open Shortest Path First (OSPF)
		* Distance vector e.g. Routing Ingormation Protocol (RIP)
	* ASes participate in an *inter-domain* routing protocol that establishes routes between domains
		* Path vector, e.g. Border Gateway Protocol (BGP)

* Routing algorithm classes
	* Link state (Global)
		* Routers maintain cost of each link in the network
		* Connectivity/cost changes flooded to all routers
		* Converges quickly (less inconsistency, looping, etc)
		* Limited network sizes
	* Distance vector (Decentralised)
		* Router maintain next hop & cost of each destination
		* Connectivity/cost changes interatively propagage form neighbour to neighbour
 		* Require multiple rounds to converge
		* Scales to large networks
	* Link state routing
		* Each note maintains its *local link state*
		* Each node floods its local link state (LS)
			* On receiving a *new* LS message, a router forwards the message to all its neighbours other than the one it received the message from
			* Flooding LSAs
				* Routers transmit *Link State Advertisement* (LSA) on links
					* A neighbouring router forwards out all links except incoming
					* Keep a copy locally; dont forward previously-seen LSAs
				* Challenges
					* Packet loss
					* Out of order arrival
				* Solutions
					* Acknowledgements and retransmissions
					* Sequence numbers
					* Time-to-leave for each packet
		* Eventually, each note learns the entire network topology
			* Can use Dijkstra's compute the shortest path between nodes
		* Algorithm: Dijkstra's
			* Net topology, link costs known to all nodes
				* Accomplished via *link state broadcast*
				* All nodes have same information
			* Computes least cost paths from one node to all other nodes
				* Gives forwarding table for that node
			* Issues
				* Scalability
				* Transient Distruptions
				* Oscillations
	* Distance vector routing
		* Each router knows the link to its neighbors
		* Each router has provisional *shortest path* to every other router --  its *distance vector (DV)*
		* Routers exchange this DV with their neighbours
		* Routers look over the set of options offered by their neighbours and select the best one
		* Iterative process converges to set of shortest paths 
		* Algorithm: Bellman Ford's
			* Issues
				* Slow convergence of routers converging on incorrect information
				* Convergence is the time during which all routers come to an agreement about the best paths through the internetwork
					* Whenever topology changes, there is a period of instability in the network as the routers converge
				* Reacts rapidly to good news, but leisurely to bad news
			* Poisoned Reverse Rule
				* Heuristic to avoid count to infinity

* ICMP: Internet Control Message Protocol
	* Used by hosts & routers to communicate network level information
		* Error reporting: Unreachable host, networkm port
		* Echo request/reply (used by ping)
	* Works above IP layer
		* ICMP messages carried in IP datagrams
	* ICMP messageL type, code plus IP header and first 8 bytes of IP datagram payload causing error

# Data Link Layer
* Nodes - Hosts and routers
* Links - Communication channels that connect adjacent nodes along communication path
	* Wired links
	* Wireless links
	* LANs
* *Data-link layer* has responsibility of transferring datagram from one node to *physically adjacent* node over a link
* Link layer
	* Datagram transferred by different link protocols over different links
	* Each link protocol provides different services
* Link layer services
	* Framing, link access
		* Encapsulate datagrams into frame, adding header, trailer
		* Channel access if shared medium
		* *MAC* address used in frame headers to identify source, dest
			* Different from IP address
	* Reliable delivery between adjacent nodes
		* Seldom used on low bit error link
		* Wireless links: high error rates
	* Flow control
		* Pacing between adjacent sending and receiving nodes
	* Error detection
		* Errors caused by signal attenuation, noise
		* Receiver detects presense of errors
			* Singal sender for retransmission or drops frame
	* Error correction
		* Receiver identifies and corrects bit errors without resorting to retransmission
	* Half-duplex and full duplex
		* With half duplex, nodes at both ends of link can transmit, but not at same time

* Where is the link layer implemented?
	* In each and every host
	* Link layer implemented in *Adaptor* or on a chip
	* Attaches into host's system buses
	* Combination of hardware, software, firmware

	* Adaptors communicating
		* Sending side:
			* Encapsulates datagram in frame
			* Adds error checking bits, rdt, flow control, etc
		* Receiving side
			* Looks for errors, rdt, flow control, etc
			* Extracts datagram, passes to upper layer at receiving side

* Framing
	* Physical layer talks in terms of bits
	* Framing used to identify frames within sequence of bits
		* Delimit the start and end of the frame
	* Ethernet framing
		* Timing/Physical layer
	* Framing in Ethernet
		* Start of frame is recognized by 
			* Preamble: Seven bytes with pattern 10101010
			* Start of Frame Delimiter (SFD): 10101011
		* Inter Frame Gap is 12 bytes (96 bits) of idle state


		