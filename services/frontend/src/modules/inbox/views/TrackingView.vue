<template>
    <div class="bg-white pt-[52px]">
        <div class="w-full flex items-center gap-2 fixed top-0 z-10 px-3 bg-white">
            <Button class="flex flex-col items-center justify-center !px-3" @click="router.back()">
                <IconArrowLeft class="w-6 stroke-neutral-80" />
            </Button>
            <div class="flex-1 text-neutral-90 font-semibold text-lg">
                Order tracking
            </div>
        </div>
        <div class="">
            <div class="flex flex-col gap-y-6 py-6">
                <div class="flex justify-center">
                    <img class="w-24 h-32 rounded-xl object-cover"
                        src="https://i.pinimg.com/originals/07/37/1a/07371a0783400a01c20701d139857643.png"
                        alt="Bershka Mom Jeans">
                </div>
                <div class="flex justify-center gap-1">
                    <div>
                        <div class="text-neutral-90 text-lg truncate">Bershka Mom Jeans</div>
                        <div class="text-neutral-60 text-sm">26 - S | Blue | ID:0706502</div>
                    </div>
                </div>
            </div>
        </div>
        <div class="flex flex-col gap-y-6">
            <div class="px-6">
                <div class="h-1 bg-primary-20 flex items-center relative">
                    <div class="flex justify-between w-full">
                        <div class="rounded-full w-3.5 h-3.5 bg-primary"></div>
                        <div class="rounded-full w-3.5 h-3.5 bg-primary"></div>
                        <div class="rounded-full w-3.5 h-3.5 bg-primary"></div>
                        <div class="rounded-full w-3.5 h-3.5 bg-primary"></div>
                    </div>
                    <div class="absolute top-0 left-0 w-full">
                        <div class="bg-primary h-1 w-2/3"></div>
                    </div>
                </div>
            </div>
            <div class="px-6">
                <div class="text-neutral-90 font-semibold text-xl">Your package is on it’s way</div>
                <div class="text-base text-neutral-70">Arrival estimate: April 15</div>
            </div>
            <div class="pt-3 pb-4 px-6">
                <div class="py-2">
                    <div class="text-base text-neutral-90">Your package is near!</div>
                    <div class="text-sm text-neutral-60">April 15, 12:05</div>
                </div>
                <div class="py-2">
                    <div class="text-base text-neutral-90">Your package is near!</div>
                    <div class="text-sm text-neutral-60">April 15, 12:05</div>
                </div>
                <div class="py-2">
                    <div class="text-base text-neutral-90">Your package is near!</div>
                    <div class="text-sm text-neutral-60">April 15, 12:05</div>
                </div>
            </div>
            <div class="py-2 px-6">
                <Button class="border w-full">Cancel order</Button>
            </div>
            <hr >
            <div class="pt-3 pb-4 px-6">
                <div class="py-2">
                    <div class="text-base text-neutral-90">Shipping info</div>
                </div>
                <div class="py-2">
                    <div class="text-base text-neutral-60">Order Address</div>
                    <div class="text-base text-neutral-90">3910 Crim Lane, Greendale County, Colorado. Zip Code 410348</div>
                </div>
                <div class="py-2">
                    <div class="text-base text-neutral-60">Receives</div>
                    <div class="text-base text-neutral-90">Ava Johnson</div>
                </div>
                <div class="py-2">
                    <div class="text-base text-neutral-60">Tracking ID</div>
                    <div class="text-base text-neutral-90">0706502</div>
                </div>
            </div>
            <hr>
            <div class="flex gap-x-2 py-2.5 px-6">
                <div class="flex-1 text-base text-neutral-90 font-semibold">Report a problem</div>
                <div>
                    <IconReportTriangle class="stroke-neutral-80"/>
                </div>
            </div>
            <div class="flex gap-x-2 py-2.5 px-6">
                <div class="flex-1 text-base text-neutral-90 font-semibold">Share order</div>
                <div>
                    <IconShare class="fill-neutral-80"/>
                </div>
            </div>
            <hr>
        </div>
    </div>
</template>
<script lang="ts" setup>
import Button from '@/components/Button.vue';
import { useRouter } from 'vue-router'

const router = useRouter()
</script>