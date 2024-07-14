<template>
    <div class="px-6 pt-2 pb-0.5 flex gap-4 bg-white">
        <div class="cursor-pointer" v-for="(item,index) in menu" :key="`item-menu-home-${index}`" @click="toggleActive(item)">
            <div class="text-base font-semibold " :class="{'text-neutral-90':item.active,'text-neutral-50':!item.active}">{{ item.name }}</div>
            <div v-if="item.active" class="text-primary text-center leading-none">•</div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router'

const router = useRouter()

const menu = ref([
    {
        name: 'Featured',
        route: 'featured',
        active: true
    },
    {
        name: 'Collection',
        route: 'collection',
        active: false
    },
    {
        name: 'Stores',
        route: 'stores',
        active: false
    },
])

function toggleActive(item:any){
    menu.value.forEach(bt => bt.active = false)
    item.active = true
    router.push({name:item.route})
}

</script>