<template>
  <div>
    <h2>Rechercher les genres écoutés</h2>
    <form @submit.prevent="fetchRecommandations" class="form">
      <label for="lieu">Lieu :</label>
      <input
        type="text"
        v-model="lieuQuery"
        @input="searchLieux"
        placeholder="Tapez un nom de lieu"
        required
      />
      <ul v-if="lieux.length" class="autocomplete">
        <li
          v-for="lieu in lieux"
          :key="lieu.id"
          @click="selectLieu(lieu)"
        >
          {{ lieu.nom }}
        </li>
      </ul>
      <p v-if="selectedLieu">Sélectionné : {{ selectedLieu.nom }}</p>

      <label for="dateDebut">Date de début :</label>
      <input type="date" v-model="dateDebut" required />

      <label for="dateFin">Date de fin :</label>
      <input type="date" v-model="dateFin" required />

      <button type="submit" :disabled="!selectedLieuId">Rechercher</button>
    </form>

    <div v-if="recommandations.length">
      <h3>Genres les plus écoutés :</h3>
      <ul>
        <li v-for="rec in recommandations" :key="rec.genre">
          {{ rec.genre }} — {{ rec.nombre }} écoutes à {{ rec.lieu }}
        </li>
      </ul>
    </div>

    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

// Champs principaux
const lieuQuery = ref('')
const lieux = ref([])
const lieuxCache = ref([])       // Tous les lieux (chargés une seule fois)
const selectedLieu = ref(null)
const selectedLieuId = ref(null)

const dateDebut = ref('')
const dateFin = ref('')
const recommandations = ref([])
const error = ref(null)

// Chargement initial du cache, car si je fais un input select ça rame trop en raison du grand nombre de lieux
onMounted(async () => {
  try {
    const response = await axios.get('http://localhost:8000/api/trajets/')
    lieuxCache.value = response.data
  } catch (err) {
    error.value = "Erreur lors du chargement des lieux : " + err.message
  }
})

// Recherche dans le cache local
const searchLieux = () => {
  if (lieuQuery.value.length < 2) {
    lieux.value = []
    return
  }

  lieux.value = lieuxCache.value.filter(lieu =>
    lieu.nom.toLowerCase().includes(lieuQuery.value.toLowerCase())
  )
}

// Sélectionner uin lieu
const selectLieu = (lieu) => {
  selectedLieu.value = lieu
  selectedLieuId.value = lieu.id
  lieuQuery.value = lieu.nom
  lieux.value = []
}

// Requête vers l’API pour récupérer les recommandations
const fetchRecommandations = async () => {
  error.value = null
  recommandations.value = []
  if (!selectedLieuId.value || !dateDebut.value || !dateFin.value) return

  try {
    const response = await axios.get(`http://localhost:8000/api/recommandations/trajet/${selectedLieuId.value}/`, {
      params: {
        'date-debut': dateDebut.value,
        'date-fin': dateFin.value
      }
    })
    recommandations.value = response.data
  } catch (err) {
    error.value = "Erreur lors de la récupération des recommandations : " + err.message
  }
}
</script>

<style scoped>
.form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  max-width: 400px;
  margin-top: 20px;
}
input, select {
  padding: 6px;
  border-radius: 4px;
  border: 1px solid #ccc;
}
button {
  padding: 8px;
  background-color: #0055aa;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}
button:hover {
  background-color: #003f80;
}
.error {
  color: red;
  margin-top: 10px;
}
.autocomplete {
  list-style: none;
  padding: 0;
  margin: 0;
  border: 1px solid #ddd;
  max-height: 150px;
  overflow-y: auto;
  background-color: white;
}
.autocomplete li {
  padding: 8px;
  cursor: pointer;
}
.autocomplete li:hover {
  background-color: #eee;
}
</style>
