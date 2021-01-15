<template>
  <div class="container">
    <div class="form">
      <h2>学生登录</h2>
      <br />
      <label for="id">学号：</label>
      <input type="text" id="id" placeholder="请输入十位数字学号" v-model="id"/>
      <br />
      <br />
      <label for="psw">密码：</label>
      <input type="password" id="psw" v-model="psw"/>
      <br />
      <br />
      <br />
      <button type="button" @click="submit">登录</button>
    </div>
  </div>
</template>


<script>
const axios = require('axios');
export default {
  data () {
    return {
      id: '',
      psw: '',
    }
  },
  methods: {
    submit: function () {
      //使用application/x-www-form-urlencoded发送请求的话需要
      //const qs = require('qs');
      if (this.id === '' || this.psw === '') {
        alert('请输入完整信息')
      } else {
        axios.post("http://localhost:80/api/student/signin",{
          number:this.id,
          password:this.psw
        }).then(function(response){
          if (response.data['ret'] === 0) {
            this.$router.push({path: '/home'});
          } else {
            window.alert(response.data['msg']);
          }
        }).catch(function(error){
          console.log(error);
        });
      }
    }
  }
}
</script>

<style scoped>
.container {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.form {
  border-radius: 25px;
  margin: 0 auto;
  padding: 2rem 3rem;
  border: 1px solid #075f5f;
  background: #0c8484;
  color: white;
  text-align: center;
}
a{
    padding: .5rem 1rem;
    background: #075f5f;
    box-shadow: 1px 1px 2px #075f5f;
}
a:hover{
    outline: 2px solid rgb(196, 196, 196);
}
button{
  padding: .5rem 1rem;
  font-size: 1rem;
}
</style>
