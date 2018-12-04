import Vue from 'vue';
import Router from 'vue-router';
import UserList from '@/components/UserList';
import UserLogin from '@/components/UserLogin';
import UserRegister from '@/components/UserRegister';
import UserUpdate from '@/components/UserUpdate';
import UserDelete from '@/components/UserDelete';

Vue.use(Router);

const router = new Router({
  routes: [
    {
      path: '/list',
      name: 'UserList',
      component: UserList,
    },
    {
      path: '/register',
      name: 'UserRegister',
      component: UserRegister,
    },
    {
      path: '/login',
      name: 'UserLogin',
      component: UserLogin,
    },
    {
      path: '/update',
      name: 'UserUpdate',
      component: UserUpdate,
    },
    {
      path: '/delete',
      name: 'UserDelete',
      component: UserDelete,
    },
  ],
});

router.replace('/login');

export default router;
