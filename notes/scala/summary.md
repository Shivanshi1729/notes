---
layout: default
title: Summary
parent: Scala
---

# What is Scala ?

- programing language
- statistically typed
  - this means, data a variable stores is defined before compiling
- general purpose
  - can be used to make wide variety of applications
- is both
  - functional
  - object oriented
- aimed to address some criticism faced by java
- first appearance in 2004

# fp vs oop

## fp

- use of functions where each function performs a specific task
- Fundamental elements used are variables and functions.
- The data in the functions are immutable.
- Importance is not given to data but to functions.
- It follows declarative programming model.
- It uses recursion for iteration.
- It is parallel programming supported.
- The statements does not need to follow a particular order while execution
- Does not have any access specifier.
- To add new data and functions is not so easy.
- No data hiding is possible. Hence, Security is not possible.

## oop

- Classes are used where instance of objects are created
- Fundamental elements used are objects and methods, 
- The data used here are mutable data.
- Importance is given to data rather than procedures.
- It follows imperative programming model.
- It uses loops for iteration.
- It does not support parallel programming.
- The statements need to follow a order (bottom up approach while execution)
- Has three access specifiers namely, Public, Private and Protected.
- Provides and easy way to add new data and functions.
- Provides data hiding. Hence, secured programs are possible.

# How to use scala ?

- you should have `jvm` installed.
- download scala binary form the scala official website
- it comes with a repl
  - read execute print loop

---

- some tools also help you set up scala for the system
- `sbt` - scala built tool is one of them
  - it is a build system 
  - help to manage dependencies for the scala project

# basics

## hello world

```scala
object HelloWorld extends App {
  println("Hello, World!")
}
```

- singleton object, no need of class like in java
- compile it with `scalac helloworld.scala`
- run it with `scala HelloWorld`
- `scala -e` for interactive mode, and scripting

## var and val

- `var` for variables whose values will be changed - `mutable`
- `val` for variable whose value will not be changed - `immutable`

## objects

- object have states and behavior
- instance of a class

syntax:

```scala
object obj-name{

}
```

## methods

- behavior

```scala
def functionName ([list of parameters]) : [return type] = {
  //function body
  return [expr]
}
```

```scala
def printHello(){

}
```

## field

```scala
val name = "Shivanshi"
var age = 11
```

## initialize variables

```scala
var varname = values
var varname:Type = value
varname: Type = value
```

## conditionals

```scala
object demo{
  def isEven(s:Int):Boolean = {
    if(x%2==0) true
    else false
  }
}
```

## loops

- while loop is supported

```scala
val i = 0;
while(i<10){
  println(i)
  i = i+1
}
```

- for loop is supported but with some changes, and diff syntax

```scala
for(i <- 1 to 10){
  println(i)
}
```

- nested loops in one line

```scala
for(i <- 1 to 10; j <- 1 to 100)
  println(i + ' ' + j)
```

same as

```scala
for(i <- 1 to 10){
  for(j <- 1 to 100)
    println(i + ' ' + j)
}
```

- do while loop is not supported


## Data types in Scala

> all java data types are supported

- `Byte`, `Short`
- `Int`
- `Long`
- `Float`
- `Double`
- `Char`
- `Boolean`
- `String`

and some additional types

- `Unit` - no value, equivalent of `void` in `java`

~ 

- `Null` - null or empty reference
- `AnyRef` - a supertype of any reference

~

- `Nothing` - a subtype of every other types
- `Any` - a supertype of any type

for object

```
Any -> ... -> Nothing
```

for references

```
AnyRef -> ... -> Null
```

## difference b/w `null` `Null` `Nothing` `Unit` `Nil` `None` 

- `null` - literal, a value
- `Null` - a subtype of all reference types

~

- `Nothing` 
  - It doesn’t have any methods or values
  - extends the Any type

~

- `Nil` - empty list - `List()`

~

- `None` - subtype of Option type, opposite of `Some`

~

- `Unit` - `void` empty return type



## types of functions

### `first order` 

- don't take functions as arguments

### `higher order` 

- take functions as arguments

### `nested functions` 

Define function inside another function.

