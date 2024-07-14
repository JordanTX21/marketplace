<template>
    <div class="px-6">
        <div>
            <div class="flex gap-4 py-2.5">
                <div class="flex-1 text-lg font-semibold text-neutral-90">New stores</div>
                <IconArrowRight class="stroke-neutral-80" />
            </div>
            <div class="">
                <div class="w-full flex overflow-x-auto">
                    <div class="flex flex-col gap-3 p-1" v-for="(item, index) in stores" :key="`stores-item-${index}`">
                        <div class="relative w-52 h-32 rounded-xl">
                            <img class="object-cover w-52 h-32 rounded-xl" :src="item.banner" :alt="item.title">
                            <img v-if="item.avatar" class="absolute left-2 bottom-2 rounded-full w-10 h-10 object-cover"
                                :src="item.avatar" :alt="item.title">
                        </div>
                        <div>
                            <div class="text-neutral-90">{{ item.title }}</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div>
            <div class="flex gap-4 py-2.5">
                <div class="flex-1 text-lg font-semibold text-neutral-90">Stores on sale</div>
                <IconArrowRight class="stroke-neutral-80" />
            </div>
            <div class="">
                <div class="w-full flex overflow-x-auto">
                    <div class="flex flex-col gap-3 p-1" v-for="(item, index) in stores" :key="`stores-item-${index}`">
                        <div class="relative w-52 h-32 rounded-xl">
                            <img class="object-cover w-52 h-32 rounded-xl" :src="item.banner" :alt="item.title">
                            <img v-if="item.avatar" class="absolute left-2 bottom-2 rounded-full w-10 h-10 object-cover"
                                :src="item.avatar" :alt="item.title">
                        </div>
                        <div>
                            <div class="text-neutral-90">{{ item.title }}</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="flex flex-col gap-y-2">
            <div class="py-2.5 flex gap-x-2.5">
                <div class="font-semibold text-neutral-80 font-lg">All stores</div>
            </div>
            <div class="grid grid-cols-3">
                <div class="py-3 px-1 flex flex-col gap-3" v-for="(item, index) in stores" :key="`all-store-${index}`"
                    @click="pushRouter(item)">
                    <img class="rounded-full border-2 border-neutral-10" :src="item.avatar" :alt="item.title">
                    <div class="text-neutral-90 text-center text-base">{{ item.title }}</div>
                </div>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import { ref } from "vue";
import { useRouter } from 'vue-router'

const router = useRouter()

const stores = ref([
    {
        id: 1,
        title: "Levi's",
        banner: "https://gocoloop.com/uploads/brand/66554968-f0e4-4a83-806f-eff31c99f26f.jpg",
        avatar: "https://thumbs.dreamstime.com/b/levis-logo-editorial-ilustrativo-sobre-fondo-blanco-icono-vectorial-logotipos-iconos-conjunto-redes-sociales-banner-plano-vectores-210441937.jpg"
    },
    {
        id: 2,
        title: "Levi's",
        banner: "https://gocoloop.com/uploads/brand/66554968-f0e4-4a83-806f-eff31c99f26f.jpg",
        avatar: "https://thumbs.dreamstime.com/b/levis-logo-editorial-ilustrativo-sobre-fondo-blanco-icono-vectorial-logotipos-iconos-conjunto-redes-sociales-banner-plano-vectores-210441937.jpg"
    },
    {
        id: 3,
        title: "Levi's",
        banner: "https://gocoloop.com/uploads/brand/66554968-f0e4-4a83-806f-eff31c99f26f.jpg",
        avatar: "https://thumbs.dreamstime.com/b/levis-logo-editorial-ilustrativo-sobre-fondo-blanco-icono-vectorial-logotipos-iconos-conjunto-redes-sociales-banner-plano-vectores-210441937.jpg"
    },
    {
        id: 4,
        title: "Levi's",
        banner: "https://gocoloop.com/uploads/brand/66554968-f0e4-4a83-806f-eff31c99f26f.jpg",
        avatar: "https://thumbs.dreamstime.com/b/levis-logo-editorial-ilustrativo-sobre-fondo-blanco-icono-vectorial-logotipos-iconos-conjunto-redes-sociales-banner-plano-vectores-210441937.jpg"
    },
    {
        id: 5,
        title: "Levi's",
        banner: "https://gocoloop.com/uploads/brand/66554968-f0e4-4a83-806f-eff31c99f26f.jpg",
        avatar: "https://thumbs.dreamstime.com/b/levis-logo-editorial-ilustrativo-sobre-fondo-blanco-icono-vectorial-logotipos-iconos-conjunto-redes-sociales-banner-plano-vectores-210441937.jpg"
    },
    {
        id: 6,
        title: "Levi's",
        banner: "https://gocoloop.com/uploads/brand/66554968-f0e4-4a83-806f-eff31c99f26f.jpg",
        avatar: "https://thumbs.dreamstime.com/b/levis-logo-editorial-ilustrativo-sobre-fondo-blanco-icono-vectorial-logotipos-iconos-conjunto-redes-sociales-banner-plano-vectores-210441937.jpg"
    },
])

function pushRouter(item:any) {
    router.push({ name: 'store', params: { id: item.id } })
}

</script>