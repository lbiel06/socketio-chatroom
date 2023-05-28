<script>
export default {
  data() {
    return {
      nick: "",
    }
  },
  methods: {
    submit(_) {
      if (this.nick.length)
        this.$router.push({ name: "chat", params: { nick: this.nick } })
    }
  }
}
</script>

<template>
  <h1>Welcome, {{ nick }}</h1>

  <el-form @submit.prevent="submit" ref="form">
    <el-input v-model="nick" placeholder="Nick" size="large">
      <template #append>
        <el-button @click="submit">Join</el-button>
      </template>
    </el-input>
  </el-form>
</template>
