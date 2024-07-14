<template>
    <div class="relative inline-block text-left w-full" ref="selectDropdown">
        <div>
            <input v-model="inputModel" type="text" :placeholder="props.placeholder" @input="input" @focus="showOptions"
                class="focus:outline-none bg-transparent w-full py-3 border-b border-b-neutral-50 focus:border-b-primary disabled:border-b-neutral-30 placeholder:text-neutral-30 disabled:text-neutral-30 focus:placeholder:text-neutral-90">
        </div>
        <transition enter-active-class="transition ease-out duration-100"
            enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100"
            leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100"
            leave-to-class="transform opacity-0 scale-95">
            <div v-show="show" class="absolute right-0 z-20 origin-top-right w-full" role="menu" aria-orientation="vertical"
                aria-labelledby="menu-button" tabindex="-1">
                <div class="bg-white rounded-xl flex flex-col shadow-lg" role="none">
                    <div v-for="(item, index) in optionsValues" :key="`${props.placeholder}-${index}`" class="p-3 cursor-pointer hover:bg-neutral-10 rounded"
                        @click="select(item)">
                        {{ item.label }}
                    </div>
                    <div v-if="optionsValues.length === 0"
                        class="p-2 m-2 rounded-lg text-xs font-medium text-zinc-300 w-[100% - 0.5rem] select-none">Sin
                        resultados</div>
                </div>
            </div>
        </transition>
    </div>
</template>
<script lang="ts" setup>
import { computed, onBeforeUnmount, onMounted, ref, watch } from "vue"

interface Option {
    value: string,
    label: string
}

const emit = defineEmits(['input', 'select', 'clear', 'showOptions', 'update:modelValue'])

const props = defineProps({
    options: {
        type: Array<Option>,
        default: () => [],
    },
    placeholder: {
        type: String,
        default: "",
    },
    validate: {
        type: Boolean,
        default: false,
    },
    name: {
        type: String,
        default: "",
    },
    disabled: {
        type: Boolean,
        default: false,
    },
})

const model = defineModel({
    default: {
        value: '',
        label: '',
    }
})

const show = ref(false)
const selectDropdown = ref<HTMLElement>()
const inputModel = ref(model.value.label)
const option = ref<Option>()

function input(e:any) {
    if (e.target.value === '') {
        clear()
    }
    // optionsValues.value = props.options.filter(item => item.label.toLowerCase().includes(inputModel.value.toLowerCase()))
    emit('input', e)
}

function clear() {
    inputModel.value = ""
    option.value = undefined
    emit('clear')
    emit('update:modelValue', { value: '', label: '' })
}

function showOptions() {
    show.value = true
    emit('showOptions', show.value)
}

function select(item:Option) {
    show.value = false
    inputModel.value = item.label
    option.value = { ...item }
    emit('showOptions', show.value)
    emit('select', { ...item })
    emit('update:modelValue', { ...item })
}

function onClickOutside(event:any) {
    // Esta función se ejecutará cuando se haga clic fuera del div
    const div = selectDropdown.value;
    if (div && !div.contains(event.target)) {
        show.value = false
        emit('showOptions', show.value)
    }
}
onMounted(() => {
    document.addEventListener('click', onClickOutside);
})
onBeforeUnmount(() => {
    document.removeEventListener('click', onClickOutside);
})

const optionsValues = computed(() => {
    let opciones = props.options
    if (inputModel.value && !option.value) {
        opciones = props.options.filter(item => item.label.toLowerCase().includes(inputModel.value.toLowerCase()))
    }
    return opciones
})


watch(model, (newValue, oldValue) => {
    inputModel.value = newValue.label
})

</script>
