<template>
    <div class="px-5">
        <div class="flex flex-col gap-y-3">
            <div class="grid grid-cols-2 overflow-y-hidden" :class="{ 'h-64': btnStatus === 'more' }">
                <div class="p-1" v-for="(item, index) in collections" :key="`collections-${index}`">
                    <div class="h-24 text-lg px-3 py-2 rounded-xl flex items-end" :class="[item.bg, item.text]">
                        <div :class="[item.text, 'text-lg']">{{ item.title }}</div>
                    </div>
                </div>
            </div>
            <Button class="border flex justify-center items-center w-full" @click="toggleStatus">
                <IconChevronDown class="stroke-neutral-80" v-if="btnStatus === 'more'" />
                <IconChevronUp class="stroke-neutral-80" v-else /> Show {{ btnStatus }}
            </Button>
        </div>
        <div class="py-4 flex flex-col gap-y-3">
            <div class="text-xl text-neutral-90">Frequently visited</div>
            <div>
                <div class="py-3" v-for="(item,index) in frequently" :key="`frequently-${index}`">
                    <div class="flex gap-4">
                        <img class="rounded-xl w-12 h-12 object-cover" :src="item.img" :alt="item.title">
                        <div>
                            <div class="text-neutral-90">{{ item.title }}</div>
                            <div class="text-neutral-50">{{ item.collection }}</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import { ref } from "vue";
import Button from '@/components/Button.vue'

const btnStatus = ref('more')

const frequently = ref([
    {
        title: 'Dresses',
        img: 'https://images-cdn.ubuy.co.in/65564d4e2c4e15509810f25b-cdress-women-39-s-short-homecoming.jpg',
        collection: 'Clothing'
    },
    {
        title: 'Dresses',
        img: 'https://images-cdn.ubuy.co.in/65564d4e2c4e15509810f25b-cdress-women-39-s-short-homecoming.jpg',
        collection: 'Clothing'
    },
    {
        title: 'Dresses',
        img: 'https://images-cdn.ubuy.co.in/65564d4e2c4e15509810f25b-cdress-women-39-s-short-homecoming.jpg',
        collection: 'Clothing'
    },
    {
        title: 'Dresses',
        img: 'https://images-cdn.ubuy.co.in/65564d4e2c4e15509810f25b-cdress-women-39-s-short-homecoming.jpg',
        collection: 'Clothing'
    },
    {
        title: 'Dresses',
        img: 'https://images-cdn.ubuy.co.in/65564d4e2c4e15509810f25b-cdress-women-39-s-short-homecoming.jpg',
        collection: 'Clothing'
    },
    {
        title: 'Dresses',
        img: 'https://images-cdn.ubuy.co.in/65564d4e2c4e15509810f25b-cdress-women-39-s-short-homecoming.jpg',
        collection: 'Clothing'
    },
])

const collections = ref([
    {
        title: 'On sale',
        bg: 'bg-red-10',
        text: 'text-red'
    },
    {
        title: 'New in',
        bg: 'bg-primary-10',
        text: 'text-primary'
    },
    {
        title: 'Clothing',
        bg: 'bg-neutral-05',
        text: 'text-neutral-90'
    },
    {
        title: 'Shoes',
        bg: 'bg-neutral-05',
        text: 'text-neutral-90'
    },
    {
        title: 'Accessories',
        bg: 'bg-neutral-05',
        text: 'text-neutral-90'
    },
    {
        title: 'Sport',
        bg: 'bg-neutral-05',
        text: 'text-neutral-90'
    },
    {
        title: 'Personal Care',
        bg: 'bg-neutral-05',
        text: 'text-neutral-90'
    },
    {
        title: 'Collabs',
        bg: 'bg-neutral-05',
        text: 'text-neutral-90'
    },
])

function toggleStatus() {
    if (btnStatus.value === 'more') {
        btnStatus.value = 'less'
    } else {
        btnStatus.value = 'more'
    }
}
</script>