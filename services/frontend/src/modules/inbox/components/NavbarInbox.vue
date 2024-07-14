<template>
    <div class="w-full flex gap-2 fixed top-0 z-10 px-3" :class="{'bg-white':showSearch}">
        <Button class="flex flex-col items-center justify-center !px-3" @click="router.back()">
            <IconExit class="w-6 stroke-neutral-80" />
        </Button>
        <div class="flex-1 flex items-center justify-center">
            <MenuInbox v-if="showSearch"/>
            <IconInbox class="stroke-neutral-80" v-else/>
        </div>
        <Button>
            <IconSearch class="w-5" :class="{'fill-neutral-80':showSearch}"/>
        </Button>
    </div>
</template>
<script lang="ts" setup>
import Button from '@/components/Button.vue'
import MenuInbox from '../components/MenuInbox.vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const props = defineProps({
    showSearch: {
        default: false,
        type: Boolean,
    }
})
</script>