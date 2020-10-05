<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue.js App" />
    <p>{{ message }}</p>
    <button v-on:click="getMessage">get message</button>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import request from 'superagent'

export default {
  name: "Home",
  data: function () {
    return {
      message: null
    }
  },
  components: {
    HelloWorld
  },
  methods: {
    async getMessage() {
      console.log(this)
      const req = await request
        .get("http://127.0.0.1:5000/api")
      this.message = req.text
      setTimeout(() => this.message = '', 5000)
    }
  }
};
</script>
