<template>
  <div class="bg-white">
    <div class="">
      <div class="flex flex-col gap-y-6 py-6">
        <div class="flex justify-center">
          <img class="w-24 h-32 rounded-xl object-cover"
               src="https://i.pinimg.com/originals/07/37/1a/07371a0783400a01c20701d139857643.png"
               alt="Bershka Mom Jeans">
        </div>
        <div class="flex justify-center gap-1">
          <div v-for="(item,index) in products" :key="`product-detail-${index}`">
            <div class="text-neutral-90 text-lg truncate">{{ item.name }}</div>
            <div class="text-neutral-60 text-sm">{{ item.quantity }} | {{ item.category }} | ID:{{ item.id }}</div>
          </div>
        </div>
      </div>
    </div>
    <div class="flex flex-col gap-y-3">
      <hr>
      <div class="">
        <div class="px-6 pt-2 pb-1 grid grid-cols-2" v-for="(item,index) in products" :key="`product-${index}`">
          <div class="text-base text-neutral-90">{{ item.name }}</div>
          <div class="text-base text-neutral-90 text-right">${{ item.price }}</div>
        </div>
      </div>
      <div class="">
        <hr>
        <div class="flex gap-x-4 px-6 py-3">
          <div class="flex-1 text-base text-neutral-90">Total</div>
          <div class="text-base font-semibold text-neutral-90">${{ cart.total() }}</div>
        </div>
        <div class="py-1 px-6">
          <Button class="bg-primary text-white w-full" @click="saveOrder" :disabled="disabled">Confirmar y pagar
          </Button>
        </div>
      </div>
      <hr>
      <div class="px-6">
        <div class="text-neutral-90 font-semibold text-xl">Informacion</div>
      </div>
      <div class="pt-3 pb-4 px-6">
        <div class="py-2">
          <div class="text-sm text-neutral-60">Direccion</div>
          <div class="text-base text-neutral-90">{{ order.client.address }}
          </div>
        </div>
        <div class="py-2">
          <div class="text-sm text-neutral-60">Recive</div>
          <div class="text-base text-neutral-90">{{ order.client.name }}</div>
        </div>
        <div class="py-2">
          <div class="text-sm text-neutral-60">Metodo de pago</div>
          <div class="text-base text-neutral-90">Mastercard termina en {{ parseNumber(order.client.number) }}</div>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts" setup>
import Button from '@/components/Button.vue';
import {useRouter} from 'vue-router'
import {useCartStore} from '@/stores/cart'
import {useClientStore, useOrderStore} from '@/modules/checkout/stores/checkout'
import {storeToRefs} from 'pinia';

const router = useRouter()
const cart = useCartStore()
const clientStore = useClientStore()
const store = useOrderStore()

const {products} = storeToRefs(cart)
const {order,disabled} = storeToRefs(store)

if (order.value.client.id === 0) {
  router.push({'name': 'address'})
}

cart.list()

const saveOrder = async () => {
  const response = await store.saveOrder(products.value,cart.total(),cart.quantity())
  if (response){
    cart.reset()
    router.push({name: 'home_inbox'})
  }
}

const parseNumber = (text) => {
  return text?text.substring(-4):''
}
</script>