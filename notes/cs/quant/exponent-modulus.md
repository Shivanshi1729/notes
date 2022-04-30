---
layout: default
use_math: true
---
# Exponent of any modulus

## general

- find the value of

$$a^b \mod c$$

- find the cycle length, let it be $l$
- then $a^{b \mod l} \mod c$ is the sol.


## examples

$$
5^{123} \mod 7
$$

- $5^{123} \mod 7$
- use fermat theorem, $a^{p-1} \equiv 1 \mod p$, for prime $p$
- so cycle length is 6
- $5^{123 \mod 6} \mod 7$
- $5^3 \mod 7$
- $25*5 \mod 7$
- $4*5 \mod 7$
- $20 \mod 7$
- $6$

---

$$
2^{34} \mod 5
$$

- $2^{34} \mod 5$
- $2^{34 \mod 4} \mod 5$
- $2^{2} \mod 5$
- $4$

---

$$
60^{60} \mod 11
$$

- $60^{60} \mod 11$
- $5^{60 \mod 10} \mod 11$
- $5^{10} \mod 11$
- $1$

---

$$
83^{1002} \mod 39
$$

- $83^{1002} \mod 39$
- $5^{1002} \mod 39$
- find cycle length
- $5^{1} \equiv 5 \mod 39$
- $5^{2} \equiv 25 \mod 39$
- $5^{3} \equiv 8 \mod 39$
- $5^{4} \equiv 1 \mod 39$
- so 4 
- $5^{1002 \mod 4} \mod 39$
- $5^{2} \mod 39$
- $25$