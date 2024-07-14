<script setup lang="ts">
import NavMarket from '../components/NavMarket.vue'
import MenuMarket from '../components/MenuMarket.vue'
import Button from '@/components/Button.vue'
import { onMounted, onUnmounted, ref } from 'vue'
import { useRouter } from 'vue-router'

const showSearch = ref(false)
const targetDiv = ref<HTMLDivElement | null>(null)
const router = useRouter()

const handleScroll = () => {
  if (targetDiv.value) {
    const rect = targetDiv.value.getBoundingClientRect();
    // Ajusta este valor según la posición deseada
    // const scrollPosition = window.innerHeight / 3;
    showSearch.value = rect.top < -70;
  }
};

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
  handleScroll();
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
})
</script>

<template>
  <div ref="targetDiv">
    <NavMarket :showSearch="showSearch" />
    <div class="flex flex-col gap-y-4 pt-6 pb-5">
      <div class="text-3xl text-neutral-90 font-extrabold text-center px-6">Market</div>
      <div class="flex gap-x-2 px-6">
        <div class="flex-1 flex px-4 py-3 bg-neutral-05 rounded-xl text-neutral-90 cursor-pointer"
          @click="router.push({ name: 'search' })">
          <div class="bg-transparent w-full text-neutral-60" type="text">Search on Tassel</div>
          <IconSearch class="w-5 fill-neutral-50" />
        </div>
        <Button class="border !font-extrabold">W</Button>
      </div>
      <div class="px-6">
        <MenuMarket />
      </div>
    </div>
    <RouterView />
  </div>
</template>
