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
  
    <div class="login-form">
      <h2>S'inscrire</h2>
      <form @submit.prevent="register">
        <input type="text" v-model="newUsername" placeholder="Nom d'utilisateur" required />
        <input type="email" v-model="email" placeholder="Email" required />
        <input type="password" v-model="newPassword" placeholder="Mot de passe" required />
        <button type="submit">S'inscrire</button>
      </form>
      <p v-if="registerError" class="error">{{ registerError }}</p>
      <p v-if="registerSuccess" class="success">{{ registerSuccess }}</p>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import axios from 'axios'
  
  const router = useRouter()
  
  // Connexion
  const username = ref('')
  const password = ref('')
  const error = ref(null)
  
  // Inscription
  const newUsername = ref('')
  const email = ref('')
  const newPassword = ref('')
  const registerError = ref(null)
  const registerSuccess = ref(null)
  
  const login = async () => {
    error.value = null
    try {
      const response = await axios.post('http://localhost:8000/api/users/login/', {
        username: username.value,
        password: password.value,
      })
      const { access_token, refresh_token, user } = response.data
  
      localStorage.setItem('access_token', access_token)
      localStorage.setItem('refresh_token', refresh_token)

      let role = user.role 
  
      switch (role) {
        case 1:
          router.push('/direction')
          break
        case 2:
          router.push('/marketing')
          break
        case 3:
          router.push('/edition')
          break
        case 4:
        console.log("redirect")
          router.push('/client')
          break
        default:
          router.push('/login')
          break
      }
    } catch (err) {
      error.value = 'Erreur de connexion : ' + (err.response?.data?.message || err.message)
    }
  }
  
  const register = async () => {
    registerError.value = null
    registerSuccess.value = null
    try {
      await axios.post('http://localhost:8000/api/users/register/', {
        username: newUsername.value,
        email: email.value,
        password: newPassword.value,
        role: 1 // Normalement par défaut l'utilisateur devrait être client, mais nous n'avons pas eu le temps ni les compétences pour 
        // implémenter un mécanisme permettant à un administrateur de gérer les rôles des utilisateurs...
      })
      registerSuccess.value = "Inscription réussie ! Vous pouvez maintenant vous connecter."
    } catch (err) {
        alert('Erreur d\'inscription :')
      registerError.value = 'Erreur d\'inscription : ' + (err.response?.data?.message || err.message)
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