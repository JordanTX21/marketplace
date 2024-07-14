<script lang="ts" setup>
import { onBeforeUnmount, onMounted, ref } from "vue"

const modal = ref<HTMLElement>()

const show = defineModel<boolean>({
    default: false
})

function onClickOutside(event:any) {
    // Esta función se ejecutará cuando se haga clic fuera del div
    const div = modal.value;
    if (div && !div.contains(event.target)) {
        show.value = false
    }
}
onMounted(() => {
    document.addEventListener('mousedown', onClickOutside);
})
onBeforeUnmount(() => {
    document.removeEventListener('mousedown', onClickOutside);
})

</script>
<template>
    <transition name="modal">
        <div v-if="show" class="fixed top-0 left-0 bottom-0 right-0 bg-neutral-90/25">
            <div class="fixed bottom-0 w-full" ref="modal">
                <div class="rounded-t-3xl bg-white text-center pt-8 pb-4">
                    <slot name="header" />
                </div>
                <div class="bg-white py-4 px-2">
                    <slot name="body" />
                </div>
            </div>
        </div>
    </transition>
</template>

<style scoped>
.modal-enter-from {
    opacity: 0;
}

.modal-leave-to {
    opacity: 0;
}

.modal-enter-from .modal-container,
.modal-leave-to .modal-container {
    -webkit-transform: scale(1.1);
    transform: scale(1.1);
}
</style>