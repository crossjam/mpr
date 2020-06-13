Title: Scalable Message Queueing
Date: 2013-01-04 20:50
Author: crossjam
Category: Uncategorized
Slug: scalable-message-queueing
Status: published

At work I started digging into [ActiveMQ][2], mostly because I wanted to whale on some folks who I thought had an unhealthy devotion to some mediocre, unscalable middleware. Then I stumbled upon the [ActiveMQ Apollo][1] project:
> ActiveMQ Apollo is a faster, more reliable, easier to maintain messaging broker built from the foundations of the original ActiveMQ. It accomplishes this using a radically different threading and message dispatching architecture. Like ActiveMQ, Apollo is a multi-protocol broker and supports STOMP, Openwire, MQTT, SSL, and WebSockets.

If [Apollo’s benchmarks][3] prove out in actual deployment, **holy smokes!!** With 1.x release implying a certain amount of stability to boot. I would like to know how it scales with a high number of concurrent subscribers thou.

And ActiveMQ isn’t all that mediocre although it has some clear scaling limitations.

[1]: http://activemq.apache.org/apollo/
[2]: http://activemq.apache.org/
[3]: http://hiramchirino.com/stomp-benchmark/ec2-c1.xlarge/index.html