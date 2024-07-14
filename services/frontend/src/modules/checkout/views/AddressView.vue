<template>
  <div>
    <div class="px-6 py-6 text-xl text-neutral-90">Seleccione o agregue una direccion</div>
    <div>
      <div>
        <div v-for="(item, index) in clients" :key="`address-${index}`"
             class="flex flex-col gap-y-6 rounded-xl py-6 my-1 mx-2"
             :class="{ 'bg-primary-10': item.id === selected }">
          <label :for="`hs-radio-group-${index}`" class="flex items-center justify-between cursor-pointer" @click="orderStore.saveClient({...item})">
            <div class="px-4">
              <div class="text-base text-neutral-90 font-semibold">{{ item.name }}</div>
              <div class="text-base text-neutral-70">{{ item.address }}</div>
              <div class="text-base text-primary">Fecha: {{ moment().format("MMM Do") }}</div>
            </div>
            <div class="flex">
              <input type="radio" name="hs-radio-group" v-model="selected"
                     class="form-radio shrink-0 mt-0.5 border-gray-200 rounded-full text-primary focus:ring-primary disabled:opacity-50 disabled:pointer-events-none dark:bg-gray-800 dark:border-gray-700 dark:checked:bg-primary dark:checked:border-primary dark:focus:ring-offset-gray-800"
                     :id="`hs-radio-group-${index}`" :value="item.id">
              <label :for="`hs-radio-group-${index}`"
                     class="text-sm text-gray-500 ms-2 dark:text-gray-400"></label>
            </div>
          </label>
          <!-- <Button class="border-t" v-if="item.id==selected">Edit</Button> -->
        </div>
      </div>
      <div class="px-6 py-4">
        <Button class="border w-full" @click="showModal">Agregar direccion</Button>
      </div>
    </div>
    <div class="fixed bottom-0 w-full">
      <hr>
      <div class="flex gap-x-4 px-6 py-3">
        <div class="flex-1 text-base text-neutral-90">Subtotal</div>
        <div class="text-base font-semibold text-neutral-90">${{ cart.total() }}</div>
      </div>
      <div class="py-1 px-6">
        <Button class="bg-primary text-white w-full" @click="routerPush">Continuar</Button>
      </div>
    </div>
    <teleport to="body">
      <Modal v-model="show">
        <template #header>Agregar Direccion</template>
        <template #body>
          <form @submit="store.saveClient" class="flex flex-col gap-y-4">
            <div class="px-4">
              <DropDown v-model="dropDownVal" placeholder="Tipo de documento" :options="type_documents"
                        @select="selectType"/>
              <div class="text-red pl-3" v-if="errors.type_document != ''">{{ errors.type_document }}
              </div>
            </div>
            <div class="px-4">
              <input v-model="document" v-bind="documentProps" type="text" id="documento"
                     placeholder="Documento" :class="{ '!border-b-red-100': errors.document != '' }"
                     class="focus:outline-none bg-transparent w-full py-3 border-b border-b-neutral-50 focus:border-b-primary disabled:border-b-neutral-30 placeholder:text-neutral-30 disabled:text-neutral-30 focus:placeholder:text-neutral-90">
              <div class="text-red pl-3" v-if="errors.document != ''">{{ errors.document }}</div>
            </div>
            <div class="px-4">
              <input v-model="name" v-bind="nameProps" type="text" id="name" placeholder="Nombre"
                     :class="{ '!border-b-red-100': errors.name != '' }"
                     class="focus:outline-none bg-transparent w-full py-3 border-b border-b-neutral-50 focus:border-b-primary disabled:border-b-neutral-30 placeholder:text-neutral-30 disabled:text-neutral-30 focus:placeholder:text-neutral-90">
              <div class="text-red pl-3" v-if="errors.name != ''">{{ errors.name }}</div>
            </div>
            <div class="px-4">
              <input v-model="address" v-bind="addressProps" type="text" id="address"
                     placeholder="Direccion" :class="{ '!border-b-red-100': errors.address != '' }"
                     class="focus:outline-none bg-transparent w-full py-3 border-b border-b-neutral-50 focus:border-b-primary disabled:border-b-neutral-30 placeholder:text-neutral-30 disabled:text-neutral-30 focus:placeholder:text-neutral-90">
              <div class="text-red pl-3" v-if="errors.address != ''">{{ errors.address }}</div>
            </div>
            <div class="px-4">
              <input v-model="email" v-bind="emailProps" type="email" id="email" placeholder="Correo"
                     :class="{ '!border-b-red-100': errors.email != '' }"
                     class="focus:outline-none bg-transparent w-full py-3 border-b border-b-neutral-50 focus:border-b-primary disabled:border-b-neutral-30 placeholder:text-neutral-30 disabled:text-neutral-30 focus:placeholder:text-neutral-90">
              <div class="text-red pl-3" v-if="errors.email != ''">{{ errors.email }}</div>
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
import Button from "@/components/Button.vue"
import Modal from "@/components/Modal.vue"
import DropDown from "@/components/DropDown.vue"
import Alert from "@/components/Alert.vue"
import {ref} from "vue"
import {useRouter} from 'vue-router'
import {useClientStore, useOrderStore} from '@/modules/checkout/stores/checkout'
import {useCartStore} from '@/stores/cart'
import {storeToRefs} from "pinia"
import moment from 'moment';

const router = useRouter()
const store = useClientStore()
const orderStore = useOrderStore()
const cart = useCartStore()

const {
  type_document,
  type_documentProps,
  document,
  documentProps,
  name,
  nameProps,
  address,
  addressProps,
  email,
  emailProps,
  disabled,
  show,
  errors, clients, client
} = storeToRefs(store)

const dropDownVal = ref({value: "", label: ""})
const type_alert = ref('success')
const selected = ref<number>()
const message_alert = ref<string>('')
const show_alert = ref<boolean>(false)

const type_documents = ref([
  {value: "DNI", label: "DNI"},
  {value: "RUC", label: "RUC"},
])

store.listClients()

const showModal = () => {
  show.value = true
}

const selectType = (item: any) => {
  type_document.value = item.value
}

const routerPush = () => {
  if (clients.value.length > 0 && selected.value !== undefined) {
    client.value = clients.value.filter((item) => item.id === selected.value)[0]
    router.push({name: 'payment'})
  } else {
    type_alert.value = 'error'
    message_alert.value = 'Seleccione una direccion'
    show_alert.value = true
  }
}
</script>
