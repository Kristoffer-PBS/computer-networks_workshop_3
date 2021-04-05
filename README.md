# Workshop 3 - Assignment: Time Protocol with Network Sockets

### Kristoffer Plagborg Bak Sørensen, 201908140
### Pernille Sonne Pallesen, 201909457

### Introduction

This short document is made for [Workshop 3](https://github.com/rhjacobsen/CN_workshops/tree/master/Workshops/3) in Computernetworking. The workshop is about implementing a client and a server for the Time Protocol specified in [RFC 868](https://tools.ietf.org/html/rfc868).

The optional part of the workshop has not been made.

The client and server can be run on Linux machines, and are implemented for the UDP-based services and the TCP-based services. Both implementations are written in Python and make use of the socket API.


### How to compile and use the programs

<!-- Description of how to compile (if applicable) and use the programs. Remember to set the appropriate permission on the files. -->

The four python scrips have an added "shebang" `#! /usr/bin/env python3` at the top of the document, such that the programs can be invoked by `./tp<PROTOCOL><client|server>`, where `PROTOCOL` can be either `tcp` or `udp`. All 4 files have their user execution bit set, but if for some reason you are not able to execute the scripts after downloading the repository, then you can set them by using the `chmod` program e.g. `chmod u+x tptcpserver`. If you have a different way of starting the python3 interpreter you can simply remove these lines, and use you own preferred method e.g. `python3 tp<PROTOCOL><client|server>`. Both the UDP and TCP server will default to create and bind a socket on `"127.0.0.1:7890"`, and the both the clients will default to use `"127.0.0.1:7890"` to create a connection. These options can be changed and set by the user, by invoking the programs with respective flags e.g. `./tpudpclient --serverhost 192.168.0.2 --port 42069`. Call each script with `--help` or look at the source code, for how to set options. 


### Implementation

TODO: Lav drawio af figur fra koden og sæt ind her (både en for TCP og UDP)

<!-- A short overall description of how the implementation has been structured -->

<!-- A description of how the socket API is used in the implementation. -->

![tcp](diagrams/interaction_sequence_diagram_TCP.png)



### Ny overskrift

<!-- A description of how it has been ensured that the implementation conforms to the protocol standard as described in RFC 868, including a documentation of the conformance testing described in the previous section.
i.e. "Use Wireshark to identify the exchange of timestamps between the server and the client. Is the payload size in the packet 32 bit (4 bytes) as specified in RFC 868?"-->

### Ny overskrift

<!-- A description of problems encountered, assumptions and simplifications made (if applicable). -->


