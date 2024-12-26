<template>
  <q-page class="flex flex-center">
    <div class="login-container">
      <h2 class="text-h4 text-center q-mb-lg">Вход</h2>
      <q-form @submit="onSubmit" class="q-gutter-md">
        <q-input
          v-model="username"
          label="Имя пользователя"
          :rules="[val => !!val || 'Обязательное поле']"
          :error="!!fieldErrors.username"
          :error-message="fieldErrors.username"
          outlined
        />

        <q-input
          v-model="password"
          label="Пароль"
          type="password"
          :rules="[val => !!val || 'Обязательное поле']"
          :error="!!fieldErrors.password"
          :error-message="fieldErrors.password"
          outlined
        />

        <div class="row justify-between items-center q-mt-md">
          <q-checkbox v-model="rememberMe" label="Запомнить меня" />
          <q-btn flat color="primary" label="Забыли пароль?" to="/reset-password" />
        </div>

        <div class="row justify-center q-mt-lg">
          <q-btn
            type="submit"
            color="primary"
            label="Войти"
            class="full-width"
            :loading="loading"
          />
        </div>

        <SocialAuthButtons
          class="q-mt-md"
          action="войти"
          @google-click="loginWithGoogle"
          @vk-click="loginWithVK"
        />

        <div class="row justify-center q-mt-md">
          <p class="text-grey-7">
            Нет аккаунта?
            <router-link to="/register" class="text-primary">Зарегистрироваться</router-link>
          </p>
        </div>
      </q-form>
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useQuasar } from 'quasar'
import { handleSuccessfulLogin } from '../utils/auth'
import SocialAuthButtons from 'components/SocialAuthButtons.vue'

const $q = useQuasar()
const router = useRouter()

const username = ref('')
const password = ref('')
const rememberMe = ref(false)
const loading = ref(false)
const fieldErrors = ref({})

const loginWithGoogle = () => {
  $q.notify({
    type: 'info',
    message: 'Функция входа через Google будет добавлена позже'
  })
}

const loginWithVK = () => {
  $q.notify({
    type: 'info',
    message: 'Функция входа через VK будет добавлена позже'
  })
}

const onSubmit = async () => {
  try {
    loading.value = true
    fieldErrors.value = {}

    const response = await fetch('http://localhost:8000/api/auth/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: username.value,
        password: password.value,
      }),
    })

    const data = await response.json()

    if (!response.ok) {
      // Handle field-specific errors and non-field errors
      Object.entries(data).forEach(([field, errors]) => {
        if (field === 'detail' || field === 'non_field_errors') {
          fieldErrors.value.password = errors
        } else {
          if (Array.isArray(errors)) {
            fieldErrors.value[field] = errors.join(', ')
          } else {
            fieldErrors.value[field] = errors
          }
        }
      })
      return
    }

    // Store refresh token if remember me is checked
    if (rememberMe.value) {
      localStorage.setItem('refresh_token', data.refresh)
    }

    // Handle successful login and redirect
    handleSuccessfulLogin(data.access)
  } catch (error) {
    fieldErrors.value.password = 'Произошла ошибка при входе'
  } finally {
    loading.value = false
  }
}
</script>

<style lang="scss" scoped>
.login-container {
  width: 100%;
  max-width: 400px;
  padding: 2rem;
}

.q-form {
  width: 100%;
}

a {
  text-decoration: none;
  font-weight: 500;
  
  &:hover {
    text-decoration: underline;
  }
}

.text-negative {
  color: #C10015;
  font-size: 0.875rem;
  line-height: 1.25rem;
}
</style>
