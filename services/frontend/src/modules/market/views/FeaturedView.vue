<template>
    <div class="px-6">
        <div>
            <div class="flex gap-4 py-2.5">
                <div class="flex-1 text-lg font-semibold text-neutral-90">New stores</div>
                <IconArrowRight class="stroke-neutral-80" />
            </div>
            <div class="">
                <div class="w-full flex overflow-x-auto">
                    <div class="flex flex-col gap-3 p-1 cursor-pointer" v-for="(item, index) in stores" :key="`stores-item-${index}`" @click="router.push({ name: 'store', params: { id: item.id } })">
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
                <div class="flex-1 text-lg font-semibold text-neutral-90">Products on sale</div>
                <IconArrowRight class="stroke-neutral-80" />
            </div>
            <div class="">
                <div class="w-full flex overflow-x-auto">
                    <div class="flex flex-col gap-3 p-1 cursor-pointer" v-for="(item, index) in products"
                        :key="`products-item-${index}`" @click="router.push({ name: 'product', params: { id: item.id } })">
                        <div class="relative w-40 h-48 rounded-xl">
                            <img class="object-cover w-40 h-48 rounded-xl" :src="item.img" :alt="item.title">
                        </div>
                        <div>
                            <div class="text-neutral-90">{{ item.title }}</div>
                            <div class="flex gap-1">
                                <div class="text-neutral-60" :class="{ 'line-through': item.discount }">${{ item.price
                                    }}
                                </div>
                                <div v-if="item.discount" class="text-red font-semibold">${{ item.discount }}</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div>
            <div class="flex gap-4 py-2.5">
                <div class="flex-1 text-lg font-semibold text-neutral-90">Fresh collections</div>
                <IconArrowRight class="stroke-neutral-80" />
            </div>
            <div class="">
                <div class="w-full flex overflow-x-auto">
                    <div class="flex flex-col gap-3 p-1 cursor-pointer" v-for="(item, index) in collections"
                        :key="`collections-item-${index}`" @click="router.push({ name: 'collection', params: { id: item.id } })">
                        <div class="relative w-40 h-48 rounded-xl">
                            <img class="object-cover w-40 h-48 rounded-xl" :src="item.img" :alt="item.title">
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
        id: 1,
        title: "Levi's",
        banner: "https://gocoloop.com/uploads/brand/66554968-f0e4-4a83-806f-eff31c99f26f.jpg",
        avatar: "https://thumbs.dreamstime.com/b/levis-logo-editorial-ilustrativo-sobre-fondo-blanco-icono-vectorial-logotipos-iconos-conjunto-redes-sociales-banner-plano-vectores-210441937.jpg"
    },
    {
        id: 1,
        title: "Levi's",
        banner: "https://gocoloop.com/uploads/brand/66554968-f0e4-4a83-806f-eff31c99f26f.jpg",
        avatar: "https://thumbs.dreamstime.com/b/levis-logo-editorial-ilustrativo-sobre-fondo-blanco-icono-vectorial-logotipos-iconos-conjunto-redes-sociales-banner-plano-vectores-210441937.jpg"
    },
    {
        id: 1,
        title: "Levi's",
        banner: "https://gocoloop.com/uploads/brand/66554968-f0e4-4a83-806f-eff31c99f26f.jpg",
        avatar: "https://thumbs.dreamstime.com/b/levis-logo-editorial-ilustrativo-sobre-fondo-blanco-icono-vectorial-logotipos-iconos-conjunto-redes-sociales-banner-plano-vectores-210441937.jpg"
    },
    {
        id: 1,
        title: "Levi's",
        banner: "https://gocoloop.com/uploads/brand/66554968-f0e4-4a83-806f-eff31c99f26f.jpg",
        avatar: "https://thumbs.dreamstime.com/b/levis-logo-editorial-ilustrativo-sobre-fondo-blanco-icono-vectorial-logotipos-iconos-conjunto-redes-sociales-banner-plano-vectores-210441937.jpg"
    },
    {
        id: 1,
        title: "Levi's",
        banner: "https://gocoloop.com/uploads/brand/66554968-f0e4-4a83-806f-eff31c99f26f.jpg",
        avatar: "https://thumbs.dreamstime.com/b/levis-logo-editorial-ilustrativo-sobre-fondo-blanco-icono-vectorial-logotipos-iconos-conjunto-redes-sociales-banner-plano-vectores-210441937.jpg"
    },
])

