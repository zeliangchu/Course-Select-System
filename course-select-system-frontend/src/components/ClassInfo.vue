<template>
  <div class="middle">
    <div class="info" v-if="isShow">
      <p>课程名称:图说课程</p>
      <p>任课教师:图图</p>
      <p>上课时间:周一1-2节，周五3-4节</p>
      <p>上课教室:图画教室</p>
      <p>课本信息:《说说图绘画》，图图教育出版社</p>
      <button @click="viewClass">返回</button>
    </div>
    <div class="table" v-if="!isShow">
      <h2>课程表：</h2>
      <table class="info">
        <thead>
          <th></th>
          <th>周一</th>
          <th>周二</th>
          <th>周三</th>
          <th>周四</th>
          <th>周五</th>
          <th>周六</th>
          <th>周日</th>
        </thead>
        <tbody>
          <tr>
            <th>1-2节</th>
            <td class="course"  title="点击查看详情" @click="viewClass">人机交互</td>
            <td class="course"  title="点击查看详情" @click="viewClass">软件测试</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
          </tr>
          <tr>
            <th>3-4节</th>
            <td></td>
            <td class="course"  title="点击查看详情" @click="viewClass">数字动画设计</td>
            <td></td>
            <td class="course"  title="点击查看详情" @click="viewClass">软件测试</td>
            <td></td>
            <td></td>
            <td></td>
          </tr>
          <tr>
            <th>5-6节</th>
            <td></td>
            <td class="course"  title="点击查看详情" @click="viewClass">人机交互</td>
            <td></td>
            <td></td>
            <td class="course"  title="点击查看详情" @click="viewClass">图像处理</td>
            <td></td>
            <td class="course"  title="点击查看详情" @click="viewClass">安卓开发</td>
          </tr>
          <tr>
            <th>7-8节</th>
            <td></td>
            <td></td>
            <td class="course"  title="点击查看详情" @click="viewClass">数字动画设计</td>
            <td></td>
            <td class="course"  title="点击查看详情" @click="viewClass">人机交互</td>
            <td></td>
            <td></td>
          </tr>
          <tr>
            <th>9-10节</th>
            <td class="course"  title="点击查看详情" @click="viewClass">图像处理</td>
            <td class="course"  title="点击查看详情" @click="viewClass">软件测试</td>
            <td></td>
            <td class="course"  title="点击查看详情" @click="viewClass">安卓开发</td>
            <td></td>
            <td></td>
            <td class="course"  title="点击查看详情" @click="viewClass">多媒体</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import '@/common.css'
export default {
  data () {
    return {
      isShow: false
    }
  },
  methods: {
    viewClass: function () {
      this.isShow = !this.isShow
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
.table{
    text-align: center;
}
.course:hover{
    background: #59cfcf;
}
</style>
