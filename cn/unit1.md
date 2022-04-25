---
layout: default
---

# Computer Network

- IP Address - consists of two parts
  - network id - identify the network
  - host id - get the host
- Where is port number then?
  - if you visit a web page in the browser then
  - you are using `http` which has a predefined port no - `80`

- the service that is used to convert the domain name to is called
  Domain name Service.
- port number is used to identify a particular process in the host
  For well known services the port number is already 
  predefined and fixed
  - `http` - 80
  - `https`
  - `smtp` - 25
  - `ftp` - 21
- even though your intention is to reach `google.com` you
  are visiting DNS firsts and then getting IP address of google.com and then visiting the google home page.
- This is actually overhead which is also called DNS overhead.

- $2^32$ ip address possible if we use 32-bit number

## Ip address types

- class A - starts with `0`
- class B - starts with `10`
- class C - starts with `110`
- class D - starts with `1110`
- class E - starts with `1111`

- class A - $2^7$ networks and $2^24$ hosts
- class B - $2^14$ networks and $2^16$ hosts
- class C - $2^21$ networks and $2^8$ hosts
- class D - used for multicasting 
- class E - used for military application