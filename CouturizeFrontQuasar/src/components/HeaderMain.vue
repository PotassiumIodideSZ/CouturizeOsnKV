<template>
  <q-header reveal class="header">
    <q-toolbar>
      <q-toolbar-title class="styled-title">
        <router-link to="/" class="header-link">
          COUTURIZE
        </router-link>
      </q-toolbar-title>

      <q-btn
        flat
        dense
        round
        icon="person"
        class=""
      />

      <q-btn
        flat
        dense
        round
        :icon="$q.dark.isActive ? 'light_mode' : 'dark_mode'"
        @click="toggleDarkMode"
        class="q-mr-sm theme-toggle"
      />

      <q-btn
        flat
        dense
        round
        aria-label="Menu"
        @click="toggleMenu"
        class="menu-btn"
        :class="{ 'is-open': rightDrawerOpen }"
      >
        <div class="hamburger-icon">
          <span class="line line-1"></span>
          <span class="line line-2"></span>
          <span class="line line-3"></span>
        </div>
      </q-btn>
    </q-toolbar>
  </q-header>
</template>

<script setup>
import { ref, computed, inject } from 'vue'
import { useQuasar } from 'quasar'

defineOptions({
  name: 'HeaderMain'
})

const $q = useQuasar()
const rightDrawerOpen = inject('rightDrawerOpen')

const toggleDarkMode = () => {
  $q.dark.toggle()
}

const emit = defineEmits(['toggle-right-drawer'])

const toggleMenu = () => {
  emit('toggle-right-drawer')
}
</script>

<style lang="scss" scoped>
.header {
  background: transparent !important;

  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.2);
    z-index: -1;
  }
}

.styled-title {
  color: var(--text-color);

  .header-link {
    color: var(--text-color);
    text-decoration: none;
    transition: color var(--transition-normal);
    text-transform: uppercase;
    font-size: 46px;
    font-family: 'Builder Extended' !important;
    font-weight: 600 !important;
    letter-spacing: 2px;

    &:hover {
      color: var(--highlight-color);
    }
  }

  &::first-letter {
    color: var(--highlight-color);
  }
}

.theme-toggle,
.menu-btn {
  color: var(--text-color);
}

.menu-btn {
  padding: 8px;

  .hamburger-icon {
    width: 24px;
    height: 18px;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .line {
    display: block;
    width: 100%;
    height: 2px;
    background-color: var(--text-color);
    transition: all 0.3s ease;
    transform-origin: center;
    position: absolute;

    &.line-1 {
      background-color: var(--highlight-color);
      top: 0;
    }

    &.line-2 {
      top: 50%;
      transform: translateY(-50%);
    }

    &.line-3 {
      bottom: 0;
    }
  }

  &.is-open {
    .line-1 {
      transform: translateY(8px) rotate(45deg);
    }

    .line-2 {
      opacity: 0;
    }

    .line-3 {
      transform: translateY(-8px) rotate(-45deg);
    }
  }

  &:hover {
    .line {
      background-color: var(--highlight-color);
    }
  }
}

@media (max-width: 750px) {
  .styled-title {
    font-size: 44px;
  }
}

@media (max-width: 400px) {
  .styled-title {
    font-size: 36px;
  }
}
</style>
