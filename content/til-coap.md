Title: TIL CoAP
Date: 2017-06-21 21:29
Author: crossjam
Category: Uncategorized
Slug: til-coap
Status: published

Saw a post on Hacker News discussing messaging. A comment mentioned [Californium][1]. Being the messaging nerd that I am, had to chase the reference. Little did I know there was a whole IETF protocol for machine to machine messaging on resource constrained devices, [CoAP][2]:

> The Constrained Application Protocol (CoAP) is a specialized web transfer protocol for use with constrained nodes and constrained networks in the Internet of Things. 
The protocol is designed for machine-to-machine (M2M) applications such as smart energy and building automation.

According to the [IETF RFC (7252)][3], CoAP has the following main features:

* Web protocol fulfilling M2M requirements in constrained environments

* UDP [RFC0768] binding with optional reliability supporting unicast and multicast requests.

* Asynchronous message exchanges.

* Low header overhead and parsing complexity.

* URI and Content-type support.

* Simple proxy and caching capabilities.

* A stateless HTTP mapping, allowing proxies to be built providing access to CoAP resources via HTTP in a uniform way or for HTTP simple interfaces to be realized alternatively over CoAP.

* Security binding to Datagram Transport Layer Security (DTLS) [RFC6347].

HTTPish packets over UDP with optional reliable transport. 

Wonder if anybody uses CoAP in practice?

[1]: http://www.eclipse.org/californium/
[2]: http://coap.technology
[3]: https://tools.ietf.org/html/rfc7252