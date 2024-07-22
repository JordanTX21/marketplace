<template>
    <div class="bg-white pt-[52px]">
        <div class="w-full flex items-center gap-2 fixed top-0 z-10 px-3 bg-white">
            <Button class="flex flex-col items-center justify-center !px-3" @click="router.back()">
                <IconArrowLeft class="w-6 stroke-neutral-80" />
            </Button>
            <div class="flex-1 text-neutral-90 font-semibold text-lg">
                Order tracking
            </div>
        </div>
        <div class="flex justify-center">
            <div class="flex flex-col gap-y-6 py-6" v-for="(product,index) in order.products">
                <div class="flex justify-center">
                    <img class="h-32 rounded-xl object-cover"
                        :src="product.image"
                        :alt="product.name">
                </div>
                <div class="flex justify-center gap-1">
                    <div>
                        <div class="text-neutral-90 text-lg truncate">{{ product.name }}</div>
                        <div class="text-neutral-60 text-sm">ID:{{ product.code }}</div>
                    </div>
                </div>
            </div>
        </div>
        <div class="flex flex-col gap-y-6">
            <div class="px-6">
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
            </div>
            <div class="px-6">
                <div class="text-neutral-90 font-semibold text-xl">Tu paquete se encuentra {{ parseStates(order.states) }}</div>
                <div class="text-base text-neutral-70">Llega aproximadamente: April 15</div>
            </div>
            <div class="pt-3 pb-4 px-6">
                <div class="py-2" v-for="(state, index) in order.states">
                    <div class="text-base text-neutral-90">{{ parseState(state).toUpperCase() }}</div>
                    <div class="text-sm text-neutral-60">{{ state.created_at }}</div>
                </div>
            </div>
            <div class="py-2 px-6">
                <Button class="border w-full hover:bg-neutral-10" @click="store.deleteOrder(order.id)">Cancelar orden</Button>
            </div>
            <hr >
            <div class="pt-3 pb-4 px-6">
                <div class="py-2">
                    <div class="text-base text-neutral-90">Información de envío</div>
                </div>
                <div class="py-2">
                    <div class="text-base text-neutral-60">Dirección</div>
                    <div class="text-base text-neutral-90">{{ order.client.address }}</div>
                </div>
                <div class="py-2">
                    <div class="text-base text-neutral-60">Recive</div>
                    <div class="text-base text-neutral-90">{{ order.client.name }}</div>
                </div>
                <div class="py-2">
                    <div class="text-base text-neutral-60">ID de Orden</div>
                    <div class="text-base text-neutral-90">{{ parseId(order.id) }}</div>
                </div>
            </div>
            <hr>
            <div class="flex gap-x-2 py-2.5 px-6">
                <div class="flex-1 text-base text-neutral-90 font-semibold">Reportar un problema</div>
                <div>
                    <IconReportTriangle class="stroke-neutral-80"/>
                </div>
            </div>
            <div class="flex gap-x-2 py-2.5 px-6">
                <div class="flex-1 text-base text-neutral-90 font-semibold">Compartir order</div>
                <div>
                    <IconShare class="fill-neutral-80"/>
                </div>
            </div>
            <hr>
        </div>
    </div>
</template>
<script lang="ts" setup>
import Button from '@/components/Button.vue';
import { useRouter, useRoute } from 'vue-router'
import { useOrderStore } from '../stores/inbox'
import { storeToRefs } from "pinia";

const store = useOrderStore()
const router = useRouter()
const route = useRoute()
const { order } = storeToRefs(store)

store.getOrder(route.params.id)

const parseStates = (states) => {
  if(states.length===0) return ''
  const state = states[states.length - 1]
  const state_names = {
    'IN PREPARATION': 'en preparación'
  }
  return state_names[state.state]
}

const parseState = (state) => {
  const state_names = {
    'IN PREPARATION': 'en preparación'
  }
  return state_names[state.state]
}

const parseId = (id) => {
  return id.toString().padStart(8,'0')
}
</script>