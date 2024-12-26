<template>
  <div class="carousel-container" :class="{ 'no-padding': !title }">
    <h2 v-if="title" class="text-center text-h4 q-mb-xl">{{ title }}</h2>
    <div class="carousel-wrapper relative-position">
      <!-- Left Arrow -->
      <q-btn
        v-if="images.length > 1"
        class="carousel-arrow left-arrow"
        flat
        round
        icon="chevron_left"
        color="primary"
        @click="previousSlide"
      />

      <!-- Images -->
      <div class="carousel-content row items-center justify-center">
        <template v-for="(image, index) in visibleImages" :key="index">
          <div
            class="carousel-item"
            :class="{ 
              'center-item': index === Math.floor(visibleCount / 2),
              'side-item': index !== Math.floor(visibleCount / 2)
            }"
            :style="getImageStyle(index)"
          >
            <q-img
              :src="image.src"
              :alt="image.alt"
              :ratio="imageRatio"
            />
          </div>
        </template>
      </div>

      <!-- Right Arrow -->
      <q-btn
        v-if="images.length > 1"
        class="carousel-arrow right-arrow"
        flat
        round
        icon="chevron_right"
        color="primary"
        @click="nextSlide"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'ImageCarouselMain',
  props: {
    // Title is optional
    title: {
      type: String,
      default: ''
    },
    // Images array with src and alt properties
    images: {
      type: Array,
      required: true,
      validator: (value) => {
        return value.every(item => 
          typeof item === 'object' && 
          'src' in item && 
          'alt' in item
        )
      }
    },
    // Number of visible images (must be odd number)
    visibleCount: {
      type: Number,
      default: 3,
      validator: (value) => value % 2 === 1 && value > 0
    },
    // Image dimensions ratio (height/width)
    imageRatio: {
      type: Number,
      default: 1.33 // 4:3 ratio
    },
    // Base image width (center image will be scaled up)
    baseWidth: {
      type: Number,
      default: 300
    },
    // Scale factor for center image
    centerScale: {
      type: Number,
      default: 1.1
    }
  },
  data() {
    return {
      currentIndex: 1
    }
  },
  computed: {
    visibleImages() {
      if (this.images.length === 0) return []
      if (this.images.length === 1) return [this.images[0]]

      const sideCount = Math.floor(this.visibleCount / 2)
      const images = []
      
      for (let i = -sideCount; i <= sideCount; i++) {
        const index = (this.currentIndex + i + this.images.length) % this.images.length
        if (index >= 0 && index < this.images.length) {
          images.push(this.images[index])
        }
      }
      
      return images
    }
  },
  methods: {
    nextSlide() {
      this.currentIndex = (this.currentIndex + 1) % this.images.length
      this.$emit('slide-change', this.currentIndex)
    },
    previousSlide() {
      this.currentIndex = (this.currentIndex - 1 + this.images.length) % this.images.length
      this.$emit('slide-change', this.currentIndex)
    },
    getImageStyle(index) {
      const centerIndex = Math.floor(this.visibleCount / 2)
      const baseHeight = this.baseWidth * 1.5 // 3:2 aspect ratio for taller images
      
      if (index === centerIndex) {
        return {
          transform: `scale(${this.centerScale})`,
          opacity: 1,
          width: `${this.baseWidth}px`,
          height: `${baseHeight}px`
        }
      }
      
      const offset = Math.abs(index - centerIndex)
      const opacity = Math.max(0.4, 1 - (offset * 0.3))
      
      return {
        opacity: opacity,
        width: `${this.baseWidth * 0.85}px`,
        height: `${baseHeight * 0.85}px`
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.carousel-container {
  width: 100%;
  overflow: hidden;
  position: relative;
  padding: 40px 0;
  background: var(--dark-page);

  &.no-padding {
    padding-top: 0;
  }

  h2 {
    color: var(--q-primary);
    font-weight: 500;
    margin-bottom: 60px;
  }
}

.carousel-wrapper {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 40px;
  overflow: visible;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;

  @media (max-width: 1400px) {
    max-width: 1000px;
  }

  @media (max-width: 1200px) {
    max-width: 800px;
  }

  @media (max-width: 900px) {
    max-width: 600px;
    padding: 0 20px;
  }

  @media (max-width: 600px) {
    max-width: 100%;
    padding: 0 10px;
  }
}

.carousel-content {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 30px;
  flex-wrap: nowrap;
  position: relative;
  width: 100%;
  margin: 0 auto;
  min-height: 600px;

  @media (max-width: 900px) {
    gap: 20px;
    min-height: 500px;
  }

  @media (max-width: 600px) {
    gap: 10px;
    min-height: 400px;
  }
}

.carousel-item {
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  transform-origin: center center;
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  justify-content: center;
  max-width: 100%;

  .q-img {
    transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    border-radius: 4px;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  &.center-item {
    z-index: 1;
  }

  &.side-item {
    @media (max-width: 600px) {
      display: none;
    }
  }
}

.carousel-arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 2;

  &.left-arrow {
    left: 0;
  }

  &.right-arrow {
    right: 0;
  }

  @media (max-width: 600px) {
    width: 40px;
    height: 40px;
    
    &.left-arrow {
      left: -10px;
    }

    &.right-arrow {
      right: -10px;
    }
  }
}
</style>
