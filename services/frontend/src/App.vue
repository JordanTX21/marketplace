<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Theme from '@/components/layouts/Theme.vue'
import PreLoader from '@/components/PreLoader.vue'
import { useLoaderState } from "@/stores/isloading";
const isLoading = useLoaderState();
</script>

<template>
  <Theme>
    <teleport to="body">
      <PreLoader v-if="isLoading.state"></PreLoader>
    </teleport>
    <RouterView />
  </Theme>
</template>

<style scoped></style>
