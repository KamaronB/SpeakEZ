// ///////////////////////////////MESSAGES/////////////////////////////////////////
//     var formData=$("#form")
//     var messages=$("#messages")
//     var vid_div=$("#vid-div")
//     var video=$("#video2")
//     var chat_history=$("#history")
//     var roomName = "{{ room.room_name}}"
//     const img = document.getElementById('img');
//     const img2 = document.getElementById('img2');
//     var cameraButton = document.getElementById('vid-icon');
//     // console.log(img.src=='')
//     // var location= window.location
//     var endpoint= window.location.host + '/profile/chat/room/' + roomName + '/'
//     var ws_start='ws://'
//     if(window.location.protocol=='https:')
//     {
//       //change to secure sockets
//       ws_start='wss://'
//     }
//     //new websocket
//     var chatSocket = new WebSocket(ws_start + endpoint)
//     chatSocket.onmessage = function(e){
//       console.log("message",e)
//       //parse the returned data from consumer.py
//       var returned_data= JSON.parse(e.data)
//
//
//       //append the chat history with new messages
//       if (returned_data.msg!=null){
//       chat_history.append("<li>  <div class='card'><div class='card-body'>" + returned_data.msg + " " + returned_data.username + "  </div></div></li>")
//         }
//
//       if(returned_data.video!=null)
//       {
//
//         console.log(returned_data.userid)
//         if (returned_data.userid=="{{room.user_1}}")
//         {
//           console.log("true")
//           img.src=returned_data.video
//         }
//         else
//         {
//           img2.src=returned_data.video
//         }
//
//
//       }
//
//
//
//     }
//     chatSocket.onopen= function(e){
//       console.log("open",e)
//       // disable post Submit
//       formData.submit(function(event){
//         event.preventDefault()
//         var msg= messages.val()
//         var data={
//           'message': msg
//         }
//          chatSocket.send(JSON.stringify(data))
//          formData[0].reset()
//       })
//     }
//     chatSocket.onerror= function(e){
//       console.log("error",e)
//     }
//     chatSocket.onclose= function(e){
//       console.log("close",e)
//     }
//
//
// ////////////////////////////////Video//////////////////////////////////////////
//
//
//     var cam = "";
//     function video_setup(){
//       //get the div
//
//     var container = document.getElementById('vid-box');
//     console.log("hello")
//     //get the video element and send which type of browser we are using
//     var vid = document.getElementById('video'), vendorUrl= window.URL || window.webkitURL;
//
//     navigator.getMedia= navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;
//     if (container.style.display=='none') {
//     //display the div
//     // container.style.display='block';
//
//
//
//     //get the media
//     navigator.getMedia({
//       video: true,
//       audio: false
//     },
//     //callback functions
//      function(stream){
//       //place stream in video element
//       cam=stream
//       vid.srcObject=cam;
//     vid.play();
//
//     },
//     function(error){
//       //an error happened
//       console.log(error.code)
//     });
//     function Frame() {
//     const canvas = document.createElement('canvas');
//     canvas.width =  vid.width;
//     canvas.height = vid.height;
//     canvas.getContext('2d').drawImage(vid, 0, 0);
//     const data = canvas.toDataURL();
//     return data;
//   }
//       const FPS=1;
//              console.log(`Connected to ${endpoint}`);
//              setInterval(() => {
//                data={'video': Frame()}
//
//                  chatSocket.send(JSON.stringify(data));
//              }, 1000 / FPS);
//     }
//
//     else{
//       container.style.display='none';
//     //close webcam
//      cam.getTracks().forEach(track => track.stop());
//     }
//
//            }
