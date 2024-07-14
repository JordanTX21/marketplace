<template>
    <div class="w-full flex gap-2 fixed top-0 z-10 bg-white px-3">
        <Button class="flex flex-col items-center justify-center !px-3" @click="router.push({name:'home_inbox'})">
            <IconInbox class="w-5 stroke-neutral-80" />
        </Button>
        <div class="flex-1 flex px-4 py-3 bg-neutral-05 rounded-xl text-neutral-90 cursor-pointer"
            v-if="props.showSearch" @click="router.push({ name: 'search' })">
            <div class="bg-transparent w-full text-neutral-60" type="text">Search on Tassel</div>
            <IconSearch class="w-5 fill-neutral-50" />
        </div>
        <Button class="!font-extrabold" v-if="props.showSearch">W</Button>
    </div>
</template>
<script lang="ts" setup>
import Button from '@/components/Button.vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const props = defineProps({
    showSearch: {
        default: false,
        type: Boolean,
    }
})
</script>