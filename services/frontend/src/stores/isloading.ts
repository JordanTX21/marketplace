import { defineStore } from "pinia";
import { reactive, ref } from "vue";

export const  useLoaderState = defineStore("isLoading", () => {

    const state = ref<boolean>(false)

    const changeStateTrue = () => {
        state.value = true
    }

    const changeStateFalse = () => {
        state.value = false
    }

    return { state, changeStateTrue, changeStateFalse }
})