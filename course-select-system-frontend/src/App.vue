<template>
  <div id="app">
    <div class="topbar">
      <topbar></topbar>
    </div>
    <div class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Topbar from '@/components/Topbar'
export default {
  components: {
    Topbar
  }
}
</script>

<style scoped>
#app{
  height: 100%;
  display: flex;
  flex-direction: column;
}
.content{
  flex: 1;
}
</style>