const products = ref([
    {
        id: 1,
        title: "Bershka Platform Sandals with Buckle",
        img: "https://img01.ztat.net/article/spp-media-p1/ef6e70ac25204d9a8f840fe2ad2883f0/3bd64c22570b4a7893f9100a98440d43.jpg",
        price: 49,
        discount: 29
    },
    {
        id: 1,
        title: "Bershka Platform Sandals with Buckle",
        img: "https://img01.ztat.net/article/spp-media-p1/ef6e70ac25204d9a8f840fe2ad2883f0/3bd64c22570b4a7893f9100a98440d43.jpg",
        price: 49,
        discount: 29
    },
    {
        id: 1,
        title: "Bershka Platform Sandals with Buckle",
        img: "https://img01.ztat.net/article/spp-media-p1/ef6e70ac25204d9a8f840fe2ad2883f0/3bd64c22570b4a7893f9100a98440d43.jpg",
        price: 49,
        discount: 29
    },
    {
        id: 1,
        title: "Bershka Platform Sandals with Buckle",
        img: "https://img01.ztat.net/article/spp-media-p1/ef6e70ac25204d9a8f840fe2ad2883f0/3bd64c22570b4a7893f9100a98440d43.jpg",
        price: 49,
        discount: 29
    },
    {
        id: 1,
        title: "Bershka Platform Sandals with Buckle",
        img: "https://img01.ztat.net/article/spp-media-p1/ef6e70ac25204d9a8f840fe2ad2883f0/3bd64c22570b4a7893f9100a98440d43.jpg",
        price: 49,
        discount: 29
    },
    {
        id: 1,
        title: "Bershka Platform Sandals with Buckle",
        img: "https://img01.ztat.net/article/spp-media-p1/ef6e70ac25204d9a8f840fe2ad2883f0/3bd64c22570b4a7893f9100a98440d43.jpg",
        price: 49,
        discount: 29
    },
])

const collections = ref([
    {
        id: 1,
        title: "Lacoste x Polaroid",
        img: "https://i.ebayimg.com/images/g/siwAAOSwGZZhrrZS/s-l500.jpg",
        avatar: "https://logowik.com/content/uploads/images/lacoste-crocodile6472.logowik.com.webp"
    },
    {
        id: 1,
        title: "Lacoste x Polaroid",
        img: "https://i.ebayimg.com/images/g/siwAAOSwGZZhrrZS/s-l500.jpg",
        avatar: "https://logowik.com/content/uploads/images/lacoste-crocodile6472.logowik.com.webp"
    },
    {
        id: 1,
        title: "Lacoste x Polaroid",
        img: "https://i.ebayimg.com/images/g/siwAAOSwGZZhrrZS/s-l500.jpg",
        avatar: "https://logowik.com/content/uploads/images/lacoste-crocodile6472.logowik.com.webp"
    },
    {
        id: 1,
        title: "Lacoste x Polaroid",
        img: "https://i.ebayimg.com/images/g/siwAAOSwGZZhrrZS/s-l500.jpg",
        avatar: "https://logowik.com/content/uploads/images/lacoste-crocodile6472.logowik.com.webp"
    },
    {
        id: 1,
        title: "Lacoste x Polaroid",
        img: "https://i.ebayimg.com/images/g/siwAAOSwGZZhrrZS/s-l500.jpg",
        avatar: "https://logowik.com/content/uploads/images/lacoste-crocodile6472.logowik.com.webp"
    },
])

</script>