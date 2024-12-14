<template>
  <div class="text-center q-pa-md">или {{ action }} через</div>
  <div class="row q-gutter-md justify-center">
    <q-btn
      flat
      color="red-6"
      icon="img:https://www.google.com/favicon.ico"
      label="Google"
      @click="$emit('google-click')"
      class="social-btn"
    />
    <q-btn
      flat
      color="blue-6"
      icon="img:https://vk.com/favicon.ico"
      label="VKontakte"
      @click="$emit('vk-click')"
      class="social-btn"
    />
  </div>
</template>

<script setup>
defineProps({
  action: {
    type: String,
    required: true
  }
})

defineEmits(['google-click', 'vk-click'])
</script>

<style lang="scss" scoped>
.social-btn {
  width: 140px;
  opacity: 0.9;
  transition: opacity 0.3s;

  &:hover {
    opacity: 1;
  }
}
</style>
