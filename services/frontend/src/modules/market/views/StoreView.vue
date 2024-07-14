<template>
    <div>
        <div class="w-full flex fixed top-0 z-10 bg-white px-3">
            <Button class="flex flex-col items-center justify-center !px-3" @click="router.back()">
                <IconArrowLeft class="w-5 stroke-neutral-80" />
            </Button>
            <div class="p-3 flex-1 text-neutral-90 font-semibold text-lg text-center"></div>
            <Button class="flex flex-col items-center justify-center !px-3">
                <IconSearch class="w-5 fill-neutral-80" />
            </Button>
            <Button class="flex flex-col items-center justify-center !px-3">
                <IconMoreDots class="w-5 fill-neutral-80 stroke-neutral-80" />
            </Button>
        </div>
        <div class="flex flex-col py-6 gap-4">
            <div class="flex flex-col gap-4 justify-center px-6">
                <div class="flex justify-center">
                    <img class="rounded-full border-4 border-neutral-10 w-28" :src="store.avatar" :alt="store.title">
                </div>
                <div class="flex justify-center">
                    <div class="pb-2">
                        <div class="text-center text-neutral-90 font-extrabold text-3xl">{{ store.title }}</div>
                        <div class="text-center text-neutral-60">{{ store.description }}</div>
                    </div>
                </div>
            </div>
            <div class="flex gap-x-2 px-6 justify-center">
                <Button class="bg-primary text-white">Follow</Button>
                <Button class="border">W</Button>
            </div>
            <div class="px-6 pt-2 pb-0.5 flex gap-4 justify-center">
                <div class="cursor-pointer" v-for="(item, index) in menu" :key="`item-menu-store-${index}`"
                    @click="toggleActive(item)">
                    <div class="text-base font-semibold "
                        :class="{ 'text-neutral-90': item.active, 'text-neutral-50': !item.active }">{{ item.name }}</div>
                    <div v-if="item.active" class="text-primary text-center leading-none">•</div>
                </div>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import Button from '@/components/Button.vue'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const store = ref({
    id: 1,
    title: "Levi's",
    description: "Verified official store",
    avatar: 'https://thumbs.dreamstime.com/b/levis-logo-editorial-ilustrativo-sobre-fondo-blanco-icono-vectorial-logotipos-iconos-conjunto-redes-sociales-banner-plano-vectores-210441937.jpg'
})

const menu = ref([
    {
        name: 'Overview',
        route: 'store_overview',
        active: true
    },
    {
        name: 'Collection',
        route: 'store_collection',
        active: false
    },
    {
        name: 'Blog',
        route: 'store_blog',
        active: false
    },
])

function toggleActive(item:any){
    menu.value.forEach(bt => bt.active = false)
    item.active = true
    // router.push({name:item.route})
}
</script>