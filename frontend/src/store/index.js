import { createStore } from 'vuex'

export default createStore({
  state: {
    access:'',
    refresh:'',
    isAuthenticated: false
  },
  getters: {
  },
  mutations: {
    initializeStore(state){
      if(localStorage.getItem('access')){
        state.access = localStorage.getItem('access')
        state.refresh = localStorage.getItem('refresh')
        state.isAuthenticated = true
      } else {
        state.access = ''
        state.refresh = ''
        state.isAuthenticated = false
      }
    },
    setAccess(state, access){
      state.access = access
      state.isAuthenticated = true
    },
    removeAccess(state){
      state.access =''
      state.refresh =''
      state.isAuthenticated=false
    },
    setRefresh(state,refresh){
      state.refresh=refresh
      state.isAuthenticated=true
    }
  },
  actions: {
  },
  modules: {
  }
})
