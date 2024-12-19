<template>
  <q-layout view="hHh lpR fFf" class="main-bg-color">
    <HeaderMain @toggle-right-drawer="toggleRightDrawer" />

    <q-drawer
      v-model="rightDrawerOpen"
      side="right"
      :class="$q.dark.isActive ? 'drawer-dark' : 'drawer-light'"
      bordered
      fixed
      @hide="onDrawerHide"
    >
      <q-list>
        <q-item-label header class="drawer-header">
          Меню
        </q-item-label>

        <EssentialLink
          v-for="link in linksList"
          :key="link.title"
          v-bind="link"
          :active="$route.path === link.link"
          @click="handleLinkClick(link)"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
    <FooterMain />
    <StyleRecommendationModal
      v-model="showStyleModal"
      @submit="handleStyleSubmit"
    />
  </q-layout>
</template>

<script setup>
import { ref, computed, provide } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import EssentialLink from 'components/EssentialLink.vue'
import FooterMain from 'components/FooterMain.vue'
import HeaderMain from 'components/HeaderMain.vue'
import StyleRecommendationModal from 'components/StyleRecommendationModal.vue'

defineOptions({
  name: 'MainLayout',
})

const route = useRoute()
const router = useRouter()

const linksList = [
  {
    title: 'Главная страница',
    caption: '',
    link: '/'
  },
  {
    title: 'Подобрать стиль',
    caption: ''
  },
  {
    title: 'Личный кабинет',
    caption: '',
    link: '/profile'
  },
  {
    title: 'Вход',
    caption: '',
    link: '/login'
  },
  {
    title: 'Регистрация',
    caption: '',
    link: '/register'
  }
]

const rightDrawerOpen = ref(false)
const showStyleModal = ref(false)

function toggleRightDrawer() {
  rightDrawerOpen.value = !rightDrawerOpen.value
}

provide('rightDrawerOpen', rightDrawerOpen)

const openStyleModal = () => {
  showStyleModal.value = true
}

provide('openStyleModal', openStyleModal)

const handleLinkClick = (link) => {
  if (link.title === 'Подобрать стиль') {
    openStyleModal()
    rightDrawerOpen.value = false
  } else {
    router.push(link.link)
    rightDrawerOpen.value = false
  }
}

const handleStyleSubmit = (formData) => {
  showStyleModal.value = false
  router.push('/style')
}

const onDrawerHide = () => {
  rightDrawerOpen.value = false
}
</script>

<style lang="scss">
/* Using global styles to override Quasar's classes */
.q-drawer {
  &.drawer-light, &.drawer-dark {
    background: var(--color-primary-bg) !important;
    color: var(--text-color) !important;
    border-left: 2px solid var(--highlight-color);
  }

  .q-item {
    font-size: 1.5rem !important;
    padding: 1rem !important;
    font-family: var(--font-family) !important;
    color: var(--text-color) !important;
    min-height: unset !important;
    transition: all 0.3s ease !important;

    &:hover {
      background: rgba(var(--highlight-color-rgb), 0.15) !important;
      color: var(--highlight-color) !important;
    }

    &--active {
      background: var(--highlight-color) !important;
      color: white !important;

      &:hover {
        background: rgba(var(--highlight-color-rgb), 0.8) !important;
      }
    }
  }

  .q-item__label--header {
    font-size: 2rem !important;
    padding: 1.5rem 1rem !important;
    color: var(--highlight-color) !important;
    font-family: var(--font-family) !important;
  }
}

.main-bg-color {
  background: var(--bg-color) !important;
  color: var(--text-color) !important;
}
</style>
