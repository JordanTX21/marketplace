<template>
  <div>
    <div class="px-6 py-6 text-xl text-neutral-90">Seleccione o agregue su metodo de pago</div>
    <div>
      <div class="py-3 pl-6 flex gap-x-2 overflow-x-auto">
        <div v-for="(item,index) in cards"
             class="w-32 h-52 p-3 bg-yellow-10 rounded-xl grid content-between cursor-pointer"
             :class="{'opacity-50':selected !== item.id}"
             :key="`card-${index}`" @click="selected = item.id;orderStore.saveCard({...item})">
          <div></div>
          <div>
            <div class="text-sm text-neutral-70">Visa</div>
            <div class="text-lg font-semibold text-neutral-90">{{ parseNumber(item.number) }}</div>
          </div>
        </div>
      </div>
      <div class="px-6 py-4">
        <Button type="button" class="border w-full" @click="showModal()">Agregar Tarjeta</Button>
      </div>
    </div>
    <div class="fixed bottom-0 w-full bg-white">
      <hr>
      <div class="flex gap-x-4 px-6 py-3">
        <div class="flex-1 text-base text-neutral-90">Total</div>
        <div class="text-base font-semibold text-neutral-90">${{ cart.total() }}</div>
      </div>
      <div class="py-1 px-6">
        <Button class="bg-primary text-white w-full" @click="routerPush">Continuar</Button>
      </div>
    </div>
    <teleport to="body">
      <Modal v-model="show">
        <template #header>Agregar Tarjeta</template>
        <template #body>
          <form @submit="store.saveCard" class="flex flex-col gap-y-4">
            <div class="px-4">
              <label class="text-primary" for="number">Número de tarjeta</label>
              <input v-model="number" v-bind="numberProps" type="text" id="number" maxlength="16"
                     placeholder="Escriba el número de la tarjeta"
                     :class="{ '!border-b-red-100': errors.number !== undefined }"
                     class="focus:outline-none bg-transparent w-full py-3 border-b border-b-neutral-50 focus:border-b-primary disabled:border-b-neutral-30 placeholder:text-neutral-30 disabled:text-neutral-30 focus:placeholder:text-neutral-90">
              <div class="text-red pl-3" v-if="errors.number !== ''">{{ errors.number }}</div>
            </div>
            <div class="px-4">
              <label class="text-primary" for="name">Nombre</label>
              <input v-model="name" v-bind="nameProps" type="text" id="name"
                     placeholder="Nombre cómo figura en la tarjeta"
                     :class="{ '!border-b-red-100': errors.name !== undefined }"
                     class="focus:outline-none bg-transparent w-full py-3 border-b border-b-neutral-50 focus:border-b-primary disabled:border-b-neutral-30 placeholder:text-neutral-30 disabled:text-neutral-30 focus:placeholder:text-neutral-90">
              <div class="text-red pl-3" v-if="errors.name !== ''">{{ errors.name }}</div>
            </div>
            <div class="px-4">
              <label class="text-primary" for="month">Fecha de vencimiento</label>
              <div
                  :class="{ '!border-b-red-100': errors.month !== undefined,'!border-b-primary !placeholder:text-neutral-90': false}"
                  class="w-full flex gap-1 py-3 border-b border-b-neutral-50 disabled:border-b-neutral-30 disabled:text-neutral-30">
                <input v-model="month" v-bind="monthProps" type="text" id="month" ref="monthHTML"
                       placeholder="MM"
                       class="focus:outline-none w-7 bg-transparent placeholder:text-neutral-30" maxlength="2">
                <span class="text-neutral-30">/</span>
                <input v-model="year" v-bind="yearProps" type="text" id="year" ref="yearHTML"
                       placeholder="YY"
                       class="focus:outline-none bg-transparent placeholder:text-neutral-30" maxlength="4">
              </div>
              <div class="text-red pl-3" v-if="errors.month !== ''">{{ errors.month }}</div>
              <div class="text-red pl-3" v-if="errors.year !== ''">{{ errors.year }}</div>
            </div>
            <div class="px-4">
              <label class="text-primary" for="cvv">CVV</label>
              <input v-model="cvv" v-bind="cvvProps" type="text" id="cvv" placeholder="000" maxlength="3"
                     :class="{ '!border-b-red-100': errors.cvv !== undefined }"
                     class="focus:outline-none bg-transparent w-full py-3 border-b border-b-neutral-50 focus:border-b-primary disabled:border-b-neutral-30 placeholder:text-neutral-30 disabled:text-neutral-30 focus:placeholder:text-neutral-90">
              <div class="text-red pl-3" v-if="errors.cvv !== ''">{{ errors.cvv }}</div>
            </div>
            <div class="px-4">
              <Button type="submit" class="bg-primary w-full text-white"
                      :disabled="disabled">Agregar
              </Button>
            </div>
          </form>
        </template>
      </Modal>
    </teleport>
    <teleport to="body">
      <Alert v-model="show_alert" :type="type_alert">{{ message_alert }}</Alert>
    </teleport>
  </div>
</template>
<script lang="ts" setup>
import {ref, watch} from 'vue'
import Button from "@/components/Button.vue"
import Modal from "@/components/Modal.vue"
import Alert from "@/components/Alert.vue"
import {useCartStore} from '@/stores/cart'
import {usePaymentStore, useOrderStore} from "../stores/checkout";
import {storeToRefs} from "pinia";
import {useRouter} from 'vue-router'

const router = useRouter()
const cart = useCartStore()
const store = usePaymentStore()
const orderStore = useOrderStore()
const {
  number, numberProps,
  name, nameProps,
  month, monthProps,
  year, yearProps,
  cvv, cvvProps, errors, disabled, show, cards
} = storeToRefs(store)
const monthHTML = ref<HTMLHtmlElement | null>(null)
const yearHTML = ref<HTMLHtmlElement | null>(null)
const selected = ref<number>()
const type_alert = ref('success')
const message_alert = ref<string>('')
const show_alert = ref<boolean>(false)


if (orderStore.order.client.id === 0) {
  router.push({'name': 'address'})
}

store.listCards()

const showModal = () => {
  show.value = true
}
const inputMonth = (e) => {
  if (month.value.length >= 2 && yearHTML.value !== null) {
    yearHTML.value.focus()
  }
}

const routerPush = () => {
  if (cards.value.length > 0 && selected.value !== undefined) {
    router.push({name: 'confirm'})
  } else {
    type_alert.value = 'error'
    message_alert.value = 'Seleccione una tarjeta'
    show_alert.value = true
  }
}

const parseNumber = (text) => {
  return text? text.substring(0,4) + ' **** **** ****': ''
}

watch(() => number.value, () => {
  number.value = number.value.replace(/\D/g, '')
})

watch(() => month.value, () => {
  month.value = month.value.replace(/\D/g, '')
})

watch(() => year.value, () => {
  year.value = year.value.replace(/\D/g, '')
})

watch(() => cvv.value, () => {
  cvv.value = cvv.value.replace(/\D/g, '')
})
</script>
