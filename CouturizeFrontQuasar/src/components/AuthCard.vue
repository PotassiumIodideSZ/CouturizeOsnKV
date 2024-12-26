<template>
  <q-card class="auth-card">
    <q-card-section class="text-center">
      <div class="text-h5 q-mb-xl">{{ title }}</div>
      <slot></slot>
    </q-card-section>
  </q-card>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    required: true
  }
})
</script>

<style lang="scss" scoped>
.auth-card {
  width: 100%;
  max-width: 400px;
  padding: 20px;
  border: 2px solid rgba(242, 84, 53, 0.2);

  &.q-card--dark {
    border-color: rgba(242, 84, 53, 0.2);
    box-shadow: 0 1px 5px rgba(242, 84, 53, 0.1),
                0 2px 2px rgba(242, 84, 53, 0.08),
                0 3px 1px -2px rgba(242, 84, 53, 0.06);
  }
}
</style>
