---
layout: default
---

# compiler design

- [tutorial point]
- [gfg]
- [jp]
- [nptl videos]

## introduction

- compilers for c
  - gcc
  - llvm

- lexical parsers
  - (bison)[https://en.wikipedia.org/wiki/GNU_Bison]
    - uses BNF notation (a context free language)
  - yacc - yet another compiler compiler
  - lex - used for lexical analysis
  - flex - another version of the lex tool, which is open source

[tutorial point]: https://www.tutorialspoint.com/compiler_design/index.htm
[gfg]: https://www.geeksforgeeks.org/introduction-of-compiler-design/
[jp]: https://www.javatpoint.com/compiler-tutorial
[nptl videos]: https://www.youtube.com/watch?v=7Nb-NTGbe-Q&list=PLbRMhDVUMngcseCW7wXDvtTDemCuH80fP&index=3

## videos

- lecture1: https://www.youtube.com/watch?v=4UTwY90pvwk
- lecture2: https://www.youtube.com/watch?v=tJeXvkxS4Dw
- Phases of compiler: https://www.youtube.com/watch?v=hJ27wIAjY9k
- Lexical analysis: https://www.youtube.com/watch?v=l_I51kjh2Cc
- Passes in gcc: https://www.youtube.com/watch?v=geSNUl7Gnpw
- Cross Compiler: https://www.youtube.com/watch?v=KeYG-lLDXUM
- Compiler Construction tools: https://www.youtube.com/watch?v=3IhR4_pCeMQ
- Lex: https://www.youtube.com/watch?v=AnATyNsKfaA
- Lexical Analysis Generator: https://www.youtube.com/watch?v=JZ9ffLYRWy4
- Parsing: https://www.youtube.com/watch?v=hCdO5DneKGU
- Types of Parsing: 
- Recursive Descent Parsing: 
- Example: 
- Predictive Parsing: 
- Calculation of first: 

## compile vs interpreters

### compiler

- scans the entire program and translates the entire program into target code
- take time to analyze the source code - overall execution is faster than interpreters
- generate the intermediate object code which require further linking - hence more memory
- debugging is hard 
- e.g. - c cpp c# 

### interpreters

- line by line execution
- less time to analyze the source code - overall execution time is more than compilers
- no intermediate code is generates - so less memory needed
- better error diagnostics 
- e.g. - javascript, python, 

## compiler generate three types of code

- pure machine code - 
  - for embedded applications
  - doesn't assume existence of any machine code
- 

## phases of compiler


## Lexical analysis

## Passes of Compiler

## Passes of GCC

## Compiler Construction Tools

## Parsing

## Types of Parsing

## Recursive Descent Parsing

## Predictive Parsing

## Calculation of First

## Calculation of Follow

