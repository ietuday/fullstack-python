//Events samples: https://www.w3schools.com/jsref/dom_obj_event.asp
//https://javascript.info/bubbling-and-capturing

var hOne = document.querySelector('#one')
var hTwo = document.querySelector('#two')
var hThree = document.querySelector('#three')




// On Click
hOne.addEventListener("click",function(){
  hOne.textContent = "Clicked On";
  hOne.style.color = 'red';
})

// Double Click
hTwo.addEventListener("dblclick",function(){
  hTwo.textContent = "Double Clicked!";
  hTwo.style.color = 'red';
})

// Hover (mouseover and mouseout)
hThree.addEventListener('mouseover',function(){
  hThree.textContent = "Mouse currently Over";
  hThree.style.color = 'red';
})

hThree.addEventListener('mouseout',function(){
  hThree.textContent = "Mouse Not On me."
  hThree.style.color = 'red';
})
