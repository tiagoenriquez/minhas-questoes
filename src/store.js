import { createStore } from 'vuex'

const store = createStore({
  state () {
    return {
      error: '',
      test: null
    }
  },
  mutations: {
    setError (state, value) {
      state.error = value
    },
    setTest(state, value) {
      state.test = value
    }
  }
})

export default store