```scala
def factorial(x:Int):Int = {
  // making a nested function
  def fact(i:Int, acc:Int):Int = {
    if(i<=1) acc
    else fact(i-1,i * acc)
  }
  fact(x, 1)
}
```

### `anonymous`

- Anonymous functions in source code are called **function literals** 
- and at **run time**, **function literals** are instantiated into objects called **function values**
- Scala supports first-class functions
  - which means functions can be expressed in function literal syntax, 
  - i.e., `(x: Int) => x + 1` 
  - and that functions can be represented by objects
  - which are called function values

e.g.

- with one parameter `var inc = (x:Int) => x+1`
- with two parameter `var mul = (x: Int, y: Int) => x*y`
- with zero parameter `var userVal = () => { 345 }`, `println(userVal())`


## closures

- a function, whose return value depends on the value of one or more variables declared outside this function.
- variable declares outside the function is called - **free variable**
- variable in the definition is called **bound variable**

e.g.

```scala
val more = 10 // free variable
var y = (x:Int) => x + more // x-> bound variable
```

- the function value (the object) that’s created at runtime from this function literal is called a closure


## tail recursion

- recursion at the end
- use `@tailrec` annotation

```scala
@tailrec def factorial(x:Int, acc:Int):Int = {
  if(n<=1)
    acc
  else
    factorial(x-1, acc*i)
}
```

## input in scala

```scala
var a = scala.io.StdIn.readInt()
var b = scala.io.StdIn.readDouble()
var c = scala.io.StdIn.readLine()
```

## try-catch exceptions

```scala
try {
  doSomething()
}
catch {
  case ex: IOException => println("Oops!")
  case ex: NullPointerException => println("Oops!!")
}
finally{
  println("this will execute every time even if code terminates in middle")
  println("so close files here")
}
```

## match

```scala
val first = "chips"
first match {
  case "salt" => println("pepper")
  case "chips" => println("salsa")
  case "eggs" => println("bacon")
}
```

```scala
def doChore(chore: String): String = chore match { 
    case "clean dishes" => "scrub, dry"
    case "cook dinner" => "chop, sizzle"
    case _ => "whine, complain"
}
```

## different types of for loops

- with single range

```scala
for(i <- 1 to 100){
  println(i)
}
```

- with multiple range

```scala
for(i <- 1 to 10; b <- 1 to 10){
  println(i+j)
}
```

- with collections

```scala
for(i <- List(2,3,5,6)){
  println(i)
}
```

- with filters

```scala
for(
  i <- List(1,3,4,6,7)
  if i !=3; if i!=4
) {
    println(i)
}
```

- with yield

```scala
var a =
  for (
    i <- List(1, 2, 3, 4)
    if i != 3; if i != 4
  ) yield i
```

# intermediate

## classes

```scala
class Point(xc: Int, yc: Int) {
  var x: Int = xc
  var y: Int = yc
  def move(dx: Int, dy: Int) {
    x = x + dx
    y = y + dy
    println ("Point x location : " + x);
    println ("Point y location : " + y);
  }
}
```

```scala
class Point(val xc: Int, val yc: Int) {
  var x: Int = xc
  var y: Int = yc

  def move(dx: Int, dy: Int) {
    x = x + dx
    y = y + dy
    println("Point x location : " + x);
    println("Point y location : " + y);
  }
}

class Location(override val xc: Int, override val yc: Int, val zc: Int)
    extends Point(xc, yc) {
  var z: Int = zc

  def move(dx: Int, dy: Int, dz: Int) {
    x = x + dx
    y = y + dy
    z = z + dz
    println("Point x location : " + x);
    println("Point y location : " + y);
    println("Point z location : " + z);
  }
}

object Demo {
  def main(args: Array[String]) {
    val loc = new Location(10, 20, 15);
    // Move to a new location
    loc.move(10, 10, 5);
  }
}
```
## objects

- `Singleton Objects`
- A singleton is a class that can have only one instance, i.e., Object. 
- You create singleton using the keyword object instead of class keyword. 
- Since you can't instantiate a singleton object, you can't pass parameters to the primary constructor.

e.g.

