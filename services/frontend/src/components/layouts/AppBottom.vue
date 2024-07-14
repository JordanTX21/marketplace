<template>
    <div class="min-h-screen">
        <div class="h-[calc(100vh-52px)] overflow-y-auto bg-white">
            <slot></slot>
        </div>
        <BottomBar />
    </div>
</template>
<script lang="ts" setup>
import BottomBar from './BottomBar.vue'
</script>