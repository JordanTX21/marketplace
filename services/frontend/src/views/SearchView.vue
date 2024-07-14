<template>
    <div class="bg-white py-[52px]">
        <div class="w-full flex fixed top-0 z-10 bg-white px-3">
            <Button class="flex flex-col items-center justify-center !px-3" @click="router.back()">
                <IconArrowLeft class="w-5 stroke-neutral-80" />
            </Button>
            <form class="flex-1" @submit.prevent="store.search(search)">
                <div class="flex gap-x-2 px-6">
                    <div class="flex-1 flex px-4 py-3 bg-neutral-05 rounded-xl text-neutral-90">
                        <input v-model="search"
                            class="focus:outline-none bg-transparent w-full placeholder:text-neutral-60" type="text"
                            placeholder="Search on Tassel" />
                        <Button type="button" v-if="search && search.length > 0" class="flex items-center !p-0"
                            @click="search='';products=[]">
                            <IconDeleteText class="w-5 stroke-neutral-80" />
                        </Button>
                    </div>
                    <Button class="border !font-extrabold"><IconSearch class="w-4 h-4 fill-neutral-80"/></Button>
                </div>
            </form>
        </div>
        <div class="flex flex-col gap-y-3 py-4" v-if="searchs.length>0 && products.length==0">
            <div class="text-neutral-50 font-semibold px-6">Recent searches</div>
            <div class="flex flex-col gap-2">
                <div v-for="(item,index) in searchs" :key="`recent-search-${index}`">
                    <div class="flex ga-x-10 py-3 px-6">
                        <div class="flex-1 text-neutral-90 cursor-pointer">{{ item }}</div>
                        <button ><IconExit class="stroke-neutral-80 w-5" /></button>
                    </div>
                    <hr>
                </div>
            </div>
        </div>
        <div class="columns-2 md:columns-3 lg:columns-4 gap-3 p-5" v-if="products.length>0">
            <div class="break-inside-avoid mb-4 cursor-pointer" v-for="(item, index) in products"
                :key="`product-item-${index}`" @click="router.push({ name: 'product', params: { code: item.code } })">
                <div class="rounded-xl bg-primary mb-2">
                    <img class="rounded-xl" :src="item.image" :alt="item.name">
                </div>
                <div class="text-neutral-90 text-sm truncate">{{ item.name }}</div>
                <div class="text-neutral-90 text-sm font-semibold">${{ item.price.toFixed(2) }}
                </div>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import { ref } from "vue";
import Button from "@/components/Button.vue"
import { useRouter } from 'vue-router'
import { useProductStore } from '@/stores/product'
import { storeToRefs } from "pinia";

const router = useRouter()
const store = useProductStore()
const {searchs,products} = storeToRefs(store)

const search = ref<string>('')

products.value = []

</script>