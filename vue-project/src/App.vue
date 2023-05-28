<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>


<template>
  <div class="container">
    <RouterView />
  </div>
</template>

<style scoped>
.container {
  margin: 10px;
}

* {
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif !important;
}
</style>
