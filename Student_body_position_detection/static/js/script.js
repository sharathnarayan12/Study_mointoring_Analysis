document.addEventListener("DOMContentLoaded", function() {
    // Get the container element
    var container = document.getElementById("bigDiv2");

    // Create a canvas element
    var canvas = document.createElement("canvas");
    canvas.id = "radarChart";
    canvas.width = 300; // Set smaller width
    canvas.height = 300; // Set smaller height

    // Append the canvas to the container
    container.appendChild(canvas);

    // Generate the radar chart
    var ctx = canvas.getContext("2d");
    var radarChart = new Chart(ctx, {
        type: 'radar',
        data: {
            labels: ["Label 1", "Label 2", "Label 3", "Label 4", "Label 5"],
            datasets: [{
                label: "Data",
                data: [10, 20, 30, 40, 50], // Example data
                backgroundColor: "rgba(255, 99, 132, 0.2)",
                borderColor: "rgba(255, 99, 132, 1)",
                borderWidth: 1
            }]
        },
        options: {
            scale: {
                ticks: {
                    beginAtZero: true
                }
            }
        }
    });

    // Adjust canvas style to remove top margin
    canvas.style.marginTop = "0px";
});


// this code is for not displaying labels 

// document.addEventListener("DOMContentLoaded", function() {
//     // Get the container element
//     var container = document.getElementById("bigDiv4");

//     // Create a canvas element
//     var canvas = document.createElement("canvas");
//     canvas.id = "pieChart";
//     canvas.width = 200; // Set smaller width
//     canvas.height = 200; // Set smaller height

//     // Append the canvas to the container
//     container.appendChild(canvas);

//     // Generate the pie chart
//     var ctx = canvas.getContext("2d");
//     var pieChart = new Chart(ctx, {
//         type: 'pie',
//         data: {
//             datasets: [{
//                 label: "Data",
//                 data: [10, 20, 30, 40, 50], // Example data
//                 backgroundColor: [
//                     'rgba(255, 99, 132, 0.2)',
//                     'rgba(54, 162, 235, 0.2)',
//                     'rgba(255, 206, 86, 0.2)',
//                     'rgba(75, 192, 192, 0.2)',
//                     'rgba(153, 102, 255, 0.2)'
//                 ],
//                 borderColor: [
//                     'rgba(255, 99, 132, 1)',
//                     'rgba(54, 162, 235, 1)',
//                     'rgba(255, 206, 86, 1)',
//                     'rgba(75, 192, 192, 1)',
//                     'rgba(153, 102, 255, 1)'
//                 ],
//                 borderWidth: 1
//             }]
//         },
//         options: {
//             legend: {
//                 display: false // Hide the legend
//             }
//         }
//     });
//     canvas.style.marginTop = "0px";
// });



// or this 

document.addEventListener("DOMContentLoaded", function() {
    // Get the container element
    var container = document.getElementById("bigDiv4");

    // Create a canvas element
    var canvas = document.createElement("canvas");
    canvas.id = "pieChart";
    canvas.width = 200; // Set width as needed
    canvas.height = 200; // Set height as needed

    // Append the canvas to the container
    container.appendChild(canvas);

    // Generate the pie chart
    var ctx = canvas.getContext("2d");
    var pieChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ["Label 1", "Label 2", "Label 3", "Label 4", "Label 5"],
            datasets: [{
                label: "Data",
                data: [10, 20, 30, 40, 50], // Example data
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)'
                ],
                borderWidth: 2
            }]
        },
        options: {
            legend: {
                position: 'right' // Position the legend on the right side
            }
        }
    });
    canvas.style.marginTop = "0px";
});
