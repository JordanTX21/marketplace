<template>
    <div class="bg-neutral-10 pt-[52px] min-h-screen" ref="targetDiv">
        <div class="w-full flex gap-2 fixed top-0 z-10 px-3" :class="{ 'bg-white': showSearch }">
            <Button class="flex flex-col items-center justify-center !px-3" @click="router.push({'name':'home'})">
                <IconExit class="w-6 stroke-neutral-80" />
            </Button>
            <div class="flex-1 flex items-center justify-center">
                <IconCart class="fill-neutral-80" />
            </div>
            <div class="w-1/5"></div>
        </div>
        <div class="p-6 pb-[105px]">
            <TransitionGroup name="list" tag="ul" class="flex flex-col gap-y-6">
                <div class="flex flex-col gap-y-6 rounded-2xl bg-white px-6 pt-8 pb-4 relative"
                    v-for="(item, index) in products" :key="`cart-product-${index}`">
                    <Button class="absolute top-0 right-0" @click="store.remove(item.code)">
                        <IconTrash class="fill-neutral-80" />
                    </Button>
                    <div class="flex flex-col gap-y-4 ">
                        <div class="flex gap-x-4">
                            <img class="w-28 h-32 rounded-xl object-cover" :src="item.image" :alt="item.code">
                            <div class="flex items-center">
                                <div class="text-neutral-90 text-lg">{{ item.name }}</div>
                            </div>
                        </div>
                        <div class="flex gap-x-3">
                            <div class="flex-1 text-neutral-60 text-sm">x{{ item.quantity }}</div>
                            <div class="text-neutral-90 font-semibold">${{ item.price }}</div>
                        </div>
                        <div class="grid grid-cols-2 gap-x-2">
                            <div></div>
                            <Button class="border"
                                @click="router.push({ name: 'product', params: { code: item.code } })">Edit</Button>
                        </div>
                    </div>
                </div>
            </TransitionGroup>
        </div>
        <div class="fixed bottom-0 w-full bg-neutral-10">
            <hr>
            <div class="flex gap-x-4 px-6 py-3">
                <div class="flex-1 text-base text-neutral-90">Subtotal (VAT included)</div>
                <div class="text-base font-semibold text-neutral-90">${{ store.total() }}</div>
            </div>
            <div class="py-1 px-6">
                <Button class="bg-primary text-white w-full" @click="router.push({ name: 'address' })">Continue to
                    checkout</Button>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import { onMounted, onUnmounted, ref } from 'vue'
import Button from '@/components/Button.vue'
import { useRouter } from 'vue-router'
import { useCartStore } from '@/stores/cart'
import { storeToRefs } from "pinia";

const showSearch = ref(false)
const targetDiv = ref<HTMLDivElement | null>(null)
const router = useRouter()
const store = useCartStore()
const { products } = storeToRefs(store)

store.list()

const handleScroll = () => {
    if (targetDiv.value) {
        const rect = targetDiv.value.getBoundingClientRect();
        // Ajusta este valor según la posición deseada
        // const scrollPosition = window.innerHeight / 3;
        showSearch.value = rect.top < -470;
    }
};

onMounted(() => {
    window.addEventListener('scroll', handleScroll);
    handleScroll();
})

onUnmounted(() => {
    window.removeEventListener('scroll', handleScroll);
})
</script>
<style scoped>
.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}
</style>