```scala
class Point(val xc: Int, val yc: Int) {
  var x: Int = xc
  var y: Int = yc
  def move(dx: Int, dy: Int): Unit = {
    x = x + dx
    y = y + dy
  }
}

object Demo {
  def main(args: Array[String]): Unit = {
    val point = new Point(10, 20)
    printPoint()
    def printPoint {
      println("Point x location : " + point.x);
      println("Point y location : " + point.y);
    }
  }
}
```

here `Demo` is a singleton object.

## access modifiers

### private

- A private member is visible only inside the class or object that contains the member definition

```scala
class Outer {
  class Inner {
    private def f():Unit = { println("f") }
    class InnerMost {
        f() // OK
    }
  }
  new Inner.f() // Error: f is not accessible
}
```

### protected

- A protected member is only accessible from subclasses of the class in which the member is defined


### public

- Unlike private and protected members, it is not required to specify Public keyword for Public members.
- There is no explicit modifier for public members. 
- Such members can be accessed from anywhere.

### scope of protection

- Access modifiers in Scala can be augmented with qualifiers.
- A modifier of the form `private[X]` or `protected[X]` means 
- that access is private or protected "up to" `X`,
- where `X` designates some enclosing package, class or singleton object.

```scala
package society {
  package professional {
    class Executive {
      private[professional] var workDetails = null
      private[society] var friends = null
      private[this] var secrets = null

      def help(another: Executive) = {
        println(another.workDetails)
        println(another.secrets) //ERROR
      }
    }
  }
}
```

- `workDetails` will be accessible to any class within the enclosing package professional.
- `friends` will be accessible to any class within the enclosing package society.
- `secrets` will be accessible only on the implicit object within instance methods (this).

## traits

- like interfaces in java
- encapsulate methods and field definition
- which can then be reused by mixing them into classes
- unlike inheritance, where only one class can be inherited
- no of traits can be mixed in one class
- traits can be partially implemented, have no constructors

```scala
trait Equal{
  def isEqual(x:Any):Boolean
  def isNotEqual(x:Any):Boolean = !isEqual(x)
}
```

using trait

```scala
class Point(xc:Int, yc:Int) extends Equal{
  var x:Int = xc;
  var y:Int = yc;
  def isEqual(obj:Any) = {
    obj.isInstanceOf[Point] && obj.asInstanceOf[Point].x == y
  }
}

object Demo{
  def main(args: Array[String]):Unit = {
    val p1 = new Point(2, 3)
    val p2 = new Point(2, 4)
    val p3 = new Point(3, 3)
    println(p1.isNotEqual(p2))
    println(p1.isNotEqual(p3))
    println(p1.isNotEqual(2))
  }
}
```

- multiple traits, `extends` and then `with`

```scala
trait Bark {
    def bark: String = "Woof"
}
trait Dog {
    def breed: String
    def color: String
}
class SaintBernard extends Dog with Bark {
    val breed = "Saint Bernard"
    val color = "brown"
}
```

# Collections

- collection framework provides data structures for collecting one or more values of given types


## collection class hierarchy

- `Iterable` -> trait
  - `Collection` ->trait
    - `Seq` -> trait
      - `List` -> sealed abstract
      - `Array` -> final
      - `Array Buffer`
    - `Set` -> trait
      - `Set` -> immutable
      - `Set` -> mutable
    - `Map` -> trait
      - `Map` -> immutables
      - `Map` -> mutable

## array

- contiguous memory allocated
- elements can be accesses using indices
- homogeneous elements

```scala
val numbers = new Array[Int](5)
numbers: Array[Int] = Array(0,0,0,0,0)
```

- `arr.toList` convert array to list
- `arr.toString` convert array to string

## array buffer

- dynamic memory allocation
- no need to specify the size

```scala
// no need to specify the size
val buf = new ArrayBuffer[Int]()

// use some initial size
val buf = new ArrayBuffer[Int](10)
```

- `buf += 12`
- `buf += 15`

## lists

- like arrays but
- immutable
- have recursive structure, where array don't
- homogeneous elements

With type inference:

