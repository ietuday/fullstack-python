// While Loops  https://www.w3schools.com/js/js_loop_while.asp
//
// Syntax:
// while (condition){
//     # Code executed here
//     # while condition is true
// }
//
// Infinite Loops are when the loop doesn't 'break' and since computer cannot detect that,
// it will keep running the loop until you stop it.

// Example
var x = 0

while(x < 3){

    console.log("x is: "+ x);
    console.log("x is still less than 3, adding 1 to x");

    // adding one to x
    x = x+1;

}


// Manually break on conditions
// Example
var x = 0

while(x <= 6){

    console.log("x is currently: "+ x);

    if(x === 3){
      console.log("x is equal to 3, BREAK")
      break;
    }

    console.log("x is still less than or equal to 6, adding 1 to x");

    // add one to x
    x = x+1;

}

// EXERCISE

// Write a while loop that prints out only the odd numbers from 1 to 100.
