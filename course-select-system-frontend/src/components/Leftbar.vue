<template>
  <div class="leftbar">
    <ul class="choices">
      <li>
        <router-link to="/home/creditcheck">查看学分</router-link>
      </li>
      <li @click="toggle()" class="choose">
        <span class="choose-span">选择课程</span>
        <i :class="{down:isDropdown,up:!isDropdown}"></i>
        <ul class="chooseclass" v-if="subshow">
          <li>
            <router-link to="/home/classselection">公共课</router-link>
          </li>
          <li>
            <router-link to="/home/classselection">体育课</router-link>
          </li>
          <li>
            <router-link to="/home/classselection">专业课程</router-link>
          </li>
          <li>
            <router-link to="/home/classselection">通识教育课程</router-link>
          </li>
          <li>
            <router-link to="/home/classselection">非限制性选修课程</router-link>
          </li>
        </ul>
      </li>
      <li>
        <router-link to="/home/classinfo">查看课程</router-link>
      </li>
      <li>
        <router-link to="/home/dropcourse">退课</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data () {
    return {
      subshow: false,
      isDropdown: true
    }
  },
  methods: {
    toggle: function () {
      this.subshow = !this.subshow
      this.isDropdown = !this.isDropdown
    }
  }
}
</script>

<style scoped>
.leftbar {
  width: 100%;
  height: 100%;
  background: #0c8484;
}
.choices li {
  padding: 0.6rem 2rem;
  border-bottom: 5px solid #075f5f;
}
.choices .choose {
  position: relative;
  color: white;
}
.choose .down {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  margin-left: 1rem;
  border-left: 6px solid transparent;
  border-right: 6px solid transparent;
  border-top: 6px solid #075f5f;
}
.choose .up {
  position: absolute;
  top: 6%;
  margin-left: 1rem;
  border-left: 6px solid transparent;
  border-right: 6px solid transparent;
  border-bottom: 6px solid #075f5f;
}
.chooseclass li {
  border-bottom: 1px solid #075f5f;
}
.router-link-active::after {
  content: ">";
  margin-left: .5rem;
}
</style>
