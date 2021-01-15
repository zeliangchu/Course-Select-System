import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/pages/Login'
import Home from '@/pages/Home'
import ClassInfo from '@/components/ClassInfo'
import Person from '@/pages/Person'
import CreditCheck from '@/components/CreditCheck'
import DropCourse from '@/components/DropCourse'
import ClassSelection from '@/components/ClassSelection'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login
    },
    {
      path: '/person',
      name: 'person',
      component: Person
    },
    {
      path: '/home',
      name: 'home',
      component: Home,
      redirect: '/home/creditcheck',
      children: [
        {
          path: '/home/classinfo',
          name: 'classinfo',
          component: ClassInfo
        },
        {
          path: '/home/creditcheck',
          name: 'creditcheck',
          component: CreditCheck
        },
        {
          path: '/home/dropcourse',
          name: 'dropcourse',
          component: DropCourse
        },
        {
          path: '/home/classselection',
          name: 'classselection',
          component: ClassSelection
        }
      ]
    }
  ]
})
