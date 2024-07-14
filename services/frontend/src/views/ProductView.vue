<template>
    <div class="bg-white py-[52px]">
        <div class="w-full flex fixed top-0 z-10 bg-white px-3">
            <Button class="flex flex-col items-center justify-center !px-3" @click="router.push({ name: 'home' })">
                <IconArrowLeft class="w-5 stroke-neutral-80" />
            </Button>
            <div class="p-3 flex-1 text-neutral-90 font-semibold text-lg text-center"></div>
            <Button class="flex flex-col items-center justify-center !px-3">
                <IconBookmark class="w-5 fill-neutral-80" />
            </Button>
            <Button class="flex flex-col items-center justify-center !px-3">
                <IconMoreDots class="w-5 fill-neutral-80 stroke-neutral-80" />
            </Button>
        </div>
        <div class="flex flex-col gap-y-4">
            <div class="flex w-full overflow-x-auto pl-6 gap-1">
                <img class="h-[396px] rounded-xl" :src="item" :alt="`product-img-${index}`"
                    v-for="(item, index) in product.images" :key="`product-img-${index}`">
            </div>
            <div class="px-6 py-2">
                <div class="flex flex-col gap-1">
                    <div class="flex items-center gap-x-6">
                        <div class="flex-1 text-neutral-90 text-xl">{{ store.product.user.name }}</div>
                        <img v-if="store.product.user.photo != null"
                            class="rounded-full border-2 border-neutral-10 w-10" :src="store.product.user.photo"
                            :alt="store.product.user.name">
                    </div>
                    <div class="text-neutral-100 font-semibold text-xl">${{ product.price }}</div>
                </div>
            </div>
        </div>
        <div class="px-6 py-2">
            <div class="flex justify-between gap-2 border border-neutral-10 text-neutral-80 rounded-xl">
                <Button @click="quantity = Math.max(1, quantity - 1)">-</Button>
                <input v-model="quantity" type="number"
                    class="focus:outline-none bg-transparent w-full placeholder:text-neutral-60 text-center" min="1"
                    setp="1">
                <Button @click="quantity++">+</Button>
            </div>
        </div>
        <hr class="my-4">
        <div class="flex flex-col gap-3 py-4">
            <div class="px-6 text-neutral-90 text-xl">Detalles</div>
            <div class="flex flex-col gap-1 px-6 py-2">
                <div class="text-neutral-90 font-semibold">Descripción</div>
                <div class="text-neutral-70">
                    <div v-text="product.description"></div>
                    <div v-for="(category, categoryIndex) in product.categories" :key="`category-${categoryIndex}`">- {{
                category }}</div>
                </div>
            </div>
        </div>
        <hr class="my-4">
        <div class="pl-6">
            <div class="flex gap-4 py-2.5">
                <div class="flex-1 text-lg font-semibold text-neutral-90">Productos relacionados</div>
            </div>
            <div class="">
                <div class="w-full flex overflow-x-auto">
                    <div class="flex flex-col gap-3 p-1" v-for="(item, index) in products"
                        :key="`products-item-${index}`"
                        @click="router.push({ name: 'product', params: { code: item.code } })">
                        <div class="relative w-40 h-48 rounded-xl">
                            <img class="object-cover w-40 h-48 rounded-xl" :src="item.image" :alt="item.code">
                        </div>
                        <div>
                            <div class="text-neutral-90">{{ item.name }}</div>
                            <div class="flex gap-1">
                                <div class="text-neutral-60">${{ item.price }}</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <hr class="my-4">
        <div class="fixed bottom-14 px-3 py-2 w-full bg-primary" v-if="cart.products.length>0">
            <div class="flex gap-x-3">
                <div class="flex flex-1 items-center gap-x-1 text-white">
                    <div class="p-3">
                        <IconCart class="w-5 h-5 fill-white" />
                    </div>
                    Carrito de compras
                </div>
                <div class="flex items-center justify-end">
                    <div class="text-primary bg-white px-1.5 py-0.5 rounded"> {{ cart.quantity() }} productos</div>
                    <Button @click="router.push({name:'cart'})">
                        <IconArrowRight class="w-5 stroke-white" />
                    </Button>
                </div>
            </div>
        </div>
        <div class="fixed bottom-0 px-6 py-1 w-full bg-white">
            <Button class="bg-primary text-white w-full" @click="add">Agregar al carrito</Button>
        </div>
        <teleport to="body">
            <Alert v-model="showAlert">
                <IconCheck class="w-4 h-4 fill-green-100" /><span class="font-semibold">Correcto: </span> Producto
                Agregado al carrito
            </Alert>
        </teleport>
    </div>
</template>
<script lang="ts" setup>
import Alert from "@/components/Alert.vue"
import Button from "@/components/Button.vue"
import { onMounted, ref, watch } from "vue"
import { useRouter, useRoute } from 'vue-router'
import { useProductStore } from '@/stores/product'
import { useCartStore } from '@/stores/cart'
import { storeToRefs } from "pinia";

const router = useRouter()
const route = useRoute()
const store = useProductStore()
const cart = useCartStore()
const quantity = ref<number>(1)

const { product, products } = storeToRefs(store)
const showAlert = ref(false)

const add = async () => {
    showAlert.value = true
    cart.add({ ...product.value, amount: quantity.value * product.value.price, quantity: quantity.value })
}

onMounted(() => {
    store.get(route.params.code.toString())
})

watch(() => route.params.code, (newCode, oldCode) => {
    store.get(route.params.code.toString())
})

</script>