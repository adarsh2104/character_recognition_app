var canvas = document.getElementById('paint');
var ctx = canvas.getContext('2d');

var sketch = document.getElementById('sketch');
var sketch_style = getComputedStyle(sketch);
canvas.width = 500;
canvas.height = 250;

var mouse = { x: 0, y: 0 };

/* Mouse Capturing Work */
canvas.addEventListener('mousemove', function (e) {
    mouse.x = e.pageX - this.offsetLeft;
    mouse.y = e.pageY - this.offsetTop;
}, false);

/* Drawing on Paint App */
ctx.lineJoin = 'round';
ctx.lineCap = 'round';

<<<<<<< HEAD
ctx.strokeStyle = "white";
ctx.lineWidth = 20
=======
ctx.strokeStyle = "red";
>>>>>>> 30b0cfcb7e8576f8df85d25944371578a51e7a15
function getColor(colour) { ctx.strokeStyle = colour; }

function getSize(size) { ctx.lineWidth = size; }


//ctx.strokeStyle = 
//ctx.strokeStyle = document.settings.colour[1].value;

canvas.addEventListener('mousedown', function (e) {
    ctx.beginPath();
    ctx.moveTo(mouse.x, mouse.y);

    canvas.addEventListener('mousemove', onPaint, false);
}, false);

canvas.addEventListener('mouseup', function () {
    canvas.removeEventListener('mousemove', onPaint, false);
}, false);

var onPaint = function () {
    ctx.lineTo(mouse.x, mouse.y);
    ctx.stroke();
};



function b64ToUint8Array(b64Image) {
    var img = atob(b64Image.split(',')[1]);
    var img_buffer = [];
    var i = 0;
    while (i < img.length) {
        img_buffer.push(img.charCodeAt(i));
        i++;
    }
    return new Uint8Array(img_buffer);
}

function sendImageForRecognition(e) {
    var b64Image = canvas.toDataURL('image/jpeg');
    var u8Image = b64ToUint8Array(b64Image);

    var formData = new FormData();
    formData.append("image", new Blob([u8Image], { type: "image/jpg" }));

<<<<<<< HEAD
    var XHR = new XMLHttpRequest();
    XHR.open("POST", "/", true);
    XHR.send(formData);

    XHR.onload = function () {

        // Process our return data
        if (XHR.status >= 200 && XHR.status < 300) {
            // Runs when the request is successful
            document.getElementById("result").innerText =  XHR.responseText;
        } else {
            // Runs when it's not
            console.log(XHR.responseText);
        }

}
=======
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/", true);
    xhr.send(formData);

>>>>>>> 30b0cfcb7e8576f8df85d25944371578a51e7a15
}