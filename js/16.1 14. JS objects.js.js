// PART 14: JAVASCRIPT OBJECTS

// Objects are hash tables, they store information in a key-value pair.
// They are very similar to dictionaries in Python.

// Unlike an array, a Javascript Object does NOT retain order, instead you access
// the value you want by entering its corresponding key. They can hold a variety of
// data types, including nested Objects.

// Creating an Object:
var studentInfo = { name: "John", age: 19 , grade: "B" };

// Call values by their key:
studentInfo['grade'];

// Flexible data types
// Example:
var mess = { a: "hello", b: ['x','y','z'] , c: {'inside': [ 4 ,5, ["weird"]]}};

// Grabbing the letter z:
mess['b'][2];

// Changing the value that corresponds to a key:
studentInfo['age'] = 20;
//Show
studentInfo['age'];

// Could also reference itself:
studentInfo['age'] += 1

//show
studentInfo['age'];

// Show Entire Object:
// Sometimes differs by browser -
console.dir(studentInfo);

// Iterate through object:
for (var key in studentInfo) {
  console.log(key)
  console.log(studentInfo[key])
  console.log("\n")
}

/// OBJECT METHODS

// Methods are functions that are built into a javascript object.
// Usually we've called a function and then passed stuff as parameters, now we
// will build this function inside of an object, creating a method for that object.

// For Example:
var studentInfo = {
  name: "John",
  age: 19 ,
  grade: "B" ,
  studentAlert: function(){
    alert("We've got a student here!")
  }
};

// Then you can call it!
studentInfo.studentAlert()

// But what if you want to actually reference an object's
// key-value pairs.

// You'll need to use the "this" keyword
var studentInfo = {
  name: "John",
  age: 19 ,
  grade: "B" ,
  studentAlert: function(){
    alert('Your car info is, name: '+this.name+ " age: "+this.age+ " grade:"+this.grade)
  }
};

// Think of 'this' as a way to point out what you are trying to reference.
// For instance, if we didn't have this.name in the previous studentAlert example,
// Javascript would have been confused, are we referring to a global variable
// called "name"? Or the key called "name", the this keyword trys to help name
// clear that sort of distinction.
