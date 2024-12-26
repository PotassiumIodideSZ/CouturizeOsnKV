<template>
  <div class="color-palettes-container">
    <h2 v-if="title" class="text-center text-h4 q-mb-xl">{{ title }}</h2>
    <div class="palettes-grid">
      <div v-for="(palette, index) in palettes" :key="index" class="palette-row">
        <div v-for="(color, colorIndex) in palette" :key="colorIndex" class="color-block">
          colors
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ColorPalettes',
  props: {
    title: {
      type: String,
      default: ''
    },
    palettes: {
      type: Array,
      required: true,
      default: () => [
        ['color1', 'color2', 'color3', 'color4'],
        ['color1', 'color2', 'color3', 'color4'],
        ['color1', 'color2', 'color3', 'color4']
      ]
    }
  }
}
</script>

<style lang="scss" scoped>
.color-palettes-container {
  width: 100%;
  padding: 40px 20px;
  background: var(--dark-page);

  h2 {
    color: var(--q-primary);
    font-weight: 500;
    margin-bottom: 40px;
  }
}

.palettes-grid {
  display: flex;
  flex-direction: column;
  gap: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.palette-row {
  display: flex;
  gap: 4px;
  justify-content: center;
}

.color-block {
  width: 80px;
  height: 80px;
  border: 2px dashed rgba(255, 255, 255, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(255, 255, 255, 0.7);
  font-size: 12px;
}

@media (max-width: 600px) {
  .color-block {
    width: 60px;
    height: 60px;
    font-size: 10px;
  }
}
</style>
