export default {
    name: 'profile',
    component: () => import('../layouts/ProfileLayout.vue'),
    children: [
        {
            path: '',
            name: 'home_profile',
            component: () => import('../views/ProfileView.vue')
        },
    ]
}