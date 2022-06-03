---
layout: default
title: Summary
parent: Software Engineering
mathjax: true
mermaid: true
---

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## ISO 9126 quality standards

- Functionality
- Reliability
- Usability
- Efficiency
- Maintainability
- Portability

## Software Crisis

The result of incremental failure rate of software development which led to an incomplete and degrading performance of software products.

**Causes**

- Increasing Demand
- Increasing Complexity
- Increasing Challenges
- Same workforce
- Same methods
- Same tools

## Types of softwares

- System software

- Application software
- Scientific / Engineering software
- Embedded software
- Web application
- AI Software
- Networking software
- Business software
- Entertainment software
- Utility software
- Document management software
- Reservation software

## Software models

### Code and Fix Model

- Characteristics
  - Start coding right away and fix the bugs as we go

- Advantages
  - Convenient for small projects
  - Time saver for low budget products
  - Good for entry level developers
  - Full control over development process

- Disadvantages
  - Might run into huge unseen problems
  - Difficult to maintain and change later
  - Might have quality issues

### Waterfall Model (Winston W. Royce)

- Characteristics
  - Consists of a number of phases. 
  - One phase cant be started before another's completion. 
  - Work is divided among different class of specialists. 
  - Work on one phase is frozen and documentation is passed on.

<div class="mermaid">
flowchart TD
    id1(Requirement analysis and specification)
    id2(Design and specification)
    id3(Coding and Unit Testing)
    id4(Integration and System Testing)
    id5(Delivery and Maintainence)
    id1-->id2-->id3-->id4-->id5
</div>

- Advantages
  - Simple and easy to understand
  - All phases are procesed one at a time
  - All phases well documented
  - Reduces development and maintainence cost
  - Enables organization
  - New person can take up an older project easily

- Disadvantages
  - Model does not allow phases to overlap, but they do in real life
  - Not a good model for long/ongoing softwares
  - Difficult to accomodatea any changes midway
  - No working software produced till the end of the lifecycle

### Iterative Waterfall Model

<div class="mermaid">
flowchart TD
a(Feasibility study)
b(Requirement analysis and specification)
c(Design and Specification)
d(Coding and Unit Tesing)
e(Integration and System Testing)
f(Maintainence)
a-->b-->c-->d-->e-->f
f-->b
f-->c
f-->e
f-->d
</div>

### V Model

- Characteristics
  - The verification and validation model
  - <img src="https://media.geeksforgeeks.org/wp-content/uploads/V-Model.png" title="" alt="Software Engineering | SDLC V-Model - GeeksforGeeks" width="381">

- Advantages
  - Easy to manage due to rigidity of the model
  - Defects are found at early stage
  - Simple to understand and follow

- Disadvantages
  - High risk and uncertainity
  - Not good for complex projects
  - Does not support iteration phases
  - Does not handle concurrent events

### Evolutionary Model

- Characteristics
  - Software is developed constantly
  - Get customer feedbacks to accomodate them

- **Incremental imlpementation**
  - Few functions are developed to get a working model.
  - Later more functions are added.

- **Prototyping**
  
  - A working prototype is provided to the user in order to get the feedback from the user.
    - Throwaway prototyping
    - Evolutionary prototyping

### Spiral Model

- <img title="" src="https://media.geeksforgeeks.org/wp-content/uploads/spiral-1-1024x945.jpg" alt="Lightbox" width="387">

## Metrics for comparing SDLC models

- Shortfall - How far the software is from user requirements
- Lateness - Time delay
- Adaptability - Adaptation of software  to new requirements
- Longevity - Time till the software is replaced
- Inappropriateness - Measure behavior of shortfall over time

___

## Non-traditional development methods

### Rapid Application Development

- Based on prototyping and iterative development with no specific planning involved
- RAD produces a software in minimum time
- Use of powerful tools and techniques

<div class="mermaid">
flowchart TD;
a(Business Modelling)
b(Data Modelling)
c(Process Modelling)
d(Application Generation)
e(Testing and Turnover)
a-->b-->c-->d-->e-->|Team1|a
f(Business Modelling)
g(Data Modelling)
h(Process Modelling)
i(Application Generation)
j(Testing and Turnover)
f-->g-->h-->i-->j-->|Team2|f
</div>

### Rational Unified Process

Process independent lifecycle approach. 

<div class="mermaid">
flowchart LR;
Inception-->Elaboration-->Construction-->Transition
id1(Establish a Business case for the system)
id2(Develop understanding of the problem domain)
id3(Design, program and Test)
id4(Moving from development to user community)
inception-->id1
elaboration-->id2
construction-->id3
transition-->id4
</div>

