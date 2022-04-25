---
layout: math
---

# what is internet

## nut bolt view

- billions of connected devices
  - hosts - endpoints
- packet switches
  - forward packets
  - routers, switches
- communication links
  - fibre, copper, radio satellite
  - transmission rate - bandwidth
- networks
  - collection of devices, routers, link
    managed by organization
- internet - networks of networks
  - interconnected ISP's
- protocols are everywhere
  - controls sending and receiving of messages
- internet standards
  - **IETF** - Internet engineering task force
    - develops and promotes voluntary Internet standards, 
      in particular the technical standards that comprise 
      the Internet protocol suite
  - **RFC** - Request for comments, produced by IETF

## services view

- infrastructure that provides services to applications
- provides programming interfaces to distributed application

# what is a protocol

Protocols define the 
- format 
- order of messages sent and received among network entities
- and actions taken on message transmission, 
- receipt


# Internet structure

## network edge

- hosts - clients
- servers - in data centers

## access network, physical media

- wired, wireless communication links

## network core

- interconnected routers
- network of networks

# Host: sends packet of data

- host sending function
  - take application messages
  - breaks it into small chunks, known as packets of length $L$ bits
  - transmits packets into access network at transmission rate $R$

- same things:
  - network transmission rate
  - link transmission rate
  - link capacity
  - link bandwidth

- packet transmission delay $d_t$
  - time needed to transmit $L$ bit packet into link
  
$$
d_t = \frac{L}{R} \frac{(\text{bit})}{(\text{bit/s})}
$$