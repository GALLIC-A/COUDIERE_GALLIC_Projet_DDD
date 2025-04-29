<template>
    <div class="login-form">
      <h2>Connexion</h2>
      <form @submit.prevent="login">
        <input type="text" v-model="username" placeholder="Nom d'utilisateur" required />
        <input type="password" v-model="password" placeholder="Mot de passe" required />
        <button type="submit">Se connecter</button>
      </form>
      <p v-if="error" class="error">{{ error }}</p>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import axios from 'axios'

  const router = useRouter()
  
  const username = ref('')
  const password = ref('')
  const error = ref(null)
  
  const login = async () => {
    error.value = null
    try {
      const response = await axios.post('http://localhost:8000/api/users/login/', {
        username: username.value,
        password: password.value,
      })
      const { access_token, refresh_token, role } = response.data
      // Stocke les tokens (attention à la sécurité selon contexte)
      localStorage.setItem('access_token', access_token)
      localStorage.setItem('refresh_token', refresh_token)

      // Redirection ou autres actions
      console.log(role)

      switch (role) {
  case "1":
    router.push('/direction')
    break
  case "2":
    router.push('/marketing')
    break
  case "3":
    router.push('/edition')
    break
  case "4":
    router.push('/client')
    break
  default:
    // Optionnel : rediriger ou gérer un cas inattendu
    router.push('/login')
    break
}


    } catch (err) {
      error.value = 'Erreur de connexion : ' + (err.response?.data?.message || err.message)
    }
  }
  </script>
  
  <style scoped>
  .login-form {
    display: flex;
    flex-direction: column;
    border-radius: 12px;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
    padding: 20px;
    background-color: white;

    width: 250px;
    margin: auto;
  }
  form{
    display: flex;
    gap: 10px;
    flex-direction: column;
  }
  input{
    padding: 5px;
    border-radius: 5px;
  }
  button{
    padding: 10px;
    background-color: rgb(24, 91, 198);
    font-weight: 500;
    color: white;
    border-radius:12px;
    border: transparent;
  }button:hover{
    background-color: rgb(16, 63, 137);
    cursor: pointer;
  }

  .error {
    color: red;
  }
  </style>  