// On Click hand emoji will take you to the top of the page
document.getElementById('top-button').addEventListener('click',function(){
    window.scrollTo(0,0);
});

$(window).scroll(function(){
  var threshold = 208; // number of pixels before bottom of page that you want to start fading
  var op = (($(document).height() - $(window).height()) - $(window).scrollTop()) / threshold;
  if( op <= 13 ){
    $("#top-button").show();
  } else {
    $("#top-button").hide();
  }
});

// ... (your existing JavaScript code) ...

// Show the neuromorphic selector after the header content is shown
window.addEventListener('scroll', function() {
  var selectorContainer = document.getElementById('selector-container');
  if (window.scrollY > 900) {
    selectorContainer.style.opacity = 1;
    selectorContainer.style.display = 'block';
  } else {
    selectorContainer.style.opacity = 0;
    selectorContainer.style.display = 'none';
  }
});

// ... (rest of your JavaScript code) ...
const chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

const randomChar = () => chars[Math.floor(Math.random() * (chars.length - 1))],
      randomString = length => Array.from(Array(length)).map(randomChar).join("");

const card = document.querySelector(".card"),
      letters = card.querySelector(".card-letters");

const handleOnMove = e => {
  const rect = card.getBoundingClientRect(),
        x = e.clientX - rect.left,
        y = e.clientY - rect.top;

  letters.style.setProperty("--x", `${x}px`);
  letters.style.setProperty("--y", `${y}px`);

  letters.innerText = randomString(1500);    
}

card.onmousemove = e => handleOnMove(e);

card.ontouchmove = e => handleOnMove(e.touches[0]);


window.addEventListener('scroll', function() {
  var extraContent = document.getElementById('extra-content');
  if (window.scrollY > (document.body.scrollHeight - window.innerHeight - 6000)) {
    // Show/hide the extra content or take any other action
  }
});
