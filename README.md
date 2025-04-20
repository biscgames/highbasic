# highbasic
HighBasic is a basic hobbyist dynamically typed programming language

Coming up for 1.1_0:
- Static alternative to defining variables: `string <var> <string>` and `num <var> <num>`
- New command `print <string>|$<varName>` to print without the \n at the end

### Table of Contents:
- [Variables](#working-with-variables)
- [Standard Output/Input](#working-with-standard-in-and-out)
- [Macros](#working-with-macros)
- [Conditionals](#conditionals)
- [Miscellaneous](#miscellaneous)

## Syntax Rules
- Variables must be referenced with `$`, i.e: `$<varName>`
- All arguments are space-seperated, for an argument to hold a space it must be surrounded with quotes.
- Read-only variables (`!ver`) cannot be modified, nor can you create one

## Working with Variables
`var <name> <value>` declares a new variable or updates an existing one
- Variables can store either strings or numbers
- Variable names starting with `!` are read-only and cannot be modified.
- To reference an existing variable, use `$<name>`
</br>Examples:
```hb
var message lol
var number 420
: modification of read-only variables will be blocked with a warning
var !ver "1.1_0"
```
`operator <var> <value1> <value2> ... <operator>` performs arithmetic/string operations and stores the result in the variable
- `+` addition or string concatenation
- `-` subtraction
- `*` multiplication or string repetition
- `/` division</br>
Examples:
```hb
: For strings
var message lol
var number 420
: Other variables can be referenced in the operator command
operator message $number +
operator message 10 *
println $message
: For numbers
var n 15
operator n 2 *
println $n
```
## Working with standard in and out
`println <string>|$<var>` prints a line to the console! It can take a literal string or the value of a variable
</br>Examples:
```hb
: You can print the version of the programming language by referencing the read-only "!ver"
println $!ver
: => 1_0
println "lol 420"
```
`readln <string>|$<var> <destinationVar>` Prints a string to the console and expects user input. User can press enter to save their input to the destinationVar</br>
Examples:
```hb
readln "What's your name? " name
println $name
```
## Working with macros
Macros are blocks of code that can be run anytime, anywhere.
`macro <macroName>` Declares a new macro, or runs an existing macro. You can use `in macro <macroName> <line>` to add lines to the macro
</br>Examples:
```hb
: Tab whitespace for readability
macro helloWorld
  in macro helloWorld println "Hello, World!"

: Run macro
macro helloWorld
```
## Conditionals
`equalInt <var> <int>|$<var> <line>` Checks if a variable is equal to an int or another variable. If it is, it runs the line
`unlessInt <var> <int>|$<var> <line>` Same as equalInt but inverted. If the variable isn't equal to the int or other variable, it runs the line
`equalString <var> <int>|$<var> <line>` Checks if a variable is equal to an int or another variable. If it is, it runs the line
`unlessString <var> <int>|$<var> <line>` Same as equalInt but inverted. If the variable isn't equal to the int or other variable, it runs the line
</br>Fibonacci Example:
```hb
: Variable Setup
var a 0
var b 1
var iterationCnt 2
var maxCnt 32

: Fibonacci Setup
macro fiboStep
    in macro fiboStep var temp $a
    in macro fiboStep operator temp $b +
    in macro fiboStep var a $b
    in macro fiboStep var b $temp
    in macro fiboStep println $b
    in macro fiboStep operator iterationCnt 1 +
    in macro fiboStep unlessInt iterationCnt $maxCnt macro fiboStep

: Run Fibonacci macro
macro fiboStep
```
</br>Truth Machine Example:
```hb
: If input is equal to 1, print 1 128 times
var maxCnt 128
var printCnt 0
readln "" num
macro truthMachine
    in macro truthMachine println "1"
    in macro truthMachine operator printCnt 1 +
    in macro truthMachine unlessInt printCnt $maxCnt macro truthMachine
equalInt num 1 macro truthMachine
```
</br>equalString Example:
```hb
var correct "door"
readln "Where do you go through to exit or enter a building? " answer
equalString answer $correct println "Correct!"
unlessString answer $correct println "Incorrect!"
```
## Miscellaneous
`: <comment>` and `# <comment>` are both no-op (does nothing). They can be used as instructions for humans or used to disable certain lines
</br>Examples:
```br
: println "lol 420"

: This is a comment
# So is this
```
