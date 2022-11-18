function showChatList() {
    document.getElementById('side--1').classList.remove("d-side");
    document.getElementById('side--2').classList.add("d-side");
}

function hideChatList() {
    document.getElementById('side--1').classList.add("d-side");
    document.getElementById('side--2').classList.remove("d-side");
}

function onKeyDown() {
    document.addEventListener('keydown', function (key) {
        if (key.which === 13) {
            sendMessage();
        }
    });
}

function sendMessage() {
    var message = `
        <div class="message my_message">
            <div>${document.getElementById('txtMessage').value}<br><span>8:15</span></div>
        </div>`;
    document.getElementById('messages').innerHTML += message;
    document.getElementById('txtMessage').value = '';
    document.getElementById('txtMessage').focus();

    // scroll effect
    document.getElementById('messages').scrollTo(0, document.getElementById('messages').clientHeight);
}


// DropDown 1
function dropDpwnMenu1() {
    document.getElementById("myDropdown1").classList.toggle("drop-show");
}
window.onclick = function (e) {
    if (!e.target.matches('.dropbtn')) {
        var myDropdown1 = document.getElementById("myDropdown1");
        if (myDropdown1.classList.contains('drop-show')) {
            myDropdown1.classList.remove('drop-show');
        }
    }
}

// DropDown 2
function dropDpwnMenu2() {
    document.getElementById("myDropdown2").classList.toggle("drop-show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function (e) {
    if (!e.target.matches('.dropbtn')) {
        var myDropdown2 = document.getElementById("myDropdown2");
        if (myDropdown2.classList.contains('drop-show')) {
            myDropdown2.classList.remove('drop-show');
        }
    }
}

// DropDown 3
function dropDpwnMenu3() {
    document.getElementById("myDropdown3").classList.toggle("drop-show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function (e) {
    if (!e.target.matches('.dropbtn')) {
        var myDropdown3 = document.getElementById("myDropdown3");
        if (myDropdown3.classList.contains('drop-show')) {
            myDropdown3.classList.remove('drop-show');
        }
    }
}


// Model for show list
// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function () {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}


// Send Image File
function chooseImage() {
    document.getElementById('imageFile').click();
}

function sendImage(event) {
    var file = event.files[0];

    if (!file.type.match("image.*")) {
        alert("Please select image only.")
    }
    else {
        alert("Image send...")
    }
}

// Send Icon and Audio
function changeSendIcon(control) {
    if (control.value !== '') {
        document.getElementById('send').removeAttribute('style');
        document.getElementById('audio').setAttribute('style', 'display:none');
    }
    else {
        document.getElementById('audio').removeAttribute('style');
        document.getElementById('send').setAttribute('style', 'display:none');
    }
}