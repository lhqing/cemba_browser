<template>
  <div>
    <p>Test RESTful API from Flask server</p>
    <p>Random number from backend: {{ randomNumber }}</p>
    <button @click="getRandom">New random number</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      randomNumber: 0
    }
  },
  methods: {
    getRandomFromBackend () {
      const path = `http://127.0.0.1:5000/api/random`
      axios.get(path)
        .then(response => {
          this.randomNumber = response.data.randomNumber
        })
        .catch(error => {
          console.log(error)
        })
    },
    getRandom () {
      this.randomNumber = this.getRandomFromBackend()
    }
  },
  created () {
    this.getRandom()
  }
}
</script>
