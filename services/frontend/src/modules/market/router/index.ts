export default {
    name: 'market',
    component: () => import('../layouts/MarketLayout.vue'),
    children: [
        {
            path: 'featured',
            name: 'featured',
            component: () => import('../views/FeaturedView.vue')
        },
        {
            path: 'collection',
            name: 'collection',
            component: () => import('../views/CollectionView.vue')
        },
        {
            path: 'stores',
            name: 'stores',
            component: () => import('../views/StoresView.vue')
        },
    ]
}