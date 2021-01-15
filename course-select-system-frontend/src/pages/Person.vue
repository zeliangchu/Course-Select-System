<template>
    <div class="person">
        <div class="form">
            <div>
                <label for="name">姓名：</label>
                <input type="text" disabled value="洛无忧">
            </div>
            <div>
                <label for="id">学号：</label>
                <input type="number" value="20001001" disabled>
            </div>
            <div>
                <label for="psw">密码：</label>
                <input type="password" value="123456">
            </div>
            <div>
                <label for="college">学院：</label>
                <input type="text" value="图说学院" disabled>
            </div>
            <div>
                <label for="grade">年级：</label>
                <input type="text" value="17" disabled>
            </div>
            <div>
                <label for="class">班级：</label>
                <input type="text" value="画说3班" disabled>
            </div>
            <button class="save" @click="confirm()" type="button">保存</button>
        </div>
    </div>
</template>

<script>
import '@/common.css'
export default {
  methods: {
    confirm: function () {
      if (confirm('确定修改密码吗？')) {
        alert('修改成功')
      }
      return false
    }
  }
}
</script>

<style scoped>
.person{
    height: 100%;
    width: 100%;
    background: #0c8484;
    display: flex;
    justify-content: center;
    padding: 2rem 0;
}
.form{
    text-align: center;
}
.form div{
    margin: 1rem 0;
    font-size: 1.2rem;
}
.form div input{
    line-height: 1.5rem;
    height: 1.5rem;
    width: 15rem;
}
</style>
