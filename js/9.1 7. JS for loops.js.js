// FOR LOOPS https://www.w3schools.com/js/js_loop_for.asp

// Javascript has two types of 'For' Loops:
// 1) for - loops through a block of code for a number of times
// 2) for/in - loops through elements of an object sequence(e.g. lists, arrays...)

// The For Loop

// Syntax:
// for (initialization_of_variable; condition_for_continue_running ; do_after_running_each_time) {
	//code block to be executed
// }
//
// Initialization is creating a variable(declaring) and giving it a value.

for (i = 0; i < 9; i=i+1) {
    console.log("Number is " + i );
}

// i=i+1 is the same as i++ (very common)
for (i = 0; i < 59; i++) {
    console.log("Number is " + i );
}


// Describe the output
var word = "Javascript is cool!"
for (i = 0; i < word.length; i++) {
    console.log(word[i]);
}

// Describe the output
var word = "BANANA"
for (i = 1; i < word.length; i=i+2) {
    console.log(word[i]);
}
