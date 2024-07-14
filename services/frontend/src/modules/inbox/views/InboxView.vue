<template>
    <div class="bg-neutral-10 pt-[52px]" ref="targetDiv">
        <NavbarInbox :showSearch="showSearch" />
        <div class="p-6">
            <div class="flex flex-col gap-y-6 rounded-2xl bg-white px-6 pt-8 pb-4">
                <div class="h-1 bg-primary-20 flex items-center relative">
                    <div class="flex justify-between w-full">
                        <div class="rounded-full w-3.5 h-3.5 bg-primary"></div>
                        <div class="rounded-full w-3.5 h-3.5 bg-primary"></div>
                        <div class="rounded-full w-3.5 h-3.5 bg-primary"></div>
                        <div class="rounded-full w-3.5 h-3.5 bg-primary"></div>
                    </div>
                    <div class="absolute top-0 left-0 w-full">
                        <div class="bg-primary h-1 w-2/3"></div>
                    </div>
                </div>
                <div class="flex flex-col gap-y-4">
                    <div class="text-neutral-90 font-semibold text-xl">Your package is on it's way</div>
                    <div class="text-base text-neutral-70">Arrival estimate: April 15</div>
                    <div class="flex gap-x-4">
                        <img class="w-12 h-14 rounded-xl object-cover"
                            src="https://i.pinimg.com/originals/07/37/1a/07371a0783400a01c20701d139857643.png"
                            alt="Bershka Mom Jeans">
                        <div>
                            <div class="text-neutral-90 text-lg truncate">Bershka Mom Jeans</div>
                            <div class="text-neutral-60 text-sm">26 - S | Blue | ID:0706502</div>
                        </div>
                    </div>
                    <div class="flex flex-col gap-y-2">
                        <Button class="border" @click="router.push({name: 'tracking'})">More info</Button>
                        <Button class="border">Cancel order</Button>
                    </div>
                </div>
            </div>
        </div>
        <div class="bg-white rounded-t-3xl">
            <div class="pt-8">
                <MenuInbox />
                <div class="px-6">
                    <div class="flex-1 flex px-4 py-3 bg-neutral-05 rounded-xl text-neutral-90 cursor-pointer">
                        <div class="bg-transparent w-full text-neutral-60" type="text">Filter inbox</div>
                        <IconSearch class="w-5 fill-neutral-50" />
                    </div>
                </div>
                <div class="pt-5 pb-4 flex flex-col">
                    <div class="flex gap-x-4 px-6 py-4" v-for="(item,index) in orders" :key="`order-${index}`">
                        <img class="w-12 h-14 rounded-xl object-cover"
                            :src="item.img"
                            :alt="item.title">
                        <div>
                            <div class="text-neutral-90 text-lg truncate">{{ item.title }}</div>
                            <div class="text-neutral-60 text-sm">{{ item.detail }}</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import { onMounted, onUnmounted, ref } from 'vue'
import NavbarInbox from '../components/NavbarInbox.vue'
import MenuInbox from '../components/MenuInbox.vue'
import Button from '@/components/Button.vue'
import { useRouter } from 'vue-router'
import { useOrderStore } from '../stores/inbox'
import { storeToRefs } from "pinia";

const showSearch = ref(false)
const targetDiv = ref<HTMLDivElement | null>(null)
const router = useRouter()
const store = useOrderStore()
const { orders } = storeToRefs(store)

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