```scala
var fruit = List("apple", "banana", "pear")
var nums = List(1,2,3,4,5)
var listinlist = List(List(1,2,3), List(1,2,4), List(3,4,5))
var emptyList = List()
```

Without type inference:

```scala
var fruit:List[String] = List("apple", "banana", "pear")
var nums:List[Int] = List(1,2,3,4,5)
var listinlist:List[List[Int]] = List(List(1,2,3), List(1,2,4), List(3,4,5))
var emptyList:List[Nothing] = List()
```

- list types are covariant
- that means
- if `S` is subtype of `T` then
- `List[S]` is subtype of `List[T]`
- e.g.
- `List[String]` is subtype of `List[Object]`

---

- list is build form two fundamental building blocks `Nil` and `::` (cons)
- `Nil` represent empty list
- `::` (infix operator) expresses list extension ar the front
- `x::xs` - represents list with first element `x` followed by list `xs`

```scala
val fruits = "apple" :: ("oranges" :: ("bananan" :: Nil))
```

---

### basic operations on the list

- `l.head` returns the first element of the list
- `l.tail` returns a list with the first element removed
- `l.isEmpty` return `true` if list has no elements otherwise `false`
- `l.length` return the length of the list
- `l.last` - return the end element
- `l.init` - return a list removing the last element
- `l.reverse` - reverse the list
- `l.toArray` - convert list to array
- `l.toString` - convert list to a string
- `l.copyTo(arr, startidx)` - copy the list to `arr` starting from `startidx` of array
- `l.take(n)` - return a list of first `n` elements
- `l.drop(n)` - return a list of elements except first `n` elements
- `l.splitAt(n)` - return two list split at `n`

```scala

```

