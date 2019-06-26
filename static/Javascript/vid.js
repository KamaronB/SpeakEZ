// //create a webrtc chat
// //self invoking function.
// //anything inside of function will be automatically run
//
// var cam = "";
// function video_setup(){
//   //get the div
//
// var container = document.getElementById('vid-box');
// console.log("hello")
// //get the video element and send which type of browser we are using
// var vid = document.getElementById('video'), vendorUrl= window.URL || window.webkitURL;
//
// navigator.getMedia= navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;
// if(container.style.display=='none'){
// //display the div
// container.style.display='block';
//
//
//
// //get the media
// navigator.getMedia({
//   video: true,
//   audio: false
// },
// //callback functions
//  function(stream){
//   //place stream in video element
//   cam=stream
//   vid.srcObject=cam;
//   vid.play();
// },
// function(error){
//   //an error happened
//   console.log(error.code)
// });
// }
// else{
//   container.style.display='none';
// //close webcam
//  cam.getTracks().forEach(track => track.stop());
// }
// }
