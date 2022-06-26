---
layout: default
title: Unit I
parent: Database Management System
---

# Database

A database is a collection of related data.

### DBMS(Database Management System)

A database management system is a collection of programs that enables users to
create and maintain a database.

#### Data base facilities

1. defining - specifying data types , structures and constraints of data to be
   stored
2. constructing - storing data on some storage medium (process control by DBMS)
3. manipulating - querying , retrieving , updating and generating reports from
   data.
4. sharing - multiple users and program to access database simultaneously.

### Data Models

A data model is a collection of concepts that is used to describe the structure
of a data base.

#### Data Model categories

1. High - level or Conceptual data models - provide concept that are close to
   the way user perceive data.
2. Low -level or Physical data models - provide concept how data is stored on
   computer storage (magnetic disk).

### Schema

Description of a database

### Instance / Database state / Snapshot/Current set of occurrences

The data in the database at a particular moment of time.

#### Three- schema architecture

1. Internal level
   - Has a internal schema/physical schema which describe physical storage
     structure and access path for the database
   - uses physical model
2. conceptual level
   - Has conceptual schema/logical schema which describe the structure of whole
     database.
   - hide physical storage structure details and describe entities ,
     relationships, user operations and constrains.
3. external or view level
   - has no. of external schema or user views .
   - describe the part of DB in which the user is interested and hide rest of
     the database from that user.

### DBMS Languages

- **DDL** (data definition language )
- _SDL_ (storage definition language)
- `VDL` (view definition language)
- DML (data manipulation language)
- DCL ( data control language)

### **ER DIAGRAM**

#### Relationship

The association among entities is called a relationship.

1.  employees **work at** department
2.  student **enrolls** in a course employees, student, department, course are
    **entities** . work at and enrolls is a **relationship**.

#### Degree of a relationship

no. of participating entities in a relationship

- binary = degree 2
- Ternary = degree 3
- n-array = degree n

#### Cardinality

The max no. of entities in one entity set which can be associated with one
entity of other set. via relation

- eg : 1 employee works at only at most 1 department = cardinality of employee
  is 1
- 1 department can have more than 1 employee = cardinality of department is n
  **Participation**

here , only 1 employee manages only 1 department and a department can have only
1 manager

E4 is an employee not a manager there not participating in a **manages **
relationship . Therefore min participation is 0 (as E4 is not participating )

All the entities of a DEPARTMENT entity is participating in the relationship
therefore **total participation** .

- **Strong entity** : having primary key
- **weak entity** not having primary key

**Identifying relationship**

The type of relationship between a strong and a weak entity set is called
identifying relationship

### CONSTRAINs

- Key Constraint
- Domain Constraint
- entity integrity constraint
- Referential integrity constraint

### TYPES OF KEYS

- simple key
- composite key
- super key
- candidate key
- primary key
- Alternate key
- Foreign key
- Self referential key

#### 12 EF CODE RULES

## RELATIONAL ALGEBRA

#### SELECT OPEERATION

- unary operator
- use to choose a subset of tuples (rows) from a relation that satisfies a
  selection condition.
- also known as filter or restrict operation

#### PROJECTION OPERATION

- selects certain columns from table
- it remove any duplicate tuples this is known as duplicate elimination.
