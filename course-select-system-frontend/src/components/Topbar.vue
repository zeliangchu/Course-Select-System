<template>
  <div class="container">
    <header class="header">
      <h1>学生选课系统</h1>
      <div class="person" v-if="this.$route.path!='/'&&this.$route.path!='/person'">
        <router-link to="/person">个人中心</router-link>
        <router-link class="logout" to="/">注销</router-link>
      </div>
      <div class="person" v-if="this.$route.path=='/person'">
        <router-link to="/home">返回首页</router-link>
      </div>
    </header>
    <div class="border"></div>
  </div>
</template>

<script>
import '@/common.css'

export default {
  mounted () {
    console.log(this.$route.path)
  }
}
</script>

<style scoped>
.header {
  width: 100%;
  padding: 2rem;
  text-align: center;
  background: #0c8484;
  color: white;
}
.person {
  float: right;
}
.border {
  width: 100%;
  height: 2rem;
  background: #075f5f;
}
.logout{
  margin-left: 2rem;
}
</style>
