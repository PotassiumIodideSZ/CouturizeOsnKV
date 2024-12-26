<template>
  <q-page class="flex flex-center">
    <div class="profile-container q-pa-md">
      <h2 class="text-h4 text-center q-mb-lg">Профиль пользователя</h2>

      <!-- Информация о пользователе -->
      <div class="user-info q-mb-xl">
        <q-list bordered class="rounded-borders">
          <q-item>
            <q-item-section>
              <q-item-label caption>Имя пользователя</q-item-label>
              <q-item-label>{{ userInfo.username }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label caption>Email</q-item-label>
              <q-item-label>{{ userInfo.email }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label caption>Имя</q-item-label>
              <q-item-label>{{ userInfo.first_name || 'Не указано' }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label caption>Фамилия</q-item-label>
              <q-item-label>{{ userInfo.last_name || 'Не указано' }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>

        <div class="q-mt-md text-center">
          <q-btn
            color="negative"
            label="Выйти"
            icon="logout"
            @click="handleLogout"
            :loading="loading"
          />
        </div>
      </div>

      <!-- Форма смены пароля -->
      <div class="password-change-form">
        <h3 class="text-h5 q-mb-md">Сменить пароль</h3>
        <q-form @submit="onChangePassword" class="q-gutter-md">
          <q-input
            v-model="passwordForm.old_password"
            label="Текущий пароль"
            type="password"
            :error="!!passwordErrors.old_password"
            :error-message="passwordErrors.old_password"
            outlined
            class="q-mb-md"
          />
          <q-input
            v-model="passwordForm.new_password"
            label="Новый пароль"
            type="password"
            :error="!!passwordErrors.new_password"
            :error-message="passwordErrors.new_password"
            outlined
            class="q-mb-md"
          />
          <q-input
            v-model="passwordForm.new_password2"
            label="Подтвердите новый пароль"
            type="password"
            :error="!!passwordErrors.new_password2"
            :error-message="passwordErrors.new_password2"
            outlined
            class="q-mb-md"
          />
          <div class="row justify-center q-mt-md">
            <q-btn
              type="submit"
              color="primary"
              label="Сменить пароль"
              :loading="loading"
            />
          </div>
        </q-form>
      </div>
    </div>
  </q-page>
</template>

<script setup>
import { ref, onMounted, onBeforeMount } from 'vue'
import { useQuasar } from 'quasar'
import axios from 'axios'
import { checkAuthAndRedirect, logout } from '../utils/auth'
import api from '../utils/axios'

const $q = useQuasar()
const redirectPath = ref('/profile')

// Check authentication before component mounts
onBeforeMount(() => {
  checkAuthAndRedirect(redirectPath.value)
})

const userInfo = ref({})
const loading = ref(false)
const passwordForm = ref({
  old_password: '',
  new_password: '',
  new_password2: ''
})
const passwordErrors = ref({})

const fetchUserInfo = async () => {
  if (!checkAuthAndRedirect(redirectPath.value)) return

  try {
    const response = await api.get('/auth/user/')
    userInfo.value = response.data
  } catch (error) {
    if (error.response?.status !== 401) {  // Don't show error for auth failures
      console.error('Error fetching user info:', error)
      $q.notify({
        color: 'negative',
        message: 'Ошибка при загрузке данных пользователя',
        position: 'top'
      })
    }
  }
}

const onChangePassword = async () => {
  if (!checkAuthAndRedirect(redirectPath.value)) return
  if (loading.value) return

  loading.value = true
  passwordErrors.value = {}

  try {
    if (passwordForm.value.new_password !== passwordForm.value.new_password2) {
      passwordErrors.value.new_password2 = 'Пароли не совпадают'
      loading.value = false
      return
    }

    await api.post('/auth/password/change/', {
      old_password: passwordForm.value.old_password,
      new_password: passwordForm.value.new_password
    })

    $q.notify({
      color: 'positive',
      message: 'Пароль успешно изменен',
      position: 'top'
    })

    // Очистка формы
    passwordForm.value = {
      old_password: '',
      new_password: '',
      new_password2: ''
    }
  } catch (error) {
    if (error.response?.status !== 401) {  // Don't show error for auth failures
      const errors = error.response?.data || {}
      passwordErrors.value = errors
      $q.notify({
        color: 'negative',
        message: 'Ошибка при смене пароля',
        position: 'top'
      })
    }
  } finally {
    loading.value = false
  }
}

const handleLogout = () => {
  loading.value = true
  try {
    logout()
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchUserInfo()
})
</script>

<style scoped>
.profile-container {
  width: 100%;
  max-width: 600px;
  padding: 2rem;
}

.password-change-form {
  margin-top: 2rem;
}
</style>
