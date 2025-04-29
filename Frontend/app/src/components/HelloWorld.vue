<template>
  <div>
    <Doughnut :data="chartData" :options="chartOptions" />
    <span>25</span>
  </div>
  <div>
    <Doughnut :data="chartData" :options="chartOptions" />
    <span>25</span>
  </div>
</template>

<script>
import { Doughnut } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  CategoryScale,
  LinearScale
} from 'chart.js'

// Enregistrer les composants Chart.js nécessaires
ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale, LinearScale)

export default {
  components: {
    Doughnut
  },
  data() {
    return {
      chartData: {
        labels: ['Progression', 'Restant'],
        datasets: [
          {
            label: 'Jauge',
            backgroundColor: ['#42A5F5', '#E0E0E0'], // Couleur de la jauge et de l'arrière-plan
            data: [25, 75], // Progrès (70%) et Restant (30%)
            borderWidth: 0 // Supprimer la bordure
          }
        ]
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        cutout: '80%', // Découper l'intérieur du cercle pour obtenir une forme de jauge
        rotation: 220, // Commencer la jauge à 12 heures (rotation)
        circumference: 280, // La jauge ne s'étend que sur la moitié du cercle (180 degrés)
        plugins: {
          tooltip: {
            enabled: false // Désactiver l'affichage des tooltips (lorsqu'on survole la jauge)
          },
          legend: {
            display: false // Désactiver la légende
          }
        }
      }
    }
  }
}
</script>

<style scoped>
div {
  height: 200px; /* Taille du graphique */
}
</style>
