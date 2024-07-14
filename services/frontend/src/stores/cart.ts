import { ref } from 'vue'
import { defineStore } from 'pinia'
// import Request from '@/utils/request';

// const request = new Request();

interface User {
    name: string,
    description: string,
    photo: string
}

interface Rate {
    rate: number,
    count: number
}

interface Product {
    id: number,
    code: string,
    name: string,
    description: string,
    image: string,
    images: Array<string>,
    categories: Array<string>,
    category: string,
    rating: Rate,
    user: User,
    created_at:string,
    quantity: number | null,
    amount: number | null,
    price: number
}

export const useCartStore = defineStore('cart', () => {
    const products = ref<Product[]>([])

    const list = () => {
        const prods = localStorage.getItem('products')
        products.value = prods? JSON.parse(prods) : []
    }

    const save = () => localStorage.setItem('products',JSON.stringify(products.value))

    const add = (product: Product) => {
        const prod = products.value.filter(prod => prod.code === product.code)
        if(prod.length === 0){
            products.value.push(product)
        }else{
            const index = products.value.indexOf(prod[0])
            products.value[index].quantity++;
        }
        save()
    }
    const remove = (code: string) => {
        products.value = products.value.filter(product => product.code !== code)
        save()
    }
    const total = ():number => products.value.reduce((acumulador, product:Product) => acumulador + product.price, 0)
    const quantity = ():number => products.value.reduce((acumulador, product:Product) => acumulador + product.quantity, 0)
    const reset = () => {
        products.value = []
        save()
    }
    return {products,add,remove,total,reset,quantity,list}
})