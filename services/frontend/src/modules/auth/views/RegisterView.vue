<template>
  <div>
    <div class="mb-5 text-center font-semibold text-2xl">Registro</div>
    <div>
      <form @submit="store.signup" novalidate>
        <div class="mb-5">
          <input
            v-model="name"
            v-bind="nameProps"
            class="focus:outline-none px-4 py-3 bg-neutral-05 rounded-xl text-neutral-90 placeholder:text-neutral-60 w-full"
            type="text" placeholder="Usuario">
            <div class="text-red pl-3" v-if="errors.name">{{errors.name}}</div>
        </div>
        <div class="mb-5">
          <input
            v-model="email"
            v-bind="emailProps"
            class="focus:outline-none px-4 py-3 bg-neutral-05 rounded-xl text-neutral-90 placeholder:text-neutral-60 w-full"
            type="email" placeholder="Email">
            <div class="text-red pl-3" v-if="errors.email">{{errors.email}}</div>
        </div>
        <div class="mb-5">
          <input
            v-model="password"
            v-bind="passwordProps"
            class="focus:outline-none px-4 py-3 bg-neutral-05 rounded-xl text-neutral-90 placeholder:text-neutral-60 w-full"
            type="password" placeholder="Contraseña">
            <div class="text-red pl-3" v-if="errors.password">{{errors.password}}</div>
        </div>
        <div class="mb-5">
          <input
            v-model="repeatPassword"
            v-bind="repeatPasswordProps"
            class="focus:outline-none px-4 py-3 bg-neutral-05 rounded-xl text-neutral-90 placeholder:text-neutral-60 w-full"
            type="password" placeholder="Repetir Contraseña">
            <div class="text-red pl-3" v-if="errors.repeatPassword">{{errors.repeatPassword}}</div>
        </div>
        <Button type="submit" class="btn-primary w-full">Registrarse</Button>
      </form>
    </div>
  </div>
</template>
<script lang="ts" setup>
import Button from '@/components/Button.vue';
import { storeToRefs } from "pinia";
import { useRegisterStore } from "../stores/login";

const store = useRegisterStore();
const {
  name,
  nameProps,
  email,
  emailProps,
  password,
  passwordProps,
  repeatPassword,
  repeatPasswordProps,
  errors,
  disabled,
} = storeToRefs(store);
</script>