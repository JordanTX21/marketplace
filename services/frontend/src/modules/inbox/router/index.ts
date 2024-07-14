export default {
    name: 'inbox',
    component: () => import('../layouts/InboxLayout.vue'),
    children: [
        {
            path: '',
            name: 'home_inbox',
            component: () => import('../views/InboxView.vue')
        },
        {
            path: 'oreder_review',
            name: 'oreder_review',
            component: () => import('../views/OrderReviewView.vue')
        },
        {
            path: 'tracking',
            name: 'tracking',
            component: () => import('../views/TrackingView.vue')
        },
    ],
    meta: { requiresAuth: true },
}