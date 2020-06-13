Title: More Linux Tracing Fun
Date: 2017-07-30 12:11
Author: crossjam
Category: Uncategorized
Slug: more-linux-tracing-fun
Status: published

I find deep dives into eBPF and Linux tracing fascinating. Jean-Tiare Le Bigot has [a basic eBPF intro][2] and then an interesting application to [single host, L2 level, network packet tracing][1].

> eBPF/bcc enables us to write a new range of tools to deeply troubleshoot, trace and track issues in places previously unreachable without patching the kernel. Tracepoints are also quite handy as they give a good hint on interesting places, removing the need to tediously read the kernel code and can be placed in portions of the code that would otherwise be unreachable from kprobes, like inline or static functions.

Also, I learned about [the `mtr` utility][3].


[1]: https://blog.yadutaf.fr/2017/07/28/tracing-a-packet-journey-using-linux-tracepoints-perf-ebpf/
[2]: https://blog.yadutaf.fr/2016/03/30/turn-any-syscall-into-event-introducing-ebpf-kernel-probes/
[3]: https://www.linode.com/docs/networking/diagnostics/diagnosing-network-issues-with-mtr