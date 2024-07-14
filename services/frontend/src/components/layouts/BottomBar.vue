<template>
    <div class="w-full grid grid-cols-3 fixed bottom-0 bg-white">
        <Button class="flex flex-col items-center justify-center" v-for="(item, index) in bottomItems"
            :key="`bottom-item-${index}`" @click="toggleActive(item)">
            <component :is="item.icon" class="w-5 fill-neutral-50" :class="{ '!fill-primary-100': item.active }" /><span
                class="text-xs text-neutral-50" :class="{ '!text-primary-100': item.active }">{{ item.title }}</span>
        </Button>
    </div>
</template>
<script lang="ts" setup>
import Button from '@/components/Button.vue'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const bottomItems = ref([
    {
        title: 'Feed',
        icon: 'IconHome',
        route: 'home',
        active: true
    },
    {
        title: 'Market',
        icon: 'IconMarket',
        route: 'featured',
        active: false
    },
    {
        title: 'Profile',
        icon: 'IconUser',
        route: 'home_profile',
        active: false
    },
])

function toggleActive(item:any){
    bottomItems.value.forEach(bt => bt.active = false)
    item.active = true
    router.push({name:item.route})
}

</script>