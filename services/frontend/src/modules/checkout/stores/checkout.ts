import {ref} from 'vue'
import {defineStore} from 'pinia'
import * as Yup from 'yup'
import Request from '@/utils/request'
import {useForm} from 'vee-validate'
import UserSingleton from '@/stores/user';

const request = new Request()
const _userSingleton = UserSingleton.getInstance();
const user = _userSingleton.getData()

const clientSchema = Yup.object({
    type_document: Yup.string().required(),
    document: Yup.string().required(),
    name: Yup.string().required(),
    address: Yup.string().required(),
    email: Yup.string().required()
})

const cardSchema = Yup.object({
    name: Yup.string().required(),
    number: Yup.string().required(),
    month: Yup.string().required(),
    year: Yup.string().required(),
    cvv: Yup.string().required()
})

interface Client {
    id: number
    document: string
    name: string
    address: string
    email: string
}

interface Card {
    id: number
    name: string
    number: string
    address: string
    cvv: string
}

interface Order {
    id: number | null
    client: Client | null
    card: Card | null
}

export const useClientStore = defineStore('client', () => {
    const {errors, defineField, handleSubmit} = useForm({
        validationSchema: clientSchema
    })
    const [type_document, type_documentProps] = defineField('type_document')
    const [document, documentProps] = defineField('document')
    const [name, nameProps] = defineField('name')
    const [address, addressProps] = defineField('address')
    const [email, emailProps] = defineField('email')

    const clients = ref<Client[]>([])
    const client = ref<Client>({
        id: 0,
        document: '',
        name: '',
        email: '',
        address: ''
    })
    const disabled = ref<boolean>(false)
    const show = ref<boolean>(false)

    const saveClient = handleSubmit(async (values) => {
        disabled.value = true
        const response = await request.post('client/', {
            type_document: values.type_document,
            document: values.document,
            name: values.name,
            address: values.address,
            email: values.email,
            user_id: user.id
        })
        disabled.value = false
        if (!response.success) {
            return false
        }
        type_document.value = ''
        document.value = ''
        name.value = ''
        address.value = ''
        email.value = ''
        show.value = false
        listClients()
        return true
    })

    const listClients = async () => {
        clients.value = []
        const response = await request.get('client/', {user_id: user.id})
        if (!response.success) {
            return false
        }
        clients.value = response.data
    }

    return {
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
        errors,
        clients,
        client,
        disabled,
        show,
        saveClient,
        listClients
    }
})

export const usePaymentStore = defineStore('payment', () => {
    const {errors, defineField, handleSubmit} = useForm({
        validationSchema: cardSchema
    })
    const [number, numberProps] = defineField('number')
    const [name, nameProps] = defineField('name')
    const [month, monthProps] = defineField('month')
    const [year, yearProps] = defineField('year')
    const [cvv, cvvProps] = defineField('cvv')
    const disabled = ref<boolean>(false)
    const show = ref<boolean>(false)

    const card = ref<Card>({
        id: 0,
        name: "",
        number: "",
        mes: "",
        anio: "",
        cvv: "",
    })
    const cards = ref<Card[]>([])

    const saveCard = handleSubmit(async (values) => {
        disabled.value = true
        const response = await request.post('card/', {
            name: name.value,
            number: number.value,
            month: month.value,
            year: year.value,
            cvv: cvv.value,
            user_id: user.id
        })
        disabled.value = false
        if (!response.success) {
            return false
        }
        number.value = ''
        name.value = ''
        month.value = ''
        year.value = ''
        cvv.value = ''
        show.value = false
        listCards()
        return true
    })

    const listCards = async () => {
        cards.value = []
        const response = await request.get('card/', {user_id: user.id})
        if (!response.success) {
            return false
        }
        cards.value = response.data
    }
    return {
        number, numberProps,
        name, nameProps,
        month, monthProps,
        year, yearProps,
        cvv, cvvProps, errors, disabled, show, cards, saveCard, listCards
    }
})

export const useOrderStore = defineStore('order', () => {
    const disabled = ref<boolean>(false)
    const order = ref<Order>({
        id: 0,
        card: null,
        client: {
            id: 0,
            document: '',
            name: '',
            email: '',
            address: ''
        }
    })

    const saveClient = (client: Client) => {
        order.value.client = client
    }
    const saveCard = (card: Card) => {
        order.value.card = card
    }

    const saveOrder = async (products: any, amount: any, quantity: any) => {
        disabled.value = true
        const response = await request.post('order/', {
            client_id: order.value.client!==null?order.value.client.id:0,
            user_id: user.id,
            products: products,
            amount: amount,
            quantity: quantity,
        })
        disabled.value = false
        if (!response.success) {
            return false
        }
        return true
    }

    return {
        order,
        disabled, saveOrder, saveClient, saveCard
    }
})