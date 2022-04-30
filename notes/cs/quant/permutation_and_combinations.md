---
layout: default
use_math: true
---

# Combinations

$$
C^n_r = \frac{n!}{r!(n-r)!}
$$

- no of handshakes
  - $n$ people in the room
  - everyone shakes hand with everyone else
  - sol. $C^n_2$
- no of matches
  - $n$ teams
  - every team play one match with every other team
  - sol. $C^n_2$
- no of line
  - $n$ points in a plane
  - no three points are in straight line
  - sol. $C^n_2$
- no of line
  - $n$ points in a plane
  - $m$ points are collinear and already in straight line
  - sol. $C^n_2 - C^m_2 + 1$
  - sol. $C^{n-m}_2 + m(n-m) + 1$
- no of diagonals
  - $n$ vertices of a regular polygon
  - sol. $C^n_2 - n$
- no of square and rectangle
  - a $n \times m$ grid
  - for rec we need 2 horizontal and 2 vertical lines
  - no of rectangles - $C^n_2 \times C^m_2$
  - no of squares - $1^2 + 2^2 + 3^2 + ... + \text{min}(n, m)^2$

Total no of combinations of things taken 0 at a time or some or all at a time $2^n$

# Permutations

$$
P^n_r = \frac{n!}{(n-r)!}
$$

- no of permutations of $n$ things taken all at a time where
  $p$ things are identical and $q$ things are identical
  $$
  \frac{n!}{p!q!}
  $$
- $n$ identical things to be distributed to $r$ boxes,
  no of ways 
  $$
  C^{n+r-1}_{r-1}
  $$
  Same as lining all the $n+r-1$ items and the selecting 
  $r-1$ and remove them, which will give you $r$ partitions.