setInterval(function(){
    fetch('/')
        .then(response => response.text())
        .then(data => {
            if (data.includes('Reading')) {
                document.getElementById('red-led').style.backgroundColor = "#F00";
                document.getElementById('green-led').style.backgroundColor = "#000";
            } else {
                document.getElementById('red-led').style.backgroundColor = "#000";
                document.getElementById('green-led').style.backgroundColor = "#058e3e";
            }
        });
}, 1000); // Update LED colors every second
