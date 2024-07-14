<template>
  <div class="flex justify-center items-center min-h-screen">
    <div>
      <div class="p-4 bg-neutral-00 rounded-2xl mb-5">
        <RouterView />
      </div>
      <div class="flex gap-4 w-full">
        <Button :class="{'btn-primary':route.name==='login'}" @click="router.push({name:'login'})">Tengo una cuenta</Button>
        <Button :class="{'btn-primary':route.name==='register'}" @click="router.push({name:'register'})">Regsitrate</Button>
      </div>
    </div>
  </div>
</template>
<script lang="ts" setup>
import {useRouter,useRoute} from 'vue-router'
import Button from '@/components/Button.vue'

const route = useRoute()
const router = useRouter()
</script>