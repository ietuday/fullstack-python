/// LOOP ANSWERS


// PROBLEM 1

// While Loop
var x = 0
while(x<5){
  console.log("hello world!")
  x++
}

// For Loop
for (var i = 0; i < 5; i++) {
  console.log("hello world!");
}


// PROBLEM 2

// While Loop
// x+=1 is also x++
number=1
while (number<=99) {
  if (number%2 == 0){
    console.log(number);
  }
  number +=1

}

// For Loop
for (var number = 1; number <= 99; number=number+1) {
    if (number%2 == 0){
      console.log(number);
    }
}

// Commonly for loops look like this:
for (i= 1; i <= 99; i++) {
    if (i%2 == 0){
      console.log(i);
    }
}
