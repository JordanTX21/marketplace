import {ref} from 'vue'
import {defineStore} from 'pinia'
import * as Yup from 'yup'
import Request from '@/utils/request'
import {useForm} from 'vee-validate'
import UserSingleton from '@/stores/user';
import {useRouter} from 'vue-router'

const request = new Request()
const _userSingleton = UserSingleton.getInstance();
const user = _userSingleton.getData()
const router = useRouter()

interface Client {
    id: number
    document: string
    name: string
    address: string
    email: string
}

interface OrderState {
    id: number
    state: string
    order_id: number
    created_at: string
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
    created_at:string,
    price: number
}

interface Order {
    id: number
    quantity: number
    amount: number
    client: Client
    user_id: number
    states: OrderState[]
    products: Product[]
    created_at: string
    status: boolean
}

export const useOrderStore = defineStore('order_inbox', () => {
    const orders = ref<Order[]>([])
    const order = ref<Order>({
        id: 0,
        quantity: 0,
        amount: 0,
        client: {
            id: 0,
            document: "",
            name: "",
            address: "",
            email: "",
        },
        user_id: 0,
        states: [],
        products: [],
        created_at: ''
    })
    const reset = () => {
        orders.value = []
        order.value = {
            id: 0,
            quantity: 0,
            amount: 0,
            client: {
                id: 0,
                document: "",
                name: "",
                address: "",
                email: "",
            },
            user_id: 0,
            states: [],
            products: [],
            created_at: ''
        }
    }

    const listOrders = async () => {
        reset()
        const response = await request.get('order/', {user_id: user.id})
        if (!response.success) {
            return false
        }
        orders.value = response.data
        order.value = response.data[0]
    }

    const getOrder = async (id:number) => {
        reset()
        const response = await request.get(`order/${id}`)
        if (!response.success) {
            return false
        }
        order.value = response.data
    }

    const deleteOrder = async (id:number) => {
        const response = await request.delete(`order/${id}`)
        if (!response.success) {
            return false
        }
        reset()
        router.push({name: 'home_inbox'})
        return true
    }

    return { order, orders, listOrders, getOrder, deleteOrder }
})