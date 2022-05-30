---
layout: default
title: Modular Arithmetic
parent: Reasoning
mathjax: true
---

# Modular arithmetic

## Formulas

- $a \equiv (a-p) \mod p$
- $a \equiv (a+np) \mod p$, $n \in \text{Z}$
- $a \equiv b \mod p \implies a - k \equiv b - k \mod p$
- $a_1 \equiv b_1 \mod p$ and $a_2 \equiv b_2 \mod p$, then
  - $a_1 + a_2 \equiv b_1 + b_2 \mod p$
  - $a_1 - a_2 \equiv b_1 - b_2 \mod p$
  - $a_1 \times a_2 \equiv b_1 \times b_2 \mod p$
- $(ab) \mod p = ((a \mod p)(b \mod p))\mod p$
- $(a+b) \mod p = ((a \mod p) + (b \mod p))\mod p$

### Fermat little theorem

Given, a no. $a$ and a prime no. $p$, 

$$ a^{p-1} \equiv 1 \mod p$$

Implications:

- for a prime $p$ and no. $a$ there will always a cycle formed
  if we keep on doing $a^n$, $n \in \text{Z+}$
  - e.g. $p = 7, a = 3$
  - $3^1 \equiv 3 \mod 7$
  - $3^2 \equiv 2 \mod 7$
  - $3^3 \equiv 6 \mod 7$
  - $3^4 \equiv 4 \mod 7$
  - $3^5 \equiv 5 \mod 7$
  - $3^6 \equiv 1 \mod 7$, fermat theorem so now cycle repeat
  - $3^7 \equiv 3 \mod 7$, as $3^7 = 3^6 \times 3$ and $3^6 \equiv 1 \mod 7$
    so cycle repeats

### Euler's Theorem

Given no $a$ and $b$, and $a$ and $b$ are co-primes

$$a^{\phi(b)} \equiv 1 \mod b$$

- $\phi(b)$ is equal to number of positive integers till $b$ that are relative
  prime to $b$, also called Euler's totient function.
- more formally,
  $\phi(n) = n(\{x:x \in \{1,2,...,n\} \text{ and } \gcd(x, n) = 1\})$

Implications
- $a=3, b=10$, and 10, 3 are co-prime, 
  - $\phi(10) = 4$ as pairs are $\{(1,10), (3, 10), (7,10), (9,10)\}$
  - $3^4 \equiv 1 \mod 10$, euler theorem
  - so 3 power will also form a cycle of 4 with 10

### Wilson's theorem

Given a prime no $a$,

$$(a-1)! \equiv -1 \mod a$$

- $1! = -1 \mod 2$
- $2! = -1 \mod 3$
- $4! = -1 \mod 5$
- $6! = -1 \mod 7$
- $12! = -1 \mod 13$
