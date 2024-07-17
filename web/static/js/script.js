// script.js

var isOutputVisible = false;

function showOutput() {
    var textarea = document.querySelector('textarea[name="textarea"]');
    var outputBox = document.getElementById('output-box');
    var overlay = document.getElementById('overlay-box');
    var output = document.getElementById('output');

    if (textarea.value.trim() === '') {
        isOutputVisible = false;
        return;
    }

    var formData = new FormData();
    formData.append('textarea', textarea.value);

    $.ajax({
        url: '/',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response) {
            output.innerHTML = response;
            overlay.style.display = 'block';
            outputBox.style.display = 'block';
            isOutputVisible = true;
        }
    });
}

function hideOutput() {
    if (isOutputVisible) {
        var overlay = document.getElementById('overlay-box');
        var outputBox = document.getElementById('output-box');
        overlay.style.display = 'none';
        outputBox.style.display = 'none';
        isOutputVisible = false;
    }
}

document.addEventListener('click', function(event) {
    var overlay = document.getElementById('overlay-box');
    var outputBox = document.getElementById('output-box');
    if (isOutputVisible && (event.target === overlay || !outputBox.contains(event.target))) {
        hideOutput();
    }
});