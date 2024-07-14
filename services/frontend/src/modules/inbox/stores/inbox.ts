import {ref} from 'vue'
import {defineStore} from 'pinia'
import * as Yup from 'yup'
import Request from '@/utils/request'
import {useForm} from 'vee-validate'
import UserSingleton from '@/stores/user';

const request = new Request()
const _userSingleton = UserSingleton.getInstance();
const user = _userSingleton.getData()

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

interface Order {
    id: number
    quantity: number
    amount: number
    client: Client
    user_id: number
    states: OrderState[]
    created_at: string
}

export const useOrderStore = defineStore('order_inbox', () => {
    const orders = ref<Order[]>([])

    const listOrders = async () => {
        orders.value = []
        const response = await request.get('order/', {user_id: user.id})
        if (!response.success) {
            return false
        }
        orders.value = response.data
    }

    return { orders, listOrders }
})