---
layout: default
use_math: true
---
# Finding Unit Digit

## General Method

- given $n$ find $n \mod 10$


## Some general numbers

- 2
  - given $2^n$, represent $n$ as $n=4k + x$, cycle = $\{2, 4, 8, 6\}$
  - $2^1 \equiv 2 \mod 10$, $2^5 \equiv 2 \mod 10$, for $n = 4k + 1$
  - $2^2 \equiv 4 \mod 10$, $2^6 \equiv 4 \mod 10$, for $n = 4k + 2$
  - $2^3 \equiv 8 \mod 10$, $2^7 \equiv 8 \mod 10$, for $n = 4k + 3$
  - $2^4 \equiv 6 \mod 10$, $2^8 \equiv 6 \mod 10$, for $n = 4k$

- 3
  - given $3^n$, represent $n$ as $n=4k + x$, cycle = $\{3, 9, 7, 1\}$
  - $3^1 \equiv 3 \mod 10$, $2^5 \equiv 3 \mod 10$, for $n = 4k + 1$
  - $3^2 \equiv 9 \mod 10$, $2^6 \equiv 9 \mod 10$, for $n = 4k + 2$
  - $3^3 \equiv 7 \mod 10$, $2^7 \equiv 7 \mod 10$, for $n = 4k + 3$
  - $3^4 \equiv 1 \mod 10$, $2^8 \equiv 1 \mod 10$, for $n = 4k$ 

- 4
  - represent 4 as $2^2$, cycle $\{4,6\}$
  - $4^1 \equiv 4 \mod 10$, $4^3 \equiv 4 \mod 10$, for $n = 2k + 1$
  - $4^2 \equiv 6 \mod 10$, $4^4 \equiv 6 \mod 10$, for $n = 2k$
  - so we do $\mod 2$ of the power

- 5 
  - given $5^n$
  - $5^n \equiv 5 \mod 10$

- 6
  - given $6^n$
  - $6^n \equiv 6 \mod 10$

- 7
  - given $7^n$, represent $n$ as $n=4k + x$, cycle = $\{7, 9, 3, 1\}$
  - $7^1 \equiv 7 \mod 10$, $7^5 \equiv 7 \mod 10$, for $n = 4k + 1$
  - $7^2 \equiv 9 \mod 10$, $7^6 \equiv 9 \mod 10$, for $n = 4k + 2$
  - $7^3 \equiv 3 \mod 10$, $7^7 \equiv 3 \mod 10$, for $n = 4k + 3$
  - $7^4 \equiv 1 \mod 10$, $7^8 \equiv 1 \mod 10$, for $n = 4k$ 

- 8
  - $2^3$, cycle $\{8, 4, 2, 6\}$

- 9
  - $3^2$, cycle $\{9, 1\}$

- 10
  - 0

- $a>10$
  - $a^n \equiv (a-10k)^n \mod 10$, i.e. reduce the no. to a no. $<=10$

- for $2,3,7$ we have to do $\mod 4$ of the power, because of cycle length of $4$
- also, if $\mod 4$ is $0$, we put $4$ instead to generalize procedure for $2$
  - $3^4 \equiv 1 \mod 10$ and $3^0 \equiv 1 \mod 10$
  - $7^4 \equiv 1 \mod 10$ and $7^0 \equiv 1 \mod 10$
  - $2^4 \equiv 6 \mod 10$ but $2^0 \equiv 1 \mod 10$, 
  - so to generalize for $2$ we say put $4$ instead of $0$


## Some questions

Find unit digit of $7^{105}$?

- $7^{105} \mod 10$
- $7^{105 \mod 4} \mod 10$
- $7^{(100 + 5) \mod 4} \mod 10$
- $7^{5 \mod 4} \mod 10$
- $7^{1 \mod 4} \mod 10$
- $7 \mod 10$
- $7$

Find the unit digit of $3^{69} \times 6^{59} \times 7^{71}$?

- $3^{69} \times 6^{59} \times 7^{71} \mod 10$
- $3^{69} \times (3*2)^{59} \times 7^{71} \mod 10$
- $3^{69} \times (3*2)^{59} \times 7^{71} \mod 10$
- $3^{69+59} \times 2^{59} \times 7^{71} \mod 10$
- $3^{69+59 \mod 4} \times 2^{59 \mod 4} \times 7^{71 \mod 4} \mod 10$
- $3^{1+3 \mod 4} \times 2^{3} \times 7^{3} \mod 10$
- $3^{4} \times 2^{3} \times 7^{3} \mod 10$, when found mod as 0 put 4 instead
- $1 \times 8 \times 3 \mod 10$
- $24 \mod 10$
- $4$

Find the unit digit of $13^{13^{13}}$?

- $13^{13^{13}} \mod 10$
- $3^{13^{13}} \mod 10$
- $3^{13^{13} \mod 4} \mod 10$
- $3^{1^{13} \mod 4} \mod 10$
- $3^{1} \mod 10$
- $3$

Find the unit digit of $13^{14^{15^{16}}}$

- $13^{14^{15^{16}}} \mod 10$
- $3^{14^{15^{16}}} \mod 10$
- $3^{14^{15^{16}} \mod 4} \mod 10$
- $3^{2^{15^{16}} \mod 4} \mod 10$
- $3^{2^{15^{16}} \mod 4} \mod 10$, 
  - note that $2^n \equiv 0 \mod 4$, if $n>1$
- $3^{4} \mod 10$
- $1$

Find the unit digit of $12^{13^{14^{15}}}$

- $12^{13^{14^{15}}} \mod 10$
- $2^{13^{14^{15}}} \mod 10$
- $2^{13^{14^{15}} \mod 4} \mod 10$
- $2^{1^{14^{15}} \mod 4} \mod 10$
- $2 \mod 10$
- $2$

[relevant](https://www.quora.com/How-do-I-find-Unit-digit-of-12-13-14-15)