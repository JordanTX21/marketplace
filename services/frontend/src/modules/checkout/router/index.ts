export default {
    name: 'checkout',
    component: () => import('../layouts/CheckoutLayout.vue'),
    children: [
        {
            path: 'address',
            name: 'address',
            component: () => import('../views/AddressView.vue')
        },
        {
            path: 'payment',
            name: 'payment',
            component: () => import('../views/PaymentView.vue')
        },
        {
            path: 'confirm',
            name: 'confirm',
            component: () => import('../views/ConfirmView.vue')
        },
    ],
    meta: { requiresAuth: true },
}