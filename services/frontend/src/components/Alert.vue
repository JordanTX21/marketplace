<script lang="ts" setup>
import { ref, defineProps, watch } from 'vue'
import { sleep } from "@/utils"

const props = defineProps({
    type: {
        type: String,
        default: "success"
    },
    timmer: {
        type: Number,
        default: 1500
    }
})
const show = defineModel<boolean>({
    default: false
})
watch(()=>show.value,async (newShow,oldShow)=>{
    if(show.value){
        await sleep(props.timmer)
        show.value = false
    }
})
</script>

<template>
    <transition name="fade">
        <div v-if="show" class="border border-dashed rounded bg-white p-2 fixed bottom-5 left-5"
            :class="{ 'border-red-100': type === 'error', 'border-green-100': type === 'success', 'border-yellow-100': type === 'warning' }">
            <div class="flex gap-x-2"
                :class="{ 'text-red-100': type === 'error', 'text-green-100': type === 'success', 'text-yellow-100': type === 'warning' }">
                <slot />
            </div>
        </div>
    </transition>
</template>
<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>