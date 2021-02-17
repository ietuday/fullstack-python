// FUNCTIONS  https://www.w3schools.com/js/js_functions.asp


// In programming, a named section of a program that performs a specific task
// so they can be run more than once is called a function. Functions can also take inputs which
//are called 'parameters' or 'arguments' for the function.

//Syntax:
function name(parameter1, parameter2, parameter3) {
    //code to be executed
}

// EXAMPLE
// Function with no input parameters
function helloworld(){
    console.log("hello world!");
}

// This will return the function but not executing it:
helloworld

// You need to add parenthesis (and any parameters if the function requires it) to actually
// 'call'(executing) the function.
helloworld()


// EXAMPLE
function helloYou(name){
    console.log("hello "+name);
}
helloYou("Jamie")

// EXAMPLE
function addition(num1,num2){
    console.log(num1+num2);
}
addition(30,20)


// Default values
// So far every single argument in the function had to be defined
// when called, but default values can be used by adding an equals sign to the paremeter.
// For example:
function helloSomeone(name="Frankie"){
    console.log("Hello "+name);
}

helloSomeone()// prints "Hello Frankie"

// Returning Values

// Without Return
function formal(name="Sam",title="Sir"){
    console.log(title+" "+name)
}


"Welcome " + formal()
// No value is returned


// With a return
function formal(name="Sam",title="Sir"){
    return title+" "+name;
}


"Welcome "+formal()

var result = formal()
// the returned value is stored in the variable 'result'

// SCOPE

// Scope is describes the visibility/accessability of an object/variable.
//
// *If a variable is defined only inside a function than its scope is
// limited to that function.*

// EXAMPLE
function times5(numInput) {
  var result = numInput * 5
  return result
}

times5(5)

// After calling function try calling:
numInput // Error
result // Error

// The scope is limited to the function

// However, variables assigned outside of the function are global variables,
// and the function will have access to them due to their scope. For example:

var v = "This is a global var"
var stuff = "This is a global stuff"

function fun(stuff){
    console.log(v);
    stuff = "Reassign stuff inside func";
    console.log(stuff);
}
fun()

// So what is happening above? The following happens
// console.log(v); check for the global variable v, the outer scope
// console.log(stuff); also check for the global variable stuff
// fun(stuff) will accept an argument stuff, print out v, and then reassign stuff
// (in the scope of the function) and print out stuff.
//
// Notice:
//
// The reassignment of stuff only effects the scope
// of the stuff variable inside the function
//
// The fun function first checks to see if v is defined
// at the function scope, if not it will then search the global scope
// for a variable names v, leading to it printing out "This is a global var".
