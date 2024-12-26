<template>
  <div class="text-section-container">
    <h2 v-if="title" class="text-center text-h4 q-mb-xl">{{ title }}</h2>
    <div class="text-content">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TextSection',
  props: {
    title: {
      type: String,
      default: ''
    }
  }
}
</script>

<style lang="scss" scoped>
.text-section-container {
  width: 100%;
  padding: 40px 20px;
  background: var(--dark-page);

  h2 {
    color: var(--q-primary);
    font-weight: 500;
    margin-bottom: 40px;
  }
}

.text-content {
  max-width: 1200px;
  margin: 0 auto;
  color: white;
  font-size: 1.5rem;
  line-height: 1.4;
  text-align: justify;
  letter-spacing: 0.3px;

  p {
    margin-bottom: 1.5rem;

    &:last-child {
      margin-bottom: 0;
    }
  }

  :deep(span.highlight) {
    color: var(--q-primary);
    font-weight: 500;
  }
}

@media (max-width: 600px) {
  .text-content {
    font-size: 1.25rem;
    line-height: 1.2;
    text-align: left;
  }
}
</style>
