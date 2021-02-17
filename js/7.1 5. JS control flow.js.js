/// Control Flow   https://www.w3schools.com/js/js_if_else.asp

// IF

// JavaScript syntax for if statement:
// if (condition){
//     // Code to be executed if true
// }

//Example
// these are variables of a battery charge

var charged = false;
var percentage = 40;
var over50 = false;


if (percentage > 50){
    over50 = true

}
console.log(over50)

// Set percentage higher
var percentage = 100

if (percentage == 100){
    charged = true

}
console.log(charged)


// ELSE
//
// Syntax:
// if (condition) {
//   // Code to execute if true
// } else {
//   // Code to execute if false
// }


percentage = 30

if (percentage > 50){
    console.log("Battery is more than 50%")
} else{
    console.log("Battery is less than 50%!")
}

// ELSE IF

// If more specialized conditions are needed then the "else if" statement is used.
// Syntax:
// if (condition) {
//   // Code to execute if condition above is true
//   // Exit if statement
// } else if(condition){
//   // Code to execute if condition above is true
//   // Exit if statement
// } else{
//   // Code to execute if all ifs are false
// }

// Example:
percentage = 75

if (percentage == 100){
    console.log("Battery is charged!")
} else if(percentage <= 90 && percentage >= 50){
    console.log('Sufficient Battery.')
} else if(percentage <= 20 && percentage >= 5){
    console.log("Battery Low!")
} else{
    console.log("Battery is dying.")
}

// Example with Comparison Operators

// Items sold that day
var burger = 10
var bread = 10

// Report to HQ
var report = 'blank'

if(burger >= 10 && bread >= 10){
    report = "Strong sales of both items"

}else if(burger === 0 && bread === 0){
    report = "Nothing sold!"
}else{
    report = 'We had some sales'
}
console.log(report)
