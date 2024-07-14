import { ref } from 'vue'
import { defineStore } from 'pinia'
import Request from '@/utils/request';

const request = new Request();

interface Product {
    id: number,
    title: string,
    image: string,
    price: number
}


export const useHomeStore = defineStore('home', () => {
    const products = ref<Product[]>([])
    const search = async () => {
        products.value = []
        const response = await request.get('product/')
        if(!response.success){
            return false;
        }
        products.value = response.data
    }

    return { products, search }
})
