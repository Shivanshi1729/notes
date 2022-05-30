---
layout: default
title: OSI Model
parent: Computer Networking
---

# OSI Model 

- Open system Interconnection model
- Develop by International organization for standardization
- Reference model
- Describe how information from software application in one computer move through physical medium to the software application in another computer.
- 7 layer
    - `Application Layer`
        - provide service to user
    - `Presentation Layer`
        - for translation,encryption ,compression
    - `Session Layer`
        - used to manage , establish ,terminate session
        -  it allows the communication between two processes which can be either half-duplex or full-duplex.
        - adds some checkpoints when transmitting the data in a sequence.
        - Synchronization and recovery process - if error occurs in middle of transmission, then the transmission will resume from the checkpoint. 
    - `Transport layer`
        -  main responsibility, transfer the data completely
        - receives the data from the upper layer and converts them into smaller units known as segments.
        - termed as an end-to-end layer,provides a point-to-point connection between source and destination to deliver data reliably.
        - ensures that messages are transmitted in the order in which they are sent and there is no duplication of data.
        - protocol used: TCP & UDP 
    - `Network Layer`
        - manages device addressing
        - tracks the location of devices on the network.
        - determines the best path to move data from source to the destination
        - routers used in this layer
        - protocol used: IP ,IPv6
    - `Data-link layer`
        - used for error free transfer of data frames
    - `Physical layer`
        - provide physical medium through which bits are transmitted
- upper layer (_application,presentation,session,transport_)
    - deals with application related issues
    - implemented only in software
- lower layer (_Network,Data-link,physical_)    
    - deals with data transport issue    
- Each layer is self- contained , so that the task assigned to each layer can be performed independently.
