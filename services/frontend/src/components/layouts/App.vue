<template>
    <div class="min-h-screen">
        <div class="min-h-[calc(100vh-52px)] py-[52px] bg-white">
            <slot></slot>
        </div>
        <BottomBar />
    </div>
</template>
<script lang="ts" setup>
import BottomBar from './BottomBar.vue'
</script>