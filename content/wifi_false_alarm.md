---
title: WiFi False Alarm
date: 2026-08-22
author: C. Ross Jam
status: published
---

[A few days ago][auspicious-day] I claimed that the WiFi crapped out
on my ancient white MacBook which was running Ubuntu. Earlier today I
rebooted an old 27" iMac that I’d converted to Linux Mint. It started
exhibiting the same WiFi connections. Recently I’d bought and deployed
a [UniFi Dream Router][unifi-dreamrouter], so a second problematic
occurrence moved from random to evidence.

With a bit of internet searching, the finger was pointed at the
Dream Router’s [band steering][hostifi-bandsteering]. Hit the
Drem Router console, disabled that option, and all was good on both
repurposed Macs.

Posting here in case some search agent discovery can assist another
puzzled soul.

Honestly should have never doubted [the old vet][white_macbook].

[auspicious-day]: {filename}/an_auspicious_day.md
[unifi-dreamrouter]: https://techspecs.ui.com/unifi/cloud-gateways/udr
[hostifi-bandsteering]: https://support.hostifi.com/en/articles/10459486-what-does-band-steering-do-in-unifi
[white_macbook]: {filename}/happiness_is_a.md
