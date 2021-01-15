<template>
  <div class="container">
    <div class="leftbar col-4">
      <leftbar></leftbar>
    </div>
    <div class="content col-8">
      <router-view></router-view>
    </div>
    <div class="clear"></div>
  </div>
</template>

<script>
import Leftbar from '@/components/Leftbar'
export default {
  components: {
    Leftbar
  }
}
</script>

<style scoped>
.container{
  width: 100%;
  height: 100%;
}
.leftbar{
  height: 100%;
}
.content{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.clear{
  clear: both;
}
</style>
