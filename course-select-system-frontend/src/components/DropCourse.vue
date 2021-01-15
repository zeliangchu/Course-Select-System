<template>
  <div class="middle">
      <div v-if="!isDrop">
          <h1>退选成功！</h1>
      </div>
      <h2>已选课程退选</h2>
      <table class="info">
        <tbody>
          <tr>
            <th>课程名称</th>
            <th>任课教师</th>
            <th>课程学分</th>
            <th>上课时间</th>
            <th>操作</th>
          </tr>
          <tr v-if="isDrop">
            <td>课程1</td>
            <td>教师1</td>
            <td>3</td>
            <td>周一1-2节，周三5-6节</td>
            <td><input type="checkbox"></td>
          </tr>
          <tr>
            <td>课程2</td>
            <td>教师2</td>
            <td>2</td>
            <td>周一5-6节，周五3-4节</td>
            <td><input type="checkbox"></td>
          </tr>
          <tr>
            <td>课程3</td>
            <td>教师1</td>
            <td>2</td>
            <td>周二3-4节，周五1-2节</td>
            <td><input type="checkbox"></td>
          </tr>
          <tr>
            <td>课程4</td>
            <td>教师3</td>
            <td>3</td>
            <td>周三5-6节</td>
            <td><input type="checkbox"></td>
          </tr>
          <tr>
            <td>课程5</td>
            <td>教师4</td>
            <td>1</td>
            <td>周三9-10节，周四3-4节</td>
            <td><input type="checkbox"></td>
          </tr>
        </tbody>
      </table>
      <button @click="dropclass">退选</button>
    </div>
</template>

<script>
import '@/common.css'
export default {
  data () {
    return {
      isDrop: true
    }
  },
  methods: {
    dropclass: function () {
      if (confirm('确认退选课程？')) {
        this.isDrop = false
      }
    }
  }
}
</script>

<style scoped>
.middle {
  height: 100%;
  width: 100%;
  flex-direction: column;
  padding: 2rem 0;
}
.info {
  margin-top: 1rem;
}

</style>
