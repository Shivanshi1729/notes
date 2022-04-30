---
layout: default
use_math: true
---
# Finding the last two digits

## General Method 

- $x^n \mod 100$

## for numbers ending with 1

- give no. $(100x_3 + 10x_2 + 1)^{(100n_3 + 10n_2 + n_1)}$,
- $0<=x_2<=9$, $0<=n_2<=9$, $0<=n_1<=9$

$$
(100x_3 + 10x_2 + 1)^{(100n_3 + 10n_2 + n_1)} 
\equiv
(10n_1x_2 + 1)
\mod 100
$$

### proof:

-  $(100x_3 + 10x_2 + 1)^{(100n_3 + 10n_2 + n_1)} \mod 100$
-  $(10x_2 + 1)^{(100n_3 + 10n_2 + n_1)} \mod 100$
-  let $100n_3 + 10n_2 + n_1 = n$
-  $(10x_2 + 1)^{n} \mod 100$
-  use binomial expansion
-  $1 + C_1^n(10x_2) + C_2^n(10x_2)^2 + ... + (10x_2)^n \mod 100$
-  $(10x_i)^a \equiv 0 \mod 100$, for $a >=2$
-  $1 + 10nx_2 \mod 100$
-  $1 + 10((100n_3 + 10n_2 + n_1)x_2 \mod 100$
-  $1 + (1000n_3 + 100n_2 + 10n_1)x_2 \mod 100$
-  $1 + 10n_1x_2 \mod 100$
-  $\blacksquare$

## for numbers ending with 3, 7, 9

- convert to number ending with 1
- because there cycle contains 1
- for 3, and 7 calculate to power 4 to reach 1
- for 9 to power 2

## for number ending with 2

- cycle repeats for last two digits $2^10$
- $(2^{10})^2 \mod 100 = 76$ also  $(2^{10})^{2n} \mod 100 = 76$
- $(2^{10})^1 \mod 100 = 24$ also  $(2^{10})^{2n+1} \mod 100 = 24$
- so convert it in this form, and for less than this compute manually

## for number ending with 4 and 6 ans 8

- split no as $2^n*x$ and then solve

## for no ending the 5

- 25

## for no ending with 0

- if power is $>2, 0$