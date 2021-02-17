// Follow along with the video lecture

var x = document.querySelector("p")

// Getting Text
x.textContent

// Mutating Text
x.textContent = "new"

// Refresh the page
// Show actual HTML
x.innerHTML

// Edit HTML
x.innerHTML = "This is <i>ITALIC</i>"

// Special tags manipulations only allowed in HTML

// Attributes:

var special = document.querySelector("#special")
var specialA = special.querySelector("a")

specialA.getAttribute("href")

specialA.setAttribute("href","https://www.facebook.com")
