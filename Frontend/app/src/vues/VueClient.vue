<template>
    <div class="recommandations">
      <h2>Recommandations de trajet</h2>
  
      <form @submit.prevent="fetchRecommandations">
        <input type="text" v-model="idTrajet" placeholder="ID Trajet" required />
        <input type="date" v-model="dateDebut" required />
        <input type="date" v-model="dateFin" required />
        <button type="submit">Obtenir les recommandations</button>
      </form>
  
      <p v-if="error" class="error">{{ error }}</p>
  
      <ul v-if="recommandations.length">
        <li v-for="(rec, index) in recommandations" :key="index">
          {{ rec }}
        </li>
      </ul>
  
      <p v-else-if="recommandationsFetched">Aucune recommandation trouvée.</p>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  
  const idTrajet = ref('')
  const dateDebut = ref('')
  const dateFin = ref('')
  const recommandations = ref([])
  const error = ref(null)
  const recommandationsFetched = ref(false)
  
  const fetchRecommandations = async () => {
    error.value = null
    recommandations.value = []
    recommandationsFetched.value = false
  
    try {
      const response = await axios.get(
        `http://localhost:8000/api/recommandations/trajet/${idTrajet.value}/`,
        {
          params: {
            'date-debut': dateDebut.value,
            'date-fin': dateFin.value,
          },
        }
      )
      recommandations.value = response.data
      recommandationsFetched.value = true
    } catch (err) {
      error.value = 'Erreur lors de la récupération : ' + (err.response?.data?.message || err.message)
    }
  }
  </script>
  
  <style scoped>
  .recommandations {
    max-width: 500px;
    margin: auto;
    padding: 1rem;
  }
  
  .error {
    color: red;
  }
  </style>
  