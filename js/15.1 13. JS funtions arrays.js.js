// ARRAYS

// Like a list, arrays store multiple values as a single variable.

// It allows you to save yourself the effort of multiple variables
// Instead of:
var nationality1= "American"
var nationality2 = "German"
var nationality3 = "Chinese"

// We can use:
var countries = ["American","German","Chinese"];

// Format it to be:
var countries = [
  "American",
  "German",
  "Chinese"
]

// Accessing elements of the Array
// Positions (indexing starts a zero) are fixed in an array
// so it can be accesed by that.

countries[0];

// Indexes apply to string as well
var myString = "ABCDEFG";
myString[0];

// Reassignments
// You can reassign elements by accessing their index and then just reassigning it!

countries[0] = "French"
countries //["French", "German", "Chinese"]

// Reassignment with a string cannot be done this way.
// This is the difference between immutable (strings) and mutable (Array)
// Even though they are both sequences.

// Mixed Data Types
var mixed = [true,20,"string"];

// Report back length
mixed.length // how many elements are in the array


// ARRAY METHODS
// resources:
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array

var myArr = ['one','two','three']
// Adding and removing elements (push and pop)

// Removing last item
// pop last item and return it to a new variable
// (could also just pop it off without reassigning it to a new var)
var lastItem = myArr.pop()

// Adding to end of Array
myArr.push("new_item")

// Indexing the last item (indexing starts at zero):
myArr[myArr.length - 1]

// Can nest arrays as well:
var matrix = [[1,2,3],[4,5,6],[7,8,9]]

// ARRAY ITERATION

// For loop
var arr = ['A','B','C']

for(var i = 0;i<arr.length;i++){
  console.log(arr[i])
}


// Now you may think that a for/in is a great choice, but an issue that arises
// the for/in statement will return the name of your user-defined properties
// in addition to the numeric indexes. So it will look like you are just
// returning the indexes of the array.

var arr = ['A','B','C']
for (letter in arr) {
  alert(letter);
}
// alert: 0,1,2 instead of A,B,C

// A for/of loop works though:
for (letter of arr) {
  alert(letter);
}

// It is very common to issue a function for every element
// in an array, so common in fact, that an array has a special method for this.
// It's called the forEach method:

arr.forEach(console.log);

function isCool(name){
  console.log(name+" is cool")
}

var topics = ["python",'django','science']

topics.forEach(isCool);
