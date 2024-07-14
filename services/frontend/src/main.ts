import './assets/main.css'

import { createApp, defineAsyncComponent } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'

import router from './router'

const app = createApp(App)

const iconsList = [
    'IconArrowLeft',
    'IconArrowRight',
    'IconBookmark',
    'IconCart',
    'IconCheck',
    'IconChevronDown',
    'IconChevronUp',
    'IconCommunity',
    'IconDeleteText',
    'IconDocumentation',
    'IconEcosystem',
    'IconExit',
    'IconHome',
    'IconInbox',
    'IconMarket',
    'IconMoreDots',
    'IconReportTriangle',
    'IconSearch',
    'IconSettings',
    'IconShare',
    'IconSupport',
    'IconTooling',
    'IconTrash',
    'IconUser',
]

iconsList.forEach((nameComponent) => {
    const component = defineAsyncComponent(() => import(`@/components/icons/${nameComponent}.vue`))
    app.component(nameComponent,component)
});

app.use(createPinia())
app.use(router)

app.mount('#app')
