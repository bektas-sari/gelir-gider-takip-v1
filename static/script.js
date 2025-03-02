document.addEventListener("DOMContentLoaded", () => {
    const ctx = document.getElementById("balanceChart").getContext("2d");
  
    // Çizgi Grafiği Başlat
    let lineChart = new Chart(ctx, {
      type: "line",
      data: {
        labels: [],       // Günler (1..31) eklenecek
        datasets: [{
          label: "Günlük Bakiye (TL)",
          data: [],        // daily_balance eklenecek
          fill: false,
          borderColor: "green",
          tension: 0.1
        }]
      },
      options: {
        responsive: true,
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  
    // Sunucudan veriyi çekip grafiği güncelle
    function updateData() {
      fetch("/data")
        .then(response => response.json())
        .then(data => {
          lineChart.data.labels = data.days;       // [1,2,3,...,31]
          lineChart.data.datasets[0].data = data.balances; // [bakiyeDay1, bakiyeDay2, ...]
          lineChart.update();
        })
        .catch(err => console.error("Veri çekilirken hata oluştu:", err));
    }
  
    // Sayfa ilk yüklendiğinde ve her 2 sn'de bir güncelle
    updateData();
    setInterval(updateData, 1000);
  });
  