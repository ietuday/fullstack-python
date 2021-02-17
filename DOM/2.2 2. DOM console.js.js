// CONSOLE PRACTICE:  https://www.w3schools.com/js/js_htmldom_methods.asp

// Grab the hi Header
var header = document.getElementsByTagName("h1")[0]


// Interface with the object:

// Interface with the style:
header.style.color = 'blue'

// Random Color Function:
// Try switching colors randomly with a function every second
// http://stackoverflow.com/questions/1484506/random-color-generator-in-javascript
function randomColor(){
  var encodings = "0123456789ABCDEF";
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += encodings[Math.floor(Math.random()*16)];
  }
  return color
}

// Simple function for clarity
function changeHeaderColor(){
  colorInput = randomColor()
  header.style.color = colorInput;
}

// Now perform the action over intervals in milliseocnds(1000ms = 1s):
setInterval("changeHeaderColor()",1000);
