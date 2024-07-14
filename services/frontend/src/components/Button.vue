<template>
  <button class="rounded-xl px-4 py-3 font-semibold focus:ring-0 flex items-center justify-center">
    <Spin v-if="$attrs.disabled && props.load" class="h-5 w-5 text-white"/>
    <slot v-else></slot>
  </button>
</template>
<script setup lang="ts">
import Spin from '@/components/Spin.vue'
import {defineProps} from 'vue'

const props = defineProps({
  load: {
    type: Boolean,
    default: true
  }
})
</script>