- `l(n)` return `n` element
- l.apply(n)` return `n` element
- `l.indices` return a list of the indices given in list
- `l.mkString(prefix, separator, suffix)` - set prefix, separator, and suffix while converting to string

```scala
var l = List('a', 'b', 'c', 'd', 'e')
println(l.mkString("[", ",", "]") // [a,b,c,d,e]
println(l.mkString("List(", ",", "]") // List(a,b,c,d,e]
```

### concatenating lists

```scala
val a = List(1,2) ::: List(3,4,5)
// or
val a = List.concat(List(1,2), List(3,4,5))
```

---

### pattern matching in list


- simple pattern matching

```scala
val fruit = List("apple", "mango", "banana")
val List(a,b,c) = fruit

// a = "apple"
// b = "mango"
// c = "banana"
```

- when list size is unknown

```scala
val fruit = List("apple", "mango", "banana", "pear", "onion")
var a :: b :: rest = fruit
// a = "apple"
// b = "mango"
// c = List("banana", "pear", "onion")
```

### higher order function in list

#### filter

- `l` - a list of type `T`
- `fun` - a predicate function of type `T=>Boolean`
- `l.filter(fun)` return a list of elements for which `fun` return `true`

```scala
var a = List(1,2,3,4,5)
var b = a.filter(_ % 2 == 0) // b = List(2,4)
```

#### partition

- `l` - a list of type `T`
- `fun` - a predicate function of type `T=>Boolean`
- `l.partition(fun)` 
  - return a tuple of list 
  - of elements for which `fun` return `true`
  - and of elements for which `fun` return `false`

#### find

- `l` - a list of type `T`
- `fun` - a predicate function of type `T=>Boolean`
- `l.find(fun)` - 
  - return first element satisfying a given predicate
  - return `None` if no element is found

#### takeWhile

- `l` - a list of type `T`
- `fun` - a predicate function of type `T=>Boolean`
- `l.takeWhile(fun)` - take values till `fun` return `true`

#### dropWhile

- `l` - a list of type `T`
- `fun` - a predicate function of type `T=>Boolean`
- `l.takeWhile(fun)` - drop values till `fun` return `true`

#### span

- `l` - a list of type `T`
- `fun` - a predicate function of type `T=>Boolean`
- `l.span(fun)` 
  - return a tuple `(l.takeWhile(fun), l.dropWhile(fun))`

#### map

- apply a function to whole list and return it

```scala
val add10: Int => Int = _ + 10 // A function taking an Int and returning an Int
List(1, 2, 3) map add10 // List(11, 12, 13) - add10 is applied to each element
```

#### foreach

- `l` - a list of type `T`
- `fun` - a predicate function of type `T=>Unit`
- `l.foreach(fun)` - run `fun` for every value in the list

e.g.

```scala
val aListOfNumbers = List(1, 2, 3, 4, 10, 20, 100)
aListOfNumbers foreach (x => println(x))
aListOfNumbers foreach println
```

## tuples

e.g.

- `(1, 2)`
- `(4, 3, 2)`
- `(1, 2, "three")`
- `(a, 2, "three")`
- `val divideInts = (x: Int, y: Int) => (x / y, x % y)` - function returning a tuple

`_._n` - access n element of the tuple, `1` based index

```scala
val d = divideInts(10, 3)    // (Int, Int) = (3,1)
d._1    // Int = 3
d._2    // Int = 1
```

also use multiple variable assignment

```scala
val (div, mod) = divideInts(10, 3)
div     // Int = 3
mod     // Int = 1
```

## option

- Scala `Option[T]` is a container for zero or one element of a given type. 
- An `Option[T]` can be either `Some[T]` or `None` object, which represents a missing value.

## ranges

- `x to y by z` =  `x until (y+1) by z`
- `val range = 0 until 10` give `Range(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)`
  - start = 0
  - end = 9 // not 10 but 9
  - step = 1
- `(0 to 10) by 5` gives `Range(0, 5, 10)`, 
  - start = 0
  - end = 10
  - step = 5
- `by` is used to set the step size

## set

- unordered elements, implements using hashing
- cannot retrieve nth element as it is unordered

~

- `val colors = Set("red", "green", "blue")`
- adding new elements - `colors + "yellow"`
- removing elements - `colors - "green"`
- union elements - `colors ++ Set("black", "white")`
- difference of set - `colors -- Set("red", "green")`

~

- `s.head`
- `s.tail`
- `s.isEmpty`
- `s.min`
- `s.max`
- `s.intersect(s2)`
- `s.contains(ele)`

## maps

- like look up tables
- stored as key, value
- `val ordinals = Map(0 -> "zero", 1 -> "one", 2 -> "two")`
- access element `ordinals(2)` gives `"two"`

~

- `s.keys` return iterable containing keys
- `s.values` return iterable containing values
- `s.isEmpty`
- `s.get(key)` get value associated with key
- `s.contains(key)` check if key is present


# Data science

## data science process

```
define business model------.    <<--------------.
map top ML problem         | 80% work           |
data preparation           |                    |
exploratory data analysis--'                    |
modelling---------------------------| 20% work  |
evaluation--------------------------'-----------'
```

1. defining business model

- clearly define the problem
- set success criteria
- define clear data science objective

2. map to ML model

- break business problems to data science problems
- identify the ML problem category

3. data preparation

- understand the data and it's constraints
- formulate data analytics strategies
- perform required transformations

4. EDA - exploratory data analysis

- perform statistical and visual analysis
- discover and handle outlier or errors
- shortlist predictive modelling techniques

5. Modelling

- experiment with multiple models
- choose most optimal model
- create a feedback loop

6. evaluation

- use model on real data
- test its accuracy
- if the model performs poorly start again form defining business model

## CRISP DM

- cross-industry standard for data mining

```
 .------------->>------>>----------->>-------------.
 |      Business      ------->   Data              |
 |  .-->Understanding <--------- Understanding     |
 |  |                                 |            |
 |  |              +----+             |            |
 ^  |              |DATA|             V            V
 ^  |              +----+             Data         V
 ^  | Deployment                      Preparation  |
 |  |     ^                             |  ^       |
 |  |     |                             |  |       |
 |  |     |                             V  |       |
 |  '-----'--------Evaluation <------ Modelling    |
 '-------<<--------<<-------------<<---------------'
```

- most widely used analytics model
- The outer circle in the diagram symbolizes the cyclic nature of data mining itself.
- A data mining process continues after a solution has been deployed.
- The lessons learned during the process can trigger new, often more focused business questions, 
- and subsequent data mining processes will benefit from the experiences of previous ones.