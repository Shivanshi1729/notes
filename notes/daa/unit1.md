---
layout: default
title: Unit I
parent: Design and Analysis of Algorithms
mathjax: true
mermaid: true
---

# Unit I

- Asymptotic Notations and Searching Algorithms 
  - Introduction to Algorithms
  - What is an Algorithm, 
  - Rate of growth, 
  - Commonly used rate of growths, 
  - Types of analysis, 
  - Asymptotic Notations, 
  - Master theorem 
- Searching
  - Linear search (sorted and unsorted), 
  - Iterative and recursive binary search, 
  - Tower of Hanoi and solving its recursion, 
  - Fibonacci and solving its recursion

## What are algorithms?

Informally - a set of rules that precisely defines a sequence of operations.

Formally algorithm can be considered to be any sequence of operations that can be simulated by a 
Turing-complete system

### How to write algorithms?

- Use flowcharts
- Use pseudocode or pidgin code

> Pseudocode is a plain language desctiption of the steps in an algorithm or another system.
> Pidgin code is a mixture of several programming languages in the same program, or pseudocode 
> that is a mixture of a programming language with natural language descriptions. 

## Analysis of Algorithms

this includes
- finding the computational complexity of the algorithms
- the amount of time, space, and other resources needed to execute the algorithm
- finding the best, worst, avg case computational complexity
- finding space complexity, time complexity

## Rate of growth of algorithms?

- growth rate of an algorithm is the rate at which the cost of the algorithm grows as the size of the input grows.

## Asymptotic Notations

- used to estimate complexity function for arbitrary large inputs.

types

- big O notation - this means the function is bounded at upper end by the function scaled to some factor
- big omega notataion - this is used to find a function which bound the function at lower end
- big theta notation - this bound the function at both end
- small o notation - this bound the function at upper end

### big o notation 

- describes the limiting behaviour of a function when arguments tends towards a particular value or infinity.


## Master theorem

- used to find time complexity in case of divide and conquer algorithms

Given a divide and conquer algo, which divides the problem into   $a$   sub problems and reduced the problem size by factor $b$.
Then we can form a recurrence relation like this

$$T(n) = aT\left(\frac{n}{b}\right) + f(n)$$

where,  

- $T(N)$ time taken by algorithm for input of size n
- $f(n)$ denotes total time taken at top leven recurrence
- $a$ number of problems in the recurrence
- $b$ factor by which subproblem size is reduced in each recursive call
- assumption 
  - $T(n) = \Theta(1)$ where n is less then some bound value $k > 0$
  - $k$ is the smallest value that will lead to recursion

\newpage

Solving the equation three cases arise

- work to split/recombine problem $<$ subproblems
- work to split/recombine problem $\approx$ subproblems
- work to split/recombine problem $>$ subproblems

a value $c_{\operatorname{crit}}$ is calculated which help us to decide case in which the problem belongs.

$$c_{\operatorname{crit}} = \log_b(a) = \frac{\log(a)}{\log(b)}$$


- **case 1:** work to split/recombine problem $<$ subproblems
  - $f(n)=O(n^{c})$
  - $c<c_{\operatorname {crit}}$
  - **sol:** $T(n)=\Theta \left(n^{c_{\operatorname {crit} }}\right)$
- **case 2:** work to split/recombine problem $\approx$ subproblems
  - $f(n)=\Theta (n^{c_{\operatorname {crit} }}\log^{k}n)$
    - subcase 1:
      - $k>-1$ 
      - **sol:** $T(n)=\Theta \left(n^{c_{\operatorname {crit} }}\log ^{k+1}n\right)$
    - subcase 2:
      - $k=-1$
      - **sol:** $T(n)=\Theta \left(n^{c_{\operatorname {crit} }}\log \log n\right)$
    - subcase 3:
      - $k<-1$
      - **sol:** $T(n)=\Theta \left(n^{c_{\operatorname {crit} }}\right)$
- **case 3:** work to split/recombine problem $>$ subproblems
  - $f(n)=\Omega (n^{c})$
  - $c>c_{\operatorname {crit} }$
  - if $af\left({\frac {n}{b}}\right)\leq kf(n)$ for some $k<1$ and large $n$ then total is dominated by $f(n)$
    - $T\left(n\right)=\Theta \left(f(n)\right)$


# Searching

## linear search

- search one by one
- time complexity - $O(n)$

## binary search

- can be applied on sorted array

algo: (for sorted array in ascending order)

- check the middle element 
- if it is same element -> then match found
- if middle element is smaller -> then the element is in the upper half
- else it is in the lower half

## tower of handoi

**Desirption of problem:** You have three rods, and some disks of varying diameter.
You put the disks in increasing order of diameter in one of the rod to form a tower. 
Your task is to move the the tower form one rod to another in minimum moves following simple rules,

- Only one disk can be moved at a time
- Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
- No disk may be placed on top of a disk that is smaller than it

Simple illustration:

```
      |         |         | 
     *|*        |         |
    **|**       |         |  
   ***|***      |         | 
---=======---=======---=======---
  
      |         |         | 
      |         |         |
    **|**       |         |  
   ***|***     *|*        | 
---=======---=======---=======---
  
      |         |         | 
      |         |         |
      |         |         |  
   ***|***     *|*      **|**
---=======---=======---=======---
  
      |         |         | 
      |         |         |
      |         |        *|* 
   ***|***      |       **|**
---=======---=======---=======---
  
      |         |         | 
      |         |         |
      |         |        *|* 
      |      ***|***    **|**
---=======---=======---=======---
  
      |         |         | 
      |         |         |
      |         |         |  
     *|*     ***|***    **|**
---=======---=======---=======---
  
      |         |         | 
      |         |         |
      |       **|**       |  
     *|*     ***|***      |  
---=======---=======---=======---
  
      |         |         | 
      |        *|*        |
      |       **|**       |  
      |      ***|***      |  
---=======---=======---=======---
```
  
### solution

recursive solution is the simplest one. 

- three rods, namely
  - source - where the tower is
  - target - where you want to move the tower
  - auxillary - the ramaining one
- n - number of disks 

**sol:** to move n sized tower form source to target, move (n-1) sized tower to 
the auzillary rod then, move to last disk to target and them move the (n-1) sized
tower to to target. base case happen when we have n=1, then you actually move the 
disk instead of recursive calling.

```py
A = [3, 2, 1] # rod A, contains 3,2,1 sized disk
B = []        # rod B
C = []        # rod C

def move(n, source, target, auxiliary):
    if n > 0:
        # Move n - 1 disks from source to auxiliary, 
        # so they are out of the way
        move(n - 1, source, auxiliary, target)

        # Move the nth disk from source to target
        target.append(source.pop())

        # Display our progress
        print(A, B, C, '--------', sep='\n')

        # Move the n - 1 disks that we left on 
        # auxiliary onto target
        move(n - 1, auxiliary, target, source)

# Initiate call from source A to target C with auxiliary B
move(3, A, C, B)
```


## Fibonacci series

- nth term is sum of n-1 th term and n-2 th term

```c
int fibonacii(n){
  if(n>0 && n <2) return n;
  else return fibonacii(n-1) + fibonacii(n-2);
} 
```