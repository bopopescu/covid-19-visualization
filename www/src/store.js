import Vue from 'vue';
import Vuex from 'vuex';
Vue.use(Vuex);
const state={//要设置的全局访问的state对象
     showFooter: false,
     changableNum:4,
     updateTime:'112',
     sums:[],
     title:''
     //要设置的初始属性值
   };
const store = new Vuex.Store({
       state
    });
export default store;