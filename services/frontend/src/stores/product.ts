import { ref } from 'vue'
import { defineStore } from 'pinia'
import Request from '@/utils/request';
import { useLoginStore } from '@/modules/auth/stores/login'

const request = new Request();

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
    price: number
}


export const useProductStore = defineStore('product', () => {
    const product = ref<Product>({
        id: 0,
        code: "",
        name: "",
        description: "",
        image: "",
        images: [],
        categories: [],
        category: '',
        rating: {rate:0,count:0},
        user: {name:'',description:'',photo:''},
        created_at: "",
        price: 0
    })
    const products = ref<Product[]>([])
    const searchs = ref<string[]>([])
    const reset = () => {
        product.value = {
            id: 0,
            code: "",
            name: "",
            description: "",
            image: "",
            images: [],
            categories: [],
            category: '',
            rating: {rate:0,count:0},
            user: {name:'',description:'',photo:''},
            created_at: "",
            price: 0
        }
    }
    const get = async (code:string) => {
        reset()
        const response = await request.get(`product/${code}`)
        if(!response.success){
            return false;
        }
        product.value = response.data
    }
    const list = async () => {
        products.value = []
        const response = await request.get('product/')
        if(!response.success){
            return false;
        }
        products.value = response.data
    }
    const search = async (name:string) => {
        const login = useLoginStore()
        products.value = []
        const body = {
            name: name,
            user_id: login.userId,
        }
        const response = await request.post('product/search',body)
        searchs.value.unshift(name)
        searchs.value = Array.from(new Set(searchs.value))
        if(!response.success){
            return false;
        }
        products.value = response.data
    }

    return { product, products, searchs, get, list, search }
})
