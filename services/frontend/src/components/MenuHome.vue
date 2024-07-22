<template>
    <div class="px-6 pt-2 pb-0.5 flex gap-4 bg-white">
        <div  v-for="(item,index) in menu" :key="`item-menu-home-${index}`" @click="toggleActive(item)" class="cursor-pointer">
            <div class="text-base font-semibold " :class="{'text-neutral-90':item.status,'text-neutral-50':!item.status}">{{ item.name }}</div>
            <div v-if="item.status" class="text-primary text-center leading-none">•</div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import { ref } from 'vue';
import { useProductStore } from '@/stores/product'
const store = useProductStore()

const menu = ref([
    {
        name: 'Todos',
        status: true
    },
    {
        name: 'Recomendados',
        status: false
    },
])

const toggleActive = (item) => {
  for(const i of menu.value){
    i.status = i.name === item.name
  }
  if(item.name === 'Todos'){
    store.list()
  }else if(item.name === 'Recomendados'){
    store.listRecomended()
  }
}

</script>