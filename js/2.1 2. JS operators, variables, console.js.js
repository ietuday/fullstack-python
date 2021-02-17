// Javascript(JS) can be tested/run on browser consoles.
// To use a Chrome console right click on the window and click inspect then
// move to the second top tab that says "Console"

// Show a prompt
alert("Hello World!")

// Basic Data Types

// Numbers (only one format for integers, floats, negatives)
20
-20
20.3

// Strings - Single or Double Quotes
"My String"
"20" // Note this is no longer a number!

// Booleans (logical values)
true
false

// undefined and null
undefined
null


// NUMBERS

// Addition
2 + 2

// Subtraction
5 - 1

// Multiplication
3 * 2

// Division
10 / 2
2/5

// Exponents
2 ** 4

// Modulo (find the remainder)
15 % 14
6 % 2
6 % 4


/// STRINGS

// Strings are combinations of character(s)
// Each character has an index for their position in the string

"This is Javascript"
'This is Javascript'

// Concatentation(Combining strings)
"This" + " is Javascript"

// Length method
"This".length//is 4
"is Javascript".length//is 13

// Escape characters
"Escape \n start a new line"
"Escape \t give me a tab"
"Escape \"quotes\" "

// Index individual characters/elements (starts at zero)
"Indexes"[0]//is I
"Indexes"[6]//is s

// VARIABLES


// Syntax:
// var varName = value;

// examples:
var balance = 100;
var deposit = 50;
var total = balance + deposit;
alert(total)

var title = "Ms. ";
var name = "Chelsea";
alert(title+name)

// undefined (created but not defined)
var myvariable

// null ("nothing" that you set)
var nothing = null

/// Basic Javascript Methods

// Alert Pop-up
alert("hello world!")

// Output to console
console.log("Hello world!")

// Asking for 'Prompt Inputs'
var name = prompt("What is your name?")
