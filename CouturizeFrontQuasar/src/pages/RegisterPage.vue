<template>
  <q-page class="flex flex-center">
    <div class="register-container">
      <h2 class="text-h4 text-center q-mb-lg">Регистрация</h2>
      <q-form @submit="onSubmit" class="q-gutter-md">
        <q-input
          v-model="username"
          label="Имя пользователя"
          :rules="[val => !!val || 'Обязательное поле']"
          :error="!!fieldErrors.username"
          :error-message="fieldErrors.username"
          outlined
          class="q-mb-md"
        />

        <q-input
          v-model="email"
          label="Email"
          type="email"
          :rules="[
            val => !!val || 'Email обязателен',
            val => /.+@.+\..+/.test(val) || 'Введите корректный email'
          ]"
          :error="!!fieldErrors.email"
          :error-message="fieldErrors.email"
          outlined
          class="q-mb-md"
        />

        <q-input
          v-model="firstName"
          label="Имя"
          :error="!!fieldErrors.first_name"
          :error-message="fieldErrors.first_name"
          outlined
          class="q-mb-md"
        />

        <q-input
          v-model="lastName"
          label="Фамилия"
          :error="!!fieldErrors.last_name"
          :error-message="fieldErrors.last_name"
          outlined
          class="q-mb-md"
        />

        <q-input
          v-model="password"
          label="Пароль"
          type="password"
          :rules="[
            val => !!val || 'Пароль обязателен',
          ]"
          :error="!!fieldErrors.password"
          :error-message="fieldErrors.password"
          outlined
          class="q-mb-md"
        />

        <q-input
          v-model="password2"
          label="Подтвердите пароль"
          type="password"
          :rules="[
            val => !!val || 'Подтверждение пароля обязательно',
            val => val === password || 'Пароли не совпадают'
          ]"
          :error="!!fieldErrors.password2"
          :error-message="fieldErrors.password2"
          outlined
          class="q-mb-md"
        />

        <div class="row justify-center q-mt-lg">
          <q-btn
            type="submit"
            color="primary"
            label="Зарегистрироваться"
            class="full-width"
            :loading="loading"
          />
        </div>

        <SocialAuthButtons
          class="q-mt-md"
          action="зарегистрироваться"
          @google-click="registerWithGoogle"
          @vk-click="registerWithVK"
        />

        <div class="row justify-center q-mt-md">
          <p class="text-grey-7">
            Уже есть аккаунт?
            <router-link to="/login" class="text-primary">Войти</router-link>
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
import SocialAuthButtons from 'components/SocialAuthButtons.vue'

const $q = useQuasar()
const router = useRouter()

const username = ref('')
const email = ref('')
const firstName = ref('')
const lastName = ref('')
const password = ref('')
const password2 = ref('')
const loading = ref(false)
const fieldErrors = ref({})

const registerWithGoogle = () => {
  $q.notify({
    type: 'info',
    message: 'Функция регистрации через Google будет добавлена позже'
  })
}

const registerWithVK = () => {
  $q.notify({
    type: 'info',
    message: 'Функция регистрации через VK будет добавлена позже'
  })
}

const clearErrors = () => {
  fieldErrors.value = {}
}

const validateForm = () => {
  clearErrors()
  const errors = {}

  // Username validation
  if (!username.value) {
    errors.username = 'Имя пользователя обязательно'
  } else if (username.value.length < 3) {
    errors.username = 'Имя пользователя должно содержать минимум 3 символа'
  } else if (!/^[a-zA-Z0-9_]+$/.test(username.value)) {
    errors.username = 'Имя пользователя может содержать только буквы, цифры и знак подчеркивания'
  }

  // Email validation
  if (!email.value) {
    errors.email = 'Email обязателен'
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
    errors.email = 'Введите корректный email адрес'
  }

  // Password validation
  const passwordErrors = []
  if (!password.value) {
    passwordErrors.push('Пароль обязателен')
  } else {
    if (password.value.length < 8) {
      passwordErrors.push('Пароль должен содержать минимум 8 символов')
    }
    if (!/[A-z]/.test(password.value)) {
      passwordErrors.push('Пароль должен содержать хотя бы одну букву')
    }

    if (['123456', 'password', '12345678', 'qwerty', 'admin123'].includes(password.value.toLowerCase())) {
      passwordErrors.push('Этот пароль слишком простой')
    }
    if (password.value.toLowerCase().includes(username.value.toLowerCase())) {
      passwordErrors.push('Пароль не должен содержать имя пользователя')
    }
  }

  if (passwordErrors.length > 0) {
    errors.password = passwordErrors.join(', ')
  }

  // Password confirmation validation
  if (!password2.value) {
    errors.password2 = 'Подтверждение пароля обязательно'
  } else if (password.value !== password2.value) {
    errors.password2 = 'Пароли не совпадают'
  }

  return errors
}

const onSubmit = async () => {
  try {
    const errors = validateForm()
    if (Object.keys(errors).length > 0) {
      fieldErrors.value = errors
      return
    }

    loading.value = true
    fieldErrors.value = {}

    const response = await fetch('http://localhost:8000/api/auth/register/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: username.value,
        email: email.value,
        first_name: firstName.value,
        last_name: lastName.value,
        password: password.value,
        password2: password2.value,
      }),
    })

    const data = await response.json()

    if (!response.ok) {
      // Handle field-specific errors
      Object.entries(data).forEach(([field, errors]) => {
        if (Array.isArray(errors)) {
          fieldErrors.value[field] = errors.join(' ')
        } else if (typeof errors === 'string') {
          fieldErrors.value[field] = errors
        } else {
          fieldErrors.value[field] = 'Ошибка валидации'
        }
      })
      return
    }

    // Automatic login after registration
    const loginResponse = await fetch('http://localhost:8000/api/auth/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: username.value,
        password: password.value,
      }),
    })

    const loginData = await loginResponse.json()

    if (!loginResponse.ok) {
      throw new Error(loginData.detail || 'Ошибка автоматического входа')
    }

    // Store tokens
    localStorage.setItem('access_token', loginData.access)
    localStorage.setItem('refresh_token', loginData.refresh)

    // Redirect to profile page
    router.push('/profile')
  } catch (error) {
    fieldErrors.value.non_field_errors = error.message
  } finally {
    loading.value = false
  }
}
</script>

<style lang="scss" scoped>
.register-container {
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
</style>
