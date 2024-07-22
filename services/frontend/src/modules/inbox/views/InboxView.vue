<template>
    <div class="bg-neutral-10 pt-[52px]" ref="targetDiv">
        <NavbarInbox :showSearch="showSearch" />
        <div class="p-6" v-if="order.id!==0">
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
                    <div class="text-neutral-90 font-semibold text-xl">Tu paquete se encuentra {{ parseState(order.states) }}</div>
                    <div class="text-base text-neutral-70">Llega aproximadamente: April 15</div>
                    <div class="flex gap-x-4">
                        <img class="w-12 h-14 rounded-xl object-cover"
                            :src="order.products[0].image"
                            alt="Bershka Mom Jeans">
                        <div>
                            <div class="text-neutral-90 text-lg truncate">{{ parseProducts(order.products) }}</div>
                            <div class="text-neutral-60 text-sm">ID:{{ parseId(order.id) }}</div>
                        </div>
                    </div>
                    <div class="flex flex-col gap-y-2">
                        <Button class="border hover:bg-neutral-05" @click="router.push({name: 'tracking', params:{id:order.id}})">More info</Button>
                        <Button class="border hover:bg-neutral-05">Cancelar orden</Button>
                    </div>
                </div>
            </div>
        </div>
        <div class="bg-white rounded-t-3xl">
            <div class="pt-8">
                <MenuInbox />
                <div class="px-6">
                    <div class="flex-1 flex px-4 py-3 bg-neutral-05 rounded-xl text-neutral-90 cursor-pointer">
                        <div class="bg-transparent w-full text-neutral-60" type="text">Filtrar inbox</div>
                        <IconSearch class="w-5 fill-neutral-50" />
                    </div>
                </div>
                <div class="pt-5 pb-4 flex flex-col gap-y-4">
                    <div class="flex gap-x-4 mx-6 py-4 hover:bg-neutral-05 rounded-xl cursor-pointer" v-for="(item,index) in orders" :key="`order-${index}`" @click="router.push({name: 'tracking', params:{id:item.id}})">
                        <img class="w-12 h-14 rounded-xl object-cover" v-if="item.products.length>0"
                            :src="item.products[0].image"
                            :alt="item.products[0].name">
                        <div v-if="item.products.length>0">
                          <div class="text-neutral-90 text-lg truncate">{{ parseProducts(item.products) }}</div>
                            <div class="text-neutral-60 text-sm">ID: {{ parseId(item.id) }}</div>
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
const { orders,order } = storeToRefs(store)

store.listOrders()

const handleScroll = () => {
    if (targetDiv.value) {
        const rect = targetDiv.value.getBoundingClientRect();
        // Ajusta este valor según la posición deseada
        // const scrollPosition = window.innerHeight / 3;
        showSearch.value = rect.top < -470;
    }
};

const parseId = (id) => {
  return id.toString().padStart(8,'0')
}

const parseProducts = (products) => {
  return products.map(obj => truncateName(obj.name,30)).join(', ')
}

const truncateName = (name, limit) => {
  if (name.length > limit) {
    return name.slice(0, limit) + '...';
  }
  return name;
};

const parseState = (states) => {
  const state = states[states.length - 1]
  const state_names = {
    'IN PREPARATION': 'en preparación'
  }
  return state_names[state]
}

onMounted(() => {
    window.addEventListener('scroll', handleScroll);
    handleScroll();
})

onUnmounted(() => {
    window.removeEventListener('scroll', handleScroll);
})
</script>
