<script>
import { io } from "socket.io-client"

export default {
  data() {
    return {
      nick: this.$route.params.nick,
      chat: [],
      message: "",
      client: io("http://localhost:5000")
    };
  },
  mounted() {
    this.client.connect();
    this.client.on("chat", (data) => {
      this.chat = data;
    });
    this.client.on("message", (data) => {
      // console.log(data)
      this.chat.push(data);
    });
  },
  updated() {
    const element = document.querySelector(".chat");
    element.scrollTop = element.scrollHeight;
  },
  methods: {
    submit() {
      this.client.emit("message", {
        nick: this.nick,
        message: this.message
      });
      this.message = "";
    }
  },
}
</script>

<template>
  <div class="main">
    <h1>Welcome, {{ nick }}</h1>
    <div class="chat">
      <div v-for="message in chat">
        <p v-if="this.nick === message.nick" style="text-align: right;">{{ message.message }}</p>
        <p v-else>({{ message.nick }}) {{ message.message }}</p>
      </div>
    </div>
  </div>
  <el-form @submit.prevent="submit" class="form">
    <el-input v-model="message" placeholder="Message" size="large">
      <template #append>
        <el-button @click="submit">Send</el-button>
      </template>
    </el-input>
  </el-form>
</template>

<style scoped>
.chat {
  height: calc(100vh - 128px);
  overflow-y: scroll;
}
</style>