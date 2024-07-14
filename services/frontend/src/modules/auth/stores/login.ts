import { defineStore } from 'pinia'
import { useForm } from 'vee-validate'
import * as Yup from 'yup'
import { ref } from 'vue'
import Request from '@/utils/request'
import { useRouter } from 'vue-router'
import UserSingleton from '@/stores/user';

const request = new Request()

const loginSchema = Yup.object({
  email: Yup.string().email().required(),
  password: Yup.string().min(6).required()
})

const registerSchema = Yup.object({
  name: Yup.string().required(),
  email: Yup.string().email().required(),
  password: Yup.string().min(6).required(),
  repeatPassword: Yup.string()
    .min(6)
    .oneOf([Yup.ref('password')], 'Las contraseñas no coinciden')
    .required()
})

export const useLoginStore = defineStore('login', () => {
  const { errors, defineField, handleSubmit, setErrors } = useForm({
    validationSchema: loginSchema
  })
  const [email, emailProps] = defineField('email')
  const [password, passwordProps] = defineField('password')
  const isLoggedIn = ref<boolean>(false)
  const userId = ref<number>(0)
  const disabled = ref<boolean>(false)
  const router = useRouter()

  const signin = handleSubmit(async (values: any) => {
    disabled.value = true
    const response = await request.post('user/login', values)
    if (!response.success) {
      disabled.value = false
      if (response.data) {
        // Set errors for each field based on response
        if (response.data.email) {
          setErrors({ email: response.message })
        }
        if (response.data.password) {
          setErrors({ password: response.message })
        }
      }
      return false
    }
    isLoggedIn.value = true
    userId.value = response.data
    await getUser()
    await router.push({ name: 'home' })
    disabled.value = false
  })

  const getUser = async () => {
    const response = await request.get(`user/${userId.value}`)
    if (!response.success) return

    const user = UserSingleton.getInstance();
    user.setData(response.data);
  }

  const logout = () => {
    isLoggedIn.value = false
  }

  return {
    errors,
    email,
    emailProps,
    password,
    passwordProps,
    signin,
    logout,
    isLoggedIn,
    userId,
    disabled
  }
})

export const useRegisterStore = defineStore('register', () => {
  const { errors, defineField, handleSubmit, setErrors } = useForm({
    validationSchema: registerSchema
  })
  const [name, nameProps] = defineField('name')
  const [email, emailProps] = defineField('email')
  const [password, passwordProps] = defineField('password')
  const [repeatPassword, repeatPasswordProps] = defineField('repeatPassword')
  const disabled = ref<Boolean>(false)
  const router = useRouter()

  const signup = handleSubmit(async (values: any) => {
    disabled.value = true
    const response = await request.post('user/', values)
    if (!response.success) {
      disabled.value = false
      if (response.data) {
        // Set errors for each field based on response
        if (response.data.email) {
          setErrors({ email: response.message })
        }
        if (response.data.password) {
          setErrors({ password: response.message })
        }
      }
      return false
    }
    await router.push({ name: 'home' })
    disabled.value = false
  })

  return {
    errors,
    name,
    nameProps,
    email,
    emailProps,
    password,
    passwordProps,
    repeatPassword,
    repeatPasswordProps,
    signup,
    disabled
  }
})
