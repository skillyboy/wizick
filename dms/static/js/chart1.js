// Doughnut Chart 

var ctx = document.getElementById('doughnutChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Business Contracts', 'IPR', 'NDA', 'Real Estate Contract', 'Employment Agreement '],
        datasets: [{
            label: 'Number of Contracts',
            data: [23, 17, 17, 20, 23],
            backgroundColor: [

                'rgba(0, 49, 129, 1)',
                'rgba(207, 96, 27, 1)',
                'rgba(142, 48, 255, 1)',
                'rgba(86, 153, 23, 1)',
                'rgba(138, 0, 121, 1)',
                
            ],
            borderColor: [
                'rgba(255, 255, 255, 1)',
                'rgba(255, 255, 255, 1)',
                'rgba(255, 255, 255, 1)',
                'rgba(255, 255, 255, 1)',
                'rgba(255, 255, 255, 1)',
                
               
            ],
            borderWidth: 2
        }]
    },
    options: {
        maintainAspectRatio: false,
            responsive: true,
            plugins:{
                legend: {
                    display: true,
                    position: 'right',
                    labels: {
                        // boxWidth: 15
                        usePointStyle: true,
                        pointStyle: 'rect',
                        
                    }
                },
                layout: {
                    padding: 20
                }

            }
        

    }


});



