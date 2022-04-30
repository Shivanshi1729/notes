---
layout: default
use_math: true
---
# Factors

## Number of factors of a number

- given number $n$, represent it in prime factors (prime factorization)
- $n = a^p b^q c^r ...$
- $a, b, c$ are prime numbers, and $p, q, r$ are positive numbers
- then total factors are 
- $f(n) = (p+1)(q+1)(r+1)...$ where $f(n)$ gives is number of 
  factors in $n$

## Products of factors of a number

- $g(n) = n^{f(n)/2}$, $f(n)$ is number of factors of $n$

## Number of ways of expressing a number as product of two numbers

- given, $n$ and its prime factorization $a^p b^q c^r...$
- $f(n) = (p+1)(q+1)(r+1)...$
- $F(n) = \frac{1}{2}f(n)$, 
  - is not possible when $f(n)$ is odd
  - if, $p, q, r,...$ are all even then $n$ is a prefect square
    - that means that $\sqrt{n}$ is a whole no.
    - therefore $F(n) = \frac{1}{2}f(n) - 1$, 
      $\sqrt{n} \times \sqrt{n}$ is not counted

## Sum of all factors of a number

- given, $n$ and its prime factorization $a^p b^q c^r...$
- sum is 

$$\frac{a^{p+1} - 1}{a-1} \frac{b^{q+1} - 1}{b-1} \frac{c^{r+1} - 1}{c-1} ...$$

## Number of ways of writing a number as product of two co-primes

- **co-primes** - there gcd (hcf) is 1
- given, $n$ and its prime factorization $a^p b^q c^r...$
- $n(\{a, b, c, ...\}) = x$, i.e. no of unique prime in prime factorization is $x$
- then, total no of co-primes are $2^{x-1}$

## Number of coprimes to $n$ that are less than $n$

- given, $n$ and its prime factorization $a^p b^q c^r...$
- then, 

$$\phi(n) = n\Big(1-\frac{1}{a}\Big) \Big(1-\frac{1}{b} \Big) \Big(1-\frac{1}{c}\Big)$$

### Number of coprimes to $n$ that are less than $n$

- $\frac{n}{2} \times \phi(n)$


# General method to find no of factors

## number of factors

- given number $n$
- represent it in prime factorization $a^p b^q c^r...$
- so, $a$ can acquire powers $\{0, 1, 2, ..., p\}$, $n(\{0, 1, 2, ..., p\}) = p+1$
- so, $b$ can acquire powers $\{0, 1, 2, ..., q\}$, $n(\{0, 1, 2, ..., p\}) = q+1$
- so, $c$ can acquire powers $\{0, 1, 2, ..., r\}$, $n(\{0, 1, 2, ..., p\}) = r+1$
- and so on, here $n(\text{A})$ is to represent the cardinality of set $\text{A}$
- so total no. of factors are $(p+1)(q+1)(r+1)$

## number of factors which are even

- should have at least one 2
- given number $n$
- represent it in prime factorization $2^p b^q c^r...$
- so, $a$ can acquire powers $\{1, 2, ..., p\}$, $n(\{1, 2, ..., p\}) = p$
- so, $b$ can acquire powers $\{0, 1, 2, ..., q\}$, $n(\{0, 1, 2, ..., p\}) = q+1$
- so, $c$ can acquire powers $\{0, 1, 2, ..., r\}$, $n(\{0, 1, 2, ..., p\}) = r+1$
- and so on, here $n(\text{A})$ is to represent the cardinality of set $\text{A}$
- so total no. of even factors are $(p)(q+1)(r+1)$

## number of factors which are perfect square

- given number $n$
- represent it in prime factorization $a^p b^q c^r...$
- so, $a$ can acquire powers $\{0, 2, 4, ..., p\}$, 
  $n(\{0, 1, 2, ..., p\}) = \lceil{\frac{p+1}{2}}\rceil$
- so, $b$ can acquire powers $\{0, 2, 4, ..., q\}$, 
  $n(\{0, 1, 2, ..., p\}) = \lceil{\frac{q+1}{2}}\rceil$
- so, $c$ can acquire powers $\{0, 2, 4, ..., r\}$, 
  $n(\{0, 1, 2, ..., p\}) = \lceil{\frac{r+1}{2}}\rceil$
- and so on, here $n(\text{A})$ is to represent the cardinality of set $\text{A}$
- so total no. of factors are 

$$\lceil{\frac{p+1}{2}}\rceil \lceil{\frac{q+1}{2}}\rceil \lceil{\frac{r+1}{2}}\rceil$$

## number of factors of $n$ and $m$ that are common

- $n = a^p b^q c^r...$
- $m = a^l b^m c^n...$
- total no of common factors are 
  $(\min(p, l) + 1) \times (\min(q, m) + 1) \times (\min(r, m) + 1) ...$