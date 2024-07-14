<template>
    <div class="w-full flex fixed top-0 z-10 bg-white px-3">
        <Button class="flex flex-col items-center justify-center !px-3" @click="router.push({name:'home_inbox'})">
            <IconInbox class="w-5 stroke-neutral-80" />
        </Button>
        <div class="p-3 flex-1 text-neutral-90 font-semibold text-lg text-center">Feed</div>
        <Button class="flex flex-col items-center justify-center !px-3" @click="router.push({ name: 'search' })">
            <IconSearch class="w-5 fill-neutral-80" />
        </Button>
    </div>
</template>
<script lang="ts" setup>
import Button from '@/components/Button.vue'
import { useRouter } from 'vue-router'

const router = useRouter()
</script>