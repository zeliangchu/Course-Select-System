<template>
  <div class="credit">
    <h2>已修课程学分</h2>
    <table class="already">
      <thead>
        <th colspan="4">学院:图说学院，姓名:洛无忧，年级:大二</th>
      </thead>
      <tbody>
        <tr>
          <th>已修课程名</th>
          <th>学分</th>
          <th>修分时间</th>
          <th>课程类型</th>
        </tr>
        <tr>
          <td>高等数学上</td>
          <td>3</td>
          <td>第一学期</td>
          <td>公共课</td>
        </tr>
        <tr>
          <td>大学物理上</td>
          <td>2</td>
          <td>第一学期</td>
          <td>公共课</td>
        </tr>
        <tr>
          <td>图说会话</td>
          <td>3</td>
          <td>第一学期</td>
          <td>专业课</td>
        </tr>
        <tr>
          <td>心理科学</td>
          <td>2</td>
          <td>第一学期</td>
          <td>通识课</td>
        </tr>
        <tr>
          <td>高等数学下</td>
          <td>3</td>
          <td>第二学期</td>
          <td>公共课</td>
        </tr>
        <tr>
          <td>计算机网络</td>
          <td>3</td>
          <td>第二学期</td>
          <td>专业课</td>
        </tr>
        <tr>
          <td>逻辑电路</td>
          <td>1</td>
          <td>第二学期</td>
          <td>非限课</td>
        </tr>
      </tbody>
    </table>

    <h2>未修课程学分</h2>
    <table class="notyet">
      <thead>
        <th colspan="2">学院:图说学院，姓名:洛无忧，年级:大二</th>
      </thead>
      <tbody>
        <tr>
          <th>课程类型</th>
          <th>需修学分</th>
        </tr>
        <tr>
          <td>公共课</td>
          <td>20</td>
        </tr>
        <tr>
          <td>体育课</td>
          <td>8</td>
        </tr>
        <tr>
          <td>专业课</td>
          <td>40</td>
        </tr>
        <tr>
          <td>通识教育课</td>
          <td>6</td>
        </tr>
        <tr>
          <td>非限课程</td>
          <td>14</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {}
</script>

<style scoped>
.credit{
    text-align: center;
    padding: 1rem 0;
}
.already,
.notyet {
  margin: 1rem auto;
}
thead th{
    padding: .5rem 2rem;
}
</style>
