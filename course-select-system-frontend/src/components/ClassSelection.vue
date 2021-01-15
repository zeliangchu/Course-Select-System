<template>
  <div class="middle">
      <div class="success" v-if="isSuccess">
          <h1>选课成功,您选择的课程如下：</h1>
      </div>
    <div class="term" v-if="!isSuccess">
      <label>学期</label>
      <select>
        <option value="1">第一学期</option>
        <option value="1">第二学期</option>
        <option value="1">第三学期</option>
        <option value="1">第四学期</option>
        <option value="1">第五学期</option>
        <option value="1">第六学期</option>
        <option value="1">第七学期</option>
        <option value="1">第八学期</option>
      </select>
    </div>
    <table class="classes">
      <tbody>
        <tr>
          <th>课程名</th>
          <th>学分</th>
          <th>任课教师</th>
          <th>上课时间</th>
          <th>上课教室</th>
        </tr>
        <tr>
          <td>
            <input type="checkbox" /> 课程1
          </td>
          <td>3</td>
          <td>xx教师</td>
          <td>周一1-2节</td>
          <td>xx教室</td>
        </tr>
        <tr>
          <td>
            <input type="checkbox" /> 课程1
          </td>
          <td>3</td>
          <td>xx教师</td>
          <td>周一3-4节</td>
          <td>xx教室</td>
        </tr>
        <tr>
          <td>
            <input type="checkbox" /> 课程2
          </td>
          <td>2</td>
          <td>xx教师</td>
          <td>周一7-8节</td>
          <td>xx教室</td>
        </tr>
        <tr>
          <td>
            <input type="checkbox" /> 课程3
          </td>
          <td>2</td>
          <td>xx教师</td>
          <td>周二3-4节</td>
          <td>xx教室</td>
        </tr>
        <tr>
          <td>
            <input type="checkbox" /> 课程3
          </td>
          <td>2</td>
          <td>xx教师</td>
          <td>周二5-6节</td>
          <td>xx教室</td>
        </tr>
        <tr>
          <td>
            <input type="checkbox" /> 课程4
          </td>
          <td>3</td>
          <td>xx教师</td>
          <td>周三5-6节</td>
          <td>xx教室</td>
        </tr>
        <tr>
          <td>
            <input type="checkbox" /> 课程5
          </td>
          <td>1</td>
          <td>xx教师</td>
          <td>周三7-8节</td>
          <td>xx教室</td>
        </tr>
      </tbody>
    </table>
    <button type="button" @click="submit">提交</button>
  </div>
</template>

<script>
import '@/common.css'
export default {
  data () {
    return {
      isSuccess: false
    }
  },
  methods: {
    submit: function () {
      if (confirm('确定提交吗？')) {
        this.isSuccess = true
      }
    }
  }
}
</script>

<style scoped>
.middle{
    flex-direction: column;
    padding: 1rem 0;
}
.term{
    margin: 1rem auto;
}

</style>
