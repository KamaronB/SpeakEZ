//create a websocket variable and a chat socket
var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
var chat_socket = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/chat" + window.location.pathname);



//send the data over the web socket instead of post
$('#chatform').on('submit', function(event) {
    var message = {
        handle: $('#handle').val(),
        message: $('#message').val(),
    }
    chat_socket.send(JSON.stringify(message));
    return false;
});



//call back for when new data is recieved on websocket

chatsock.onmessage = function(message) {
    var data = JSON.parse(message.data);
    $('#chat').append('<tr>'
        + '<td>' + data.timestamp + '</td>'
        + '<td>' + data.handle + '</td>'
        + '<td>' + data.message + ' </td>'
    + '</tr>');
};
