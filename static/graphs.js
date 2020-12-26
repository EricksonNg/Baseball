var progressive =
{
  type: 'line',
  data: {
      labels: {{ player_date | tojson }},
      datasets: [
      {
          label: {{ category | tojson }},
          data: {{ player_category | tojson }},
          backgroundColor: [
              'rgba(254, 90, 29, 0.8)'
          ],
          borderColor: [
              'black'
          ],
          borderWidth: 1,
          lineTension: 0
      }
    ]
  },
  options: {
       scales: {
            xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                    }
                }],
            yAxes: [{
                    display: true,
                    ticks: {
                        min: 0
                    }
                }]
        },
  }
}