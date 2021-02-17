// Logical capabilities of Javascript

// Let's review booleans
true
false

// Comparison Operators
// Compare two values/objects and returns a boolean

// Greater Than
3 > 2;//return true
2 > 3;//return false

// Less Than
1 < 2;//return true

// Greater than or equal to
2 >= 2;//return true
2 >= 1;//return true

// Less than or equal to
1 <= 3;//return true
1 <= 1;//return true

// Equality
2 == 2;//return true
"username" == "username";//return true
"Username" == "username";//return false

// Inequality
2 != 3;//return true

// What about a string and a number?
"2" == 2;

// Returned True. This could become a bug in programs though.

// JS has type coercion. It will convert objects to similar data types
// to perform the comparison. This is done to save the programmer's time
// or one might argue could be causing further bugs.


// There is a way to check equality of value and type:
// 3 equal signs instead of 2
5 === 5;//true
5 === "5";//false

// Check for inequality of value and type
5 !== "5";//true
5 !== 5;//false


// It's a convention for some programmers to substitute
// true and false with 1 and 0 respectively
true == 1; //true
true === 1;//false

false == 0;//true
false === 0;//false

// Comparisions result for null, undefined, and NaN(Not-a-Number: illegal/invalid numbers)

undefined==null ; // true

NaN == NaN; // false


// LOGICAL OPERATORS

// Logical Operators is used to combine multiple comparison operators

// AND is &&
// need both conditions to be true: true && true == true
// otherwise it will return false
1 === 1 && 2 ===2; //true

// OR is ||
// need only one condition to be true to be true:
// true || true == true
// true || false == true
// false || false == false
1 === 2 || 1 ===1;//true

// NOT is !
// Inverting a condition:
// !true == false
// !false == true
!(1===1);//false
// Multiples is also syntactically correct but uncommon
!!(1===1);//true

// OPTIONAL EXERCISES
// Evaluate the following expressions on your own before using the console to check.

var x = 3
var y = 5

// Ex1:
"5" == y && x === 1;

// Ex2:
x >= 0 || y === "3";

// Ex3:
!(x !== 1) && y === (1+1);

// Ex4:
y !== "2" && x < 10 ;

// Ex5:
y !== x || y == "5" || x === 3;



/*
Answers:
Ex1: False
Ex2: True
Ex3: False
Ex4: True
Ex5: True
*/

var carName;
