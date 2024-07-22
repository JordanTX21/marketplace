<script setup lang="ts">
import {storeToRefs} from "pinia";
import MenuHome from '@/components/MenuHome.vue'
import {useProductStore} from '@/stores/product'
import NavBar from '@/components/layouts/NavBar.vue'
import {useRouter} from 'vue-router'
import Spin from '@/components/Spin.vue'

const router = useRouter()
const store = useProductStore()
const {
  products,
  disabled,
} = storeToRefs(store);

store.list()
</script>

<template>
  <div>
    <NavBar/>
    <MenuHome/>
    <div v-if="disabled" class="w-full min-h-80 flex items-center justify-center"><Spin class="w-10 h-10 text-gray-600"/></div>
    <div class="columns-2 md:columns-3 lg:columns-4 gap-3 p-5">
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