Perspectives or RUP

- **Dynamic perspective** shows phases of model over time
- **Static perspective** shows process activities that are enacted
- **Practice perspective** suggests good practices to be used during the process

### Agile Development Process

Used when the requirements change rapidly

[Manifesto](http://agilemanifesto.org/)

[Principles](http://agilemanifesto.org/principles.html)

| Principle             | Description                                                                                               |
| --------------------- | --------------------------------------------------------------------------------------------------------- |
| Customer involvemnet  | Customers should be closely involved throughtout the development phase                                    |
| Incremental delilvery | Customers specify the requirements in each increment                                                      |
| People not process    | Skills of development team should be recognized and exploited, rather than following a particular process |
| Embrace changes       | Expect the changes to the system so that they can be easily accomodated                                   |
| Maintain simplicity   | Wherever possible, stay simple                                                                            |

<div class="mermaid">
flowchart LR;
User-Stories<-->Specification
Specification-->Test-->Implementation-->Design-->Specification
Test-->Design
</div>

### Extreme Programming

User explains the stories as scenarios called as *user stories*. The stories are then translated as tasks and are completed one at a time.

### SCRUM

This is also an agile methodology where there are short sprints of 3 to 4 weeks and a full product is developed within a single sprint. The *SCRUM master* leads the project and meetings are held on a daily basis.

___

## Requirement analysis

#### Types of requirements

- User requirements
- System requirements
- Stakeholders

Based on functionality

- Functional requirements
- Non Functional requirements
  - Product requirements
  - Organizational requirements
  - External requirements
    Metrics for measuring non-functional requirements
    - Speed 
    - Size
    - Ease of use
    - Reliability
    - Robustness
    - Portability

## Requirements Engineering

1. Feasibility study
   - Technical feasibility
   - Operational feasibility
   - Legal feasibility
   - Schedule feasibility

2. Requirement elicitation and analysis
   - Interviewing
   - Observation and Ethnography 
   - Scenarios
   - Use cases
   - Questionnaires
   - Survey
   - Existing manuals and documentation
   - Group discussion
   - Prototyping

3. Requirement specification
   - Documentation of user and system specifications.
   - It can be done as:
     - Natural Language Specification
     - Structured specification
     - Graphical notations
     - Mathematical specifications
       The official document that specifies sofware requirements is called as the **SRS** **document**. It is used by customers, managers, system engineers, system test engineers, system maintainence engineers.
       
       A good SRS document is concise, complete, correct, consistent, unambiguous, structured,verifiable, modifiable.
   
   - Specifications of SRS by IEEE

---

1. Introduction
  1. Purpose
  2. Project scope
  3. Definitions, acronyms and abbreviations
  4. Reference
  5. Overview

2. Overall Descriptive
  1. Product perspective
  2. Product features
  3. User classes
  4. Operating environment
  5. Design and implementation constraints
  6. User documentation
  7. Assumptions and Dependencies

3. Specific requirements
  1. Functional requirements

4. External interface requirements
  1. User
  2. Hardware
  3. Software
  4. Communication

5. Other non-functional requirements

6. Other requirements

---

4. Requirement verification and validation
5. Requirements management

## Tools for requirement gathering

### Decision table

| Conditions  | Condition entries  |
| ----------- | ------------------ |
| **Actions** | **Action entries** |

### Decision tree

### Data flow diagram

A representation of how data flows and is stores in a system; Useful for data analysts, DBAs and end users

### Data dictionary

| Entry              | Value |
| ------------------ | ----- |
| Name of item       | ----  |
| Alias              | ----  |
| Description        | ----  |
| Related data items | ----  |
| Range of values    | ----  |

---

## Software Design

- Preliminary / high level design
- Detailed design
- Following items are designed during design phase
  - Modules
  - Control relationship among identified modules
  - Interfaces among the modules
  - Data structure of individual module
  - Algorithm to implement each module

- Characteristics of good software design
  - Correct
  - Understandable
  - Efficient
  - Maintainable
  - Complete
  - Consistent
  

### Software design principles

- Problem partitioning
- Increase abstraction
- Modularity
- Increase cohesion
- Reduce coupling
- Increase reusability
- Design for flexibility
- Portability
- Testability


  **Types of coupling**

  - Data coupling
  - Stamp coupling
  - Control coupling
  - External coupling
  - Common coupling
  - Content coupling

  **Types of cohesion**

  - Functional
  - Sequential
  - Communicational
  - Procedural
  - Temporal
  - Logical
  - Coincidental


### Software design methodology

- Level oriented software design
  - Top down - Go into more depth, keep breaking down the system into smaller chunks. Used when design is to be done ground up.
  - Bottom up - Lowest level subsystems are designed first

- Function oriented
  - Design of data flow
  - Structure division
  - Detailed design

- Object oriented software design approach
  
  - ER model
  - Decision tree
  - DFD
  - Structure charts

### DFDs and Structre charts

- 0-level DFD or context diagram
  - Has single process for main task and its relationship with external entities.
- 1-Level DFD
  - More than 1 process/bubble. The major process is highlighted and is further divided into subprocesses.
- 2 level DFD
  - The data flow is also shown along with the processes. 



### Functional independence

A module with high cohesion and low coupling is called as functionally independent of other modules. Functional independence is required because:
- Error isolation
- Scope of reuse
- Understandability
  
  

### Modularity

- Easy to understand the system
- System maintainence is easy
- Reusability
  

### Detailed design

- Short description of each function is provided in a tablula r format

## Design and Development

- **UML diagram** (Unified modelling language) - Show design of the system
- **Context model** - Show the scope of the system
- **Interaction modelling** - Show the user interface of the system
- **Use case diagram** - The actions to be performed by particular users on an entity
- **Sequence diagram** - Communication of entities based on time sequence
- **Structured model** - Show structure of model with relation among the components
- **Class diagram** - Shows class, attribute, function and inter-relationship
- **Behavioral diagram** - Show the behavior of an entity when an action is performed

### Architectural design

The organization and design of overall structure of a system is specified in architectural design. It is the starting stage of software design process. Link between requirement and design is specified at this stage. Non functional requirements are given utmost importance.

**Advantages**

- Stakeholder communication
- System analysis
- Large scale reuse

**Architectural views**

- Logical view
- Physical view
- Development view
- Process view

**Types of architectures**

- Layered
- Repository
- Client server
- Pipe and filter

# Development

- Selection of language

- Focus on reusability

- Configuration management

  - Version managemen
  - System integration
  - Problem tracking

- Host target development

- Coding

  - Modular
  - Notation / Comments
  - Portability
  - Debugging
  - Size of code
  - Cost of code

- Documentation

  - Introduction in README
  - Explain return values, parameters etc.
  - Naming convention for files
  - Names of contributors
  - License
  - Roles of developers / Contact
  - Version

- Code review

  - Are requirements covered ?
  - Is software design consistent ?
  - Is it a standard coding style ?
  - Are enough test cases generated ?
  - Is documentation complete ?
  - Major drawbacks / flaws
    **Types of code reviews**

    - Code walkthrough 
    - Code inspection

# Testing

## Objectives of testing

- To find situations where software may malfunction (Verification) - "Are we making the product right ?"
- Show clients that software meets provided specifications (Validation) - "Are we making right product ?"

## Stages of software testing

- Development testing
  - Unit testing
  - Component testing
  - Integration testing
    - Top Down
    - Bottom Up
    - Mixed 
    - Bing-Bang
- Release testing / Functional testing
  - Requirement based
  - Scenario based
  - Performance based
    - Speed 
    - Scalability
    - Stability
    - Compatibility
    - Volume
    - Recovery
    - Maintenance
    - Documentation
  - Regression based
    - When existing system is upgraded
- User testing

# Maintenance

**Need to maintain**

- Fix the errors
- Business status change / User expectaions
- Software evolution
- Migration of legacy software

**Types of maintenance**

- Corrective
- Adaptive
- Perfective
- Preventive

**Reverse Engineering**

- Functionality is not changed, complex statements are simplified (Cosmetic changes)

- Complete code analysis, their modules and interfaces are understood, design is extracted, SRS is generated based on design

  **Benefits of reverse engineering**

  - Understanding the complexity
  - Find side effects
  - Recover lost information
  - Create new products
  - Explore reusability

## Software maintenance Process Model 1

- For small changes
- Few team members gather info, and formulate changes

## Software maintenance Process Model 2

- More rework is needed
- Combine reverse and forward engineering
- Called as software re-engineering
- Helps in software evolution
- Useful in Legacy software migration
- Reduces risk and cost of development

## maintenance

- COCOMO - Boehm
- Based on ACT (Annual change traffic)
$$
ACT = \frac{KLOC_{added}+KLOC_{deleted}}{KLOC_{total}}
$$

- **Factors affecting cost**
  - Technical (Changes in modules, programming languages, style etc.)
  - Non-technical (Scope, Stable team, Hardware, environment)

## Configuration management

**Release** - Minor change

**Version** - Major change

**Software configuration management process**

- Identification of the objects to be configured
- Controlling versions
- Controlling changes
- Audit configurations
- Generating status report

# CASE

- Computer aided software engineering
- Automated support in software engineering
- CASE tools for Structured analysis - Flow chart maker
- CASE tools for code generation - Code completion
- CASE tools for test case generation - SoapTest

## CASE tools classification

- Upper CASE tools
- Lower CASE tools
- Integrated CASE tools

## Project Management

**Duties of project manager**

- Project planning
- Reporting
- Risk management
- People management
- Proposal writing


## SPMP Document

| Name              | Details                                              |
| ----------------- | ---------------------------------------------------- |
| Introduction      | Objective, Functions, Performance issues, Constrains |
| Project estimates | Historical data, Cost duration, Effort estimates     |
| Project schedule  | Work breakdown using Gantt and PERT chart            |
| Project resource  | Manpower, Hardware, Software, Skills                 |

## Project Size allocation

- **LOC - Lines of code**

$$
LOC = \frac{S_{opt} + 4S_{m} + S_{pess}}{6}
$$

$$
\text{Productivity rate} = \frac{size}{effort}
$$

Example:
- Let number of men = 2
  LOC = 4800\\
  $$
  \text{Productivity rate} = \frac{4800}{men*12} LOC/man/month
  $$

- **FP - Functional point**
  - AFP = UFP $\times$ CAF\\
    AFP = Adjusted Functional Points\\
    UFP = Unadjusted Functional Points\\
    CAF = Complexity Adjustment Factor

## Project Estimation Techniques

- **Empirical**

  - Experts extimate the cost
  - Human judgement / errors / bias

- **Heuristic**

  - Technique 1
    - $\text{Estimated parameter} = c_{1}\times e^{d_{1}}\\$
    - $c_1$ and $d_1$ are constants determined from previous projects
    - $e$ is the estimate

  - Technique 2
    - $\text{Estimated parameter} = c_{1}\times e^{d_{1}}\ * c_{2}\times e^{d_{2}}...$
    - $c_1$ and $d_1$ are constants determined from previous projects
    - $e$ is the estimate

- **Analytical**

  - Halstead's Software science
  - Considers the following points
    - Length and vocabulary
    - Program volume
    - Potential minimum volume
    - Program level
    - Effort
    - Time

## COCOMO

Constructive Cost Model - Falls under Heuristic approach

### COCOMO - Basic

- Based on LOC

- Software projects can be divided as

  - Organic - Well understood, small team, good experience (2 kloc - 50 kloc)
  - Semi Detached - Mixture of experienced and unexperienced people (50 kloc - 300 kloc)
  - Embedded - Strongly connected and complex hardware (> 300 kloc)

$$
\text{Effort} = a_{1}\times (kloc)^{a_{2}} \text{person month}\\
T_{dev} = b_{1}\times\text{Effort}^{b_{2}} \text{months}
$$

a$ and $b$ are constants

### COCOMO - Intermediate

Attributes of COCOMO intermediate

- Product
- Personnel
- Computer
- Development environment

These factors determine **EAF - Effort Adjustment Factor** 

### COCOMO - Complete

- Planning and requirement
- System design
- Detailed design
- Module cost and test
- Integration and test
- Cost constructive model

# Risk management

![image-20220603083607424](C:\Users\hnegi\AppData\Roaming\Typora\typora-user-images\image-20220603083607424.png)

# Reliability

### Reliability metrics

- ROCOF - Rate of occurrence of failure
- Behavior of software over time
- MTTF - Mean time to failure (Duration to track and fix an error)
- MTTR - Mean time to repair
- MTBR - Mean time between repair (MTTR + MTTF)
- POFOD - Probability of failure on demand
- Availability

### Types of failure

- Transient - Due to certain input values
- Permanent - All input values
- Recoverable - Can recover without manual help
- Unrecoverable - Needs to be restarted
- Cosmetic - Minor failures

# ISO 9000

**International Standards Organization**

Provides guidelines to maintain ISO certification. Is not concerned with the product itself.

### ISO 9001

- Design, development, product and servicing of product use this standard

### ISO 9002

- For companies not involved in design, but in production

### ISO 9003

- Only for companies involved in installation and testing


---

# Contributors

- [@Bot-70370](https://github.com/Bot-7037)
