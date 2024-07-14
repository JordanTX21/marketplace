<template>
    <div>
        <div class="w-full flex fixed top-0 z-10 bg-white px-3">
            <Button class="flex flex-col items-center justify-center !px-3" @click="router.back()">
                <IconArrowLeft class="w-5 stroke-neutral-80" />
            </Button>
        </div>
        <div class="flex flex-col py-6 gap-4">
            <div class="flex flex-col gap-4 justify-center px-6">
                <div class="flex justify-center">
                    <img class="rounded-full border-4 border-neutral-10 w-28" :src="store.avatar" :alt="store.title">
                </div>
                <div class="flex justify-center">
                    <div class="pb-2">
                        <div class="text-center text-neutral-90 font-extrabold text-3xl">{{ store.title }}</div>
                        <div class="text-center text-neutral-60">{{ store.description }}</div>
                    </div>
                </div>
            </div>
            <div class="flex gap-x-2 px-6 justify-center">
                <Button class="border">10 Following</Button>
                <Button class="bg-primary text-white"><IconSettings class="fill-white"/></Button>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import Button from '@/components/Button.vue'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const store = ref({
    id: 1,
    title: "Ava Johnson",
    description: "@avajohnson",
    avatar: 'https://www.befunky.com/images/wp/wp-2021-01-linkedin-profile-picture-after.jpg?auto=avif,webp&format=jpg&width=944'
})

</script>