"use strict";

// Basic stuff
function popup() {
  console.log(alert("Hello World Popup!"));
}
// setTimeout(popup, 10000);

// I wish I could have used ES6 extravaganza, but not everyone supports it :(
var r = document.getElementById("rbw"),
  currentHue = 0,
  hueAddition = 5,
  documentElement = document.getElementsByTagName("html")[0],
  clickEvent = "ontouchstart" in window ? "touchend" : "click",
  classMethods = ["remove", "add"],
  rainbowTiming = 1000 / 25;

// function doThatColorThing() {
//   var color = "hsl(" + currentHue + ", 80%, 60%)",
//     nextHue = currentHue + hueAddition;
//   currentHue = nextHue > 360 ? 0 : nextHue;
//   r.style.color = color;
//   setTimeout(doThatColorThing, rainbowTiming);
// }

function someControl(id, textArr, className) {
  /* You see? No fucking jQuery needed, check:
   * http://www.vanilla-js.com/
   * http://jsperf.com/getelementbyid-vs-jquery-id/44
   */
  var el = document.getElementsByTagName("html")[0];
  var acbox = document.getElementById(id),
    textNode = acbox.firstChild,
    toggled = false;
  acbox.addEventListener(
    clickEvent,
    function() {
      var selector = Number((toggled = !toggled));
      textNode.data = textArr[selector];
      el.classList[classMethods[selector]](className);
    },
    false
  );
}

function addContrastControl() {
  someControl(
    "contrast",
    ["Add more contrast", "Remove additional contrast"],
    "contrast"
  );
}

function addInvertedControl() {
  someControl("invmode", ["Night", "Day"], "inverted");
}

// // Make color shocking background
// function psyche() {
//   document.body.style.backgroundColor = "magenta";
// }

// doThatColorThing();
addContrastControl();
addInvertedControl();
