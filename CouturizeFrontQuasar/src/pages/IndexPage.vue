<template>
  <q-page class="flex flex-center page-main">
    <section class="banner-section section">
      <img src="../assets/HeroBanner.png" alt="Banner" style="width: 100%;" />
    </section>
    <div class="main-page-container">
      <div class="section title-text" id="section1">
        <div class="style-title"><span class="highlight">ВАШ</span> СТИЛЬ</div>
        <div class="history-title">ВАША <span class="highlight">ИСТОРИЯ</span></div>
      </div>

      <div class="image-row section">
        <img class="image-1" src="../assets/image 7.jpg" alt="Image 1" />
        <img class="image-2" src="../assets/image 5.jpg" alt="Image 2" />
        <img class="image-3" src="../assets/image 6.jpg" alt="Image 3" />
      </div>
      <image-carousel-main
        title="КАРУСЕЛЬКА"
        :images="carouselImages"
        :visible-count="3"
        :image-ratio="1.33"
        :base-width="300"
        :center-scale="1.1"
        @slide-change="onSlideChange"
      />
      <div class="text-center q-mt-lg">
        <q-btn
          class="style-btn"
          color="primary"
          size="lg"
          label="ПОДОБРАТЬ СТИЛЬ"
          @click="openStyleModal"
        />
      </div>
      <div class="section">
        <div class="flex-section">
          <p class="flex-section-text"><span class="highlight">ПОДБОР</span> ЦВЕТОВОЙ ПАЛИТРЫ И <span class="highlight">РЕКОМЕНДАЦИИ</span> ПО ФАСОНАМ И СТИЛЯМ ОДЕЖДЫ</p>
          <div class="flex-section-img"><img id="flex-section-img-1" src="../assets/image 9.png" alt="Image 1" /></div>
        </div>
        <div class="flex-section">
          <div class="flex-section-img"><img id="flex-section-img-2" src="../assets/newspaper.png" alt="Image 2" /></div>
          <p class="flex-section-text"><span class="highlight">НОВОСТИ</span> О ТРЕНДАХ И <span class="highlight">СОВЕТЫ</span> ПО СТИЛЮ</p>
        </div>
        <div class="flex-section">
          <p class="flex-section-text"><span class="highlight">СОХРАНЕНИЕ</span> ПОНРАВИВШИХСЯ КОМБИНАЦИЙ</p>
          <div class="flex-section-img"><img id="flex-section-img-3" src="../assets/vector.png" alt="Image 3" /></div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script setup>
import { useQuasar } from 'quasar'
import { onMounted, watch, ref, inject } from 'vue'
import { useRouter } from 'vue-router'

import ImageCarouselMain from 'components/ImageCarouselMain.vue'
defineOptions({
  name: 'IndexPage'
});

const $q = useQuasar()
const router = useRouter()
const openStyleModal = inject('openStyleModal')

const carouselImages = ref([
  { src: new URL('../assets/pngExample1.png', import.meta.url).href, alt: 'Style Example 1' },
  { src: new URL('../assets/pngExample2.png', import.meta.url).href, alt: 'Style Example 2' },
  { src: new URL('../assets/pngExample3.png', import.meta.url).href, alt: 'Style Example 3' },
  { src: new URL('../assets/pngExample4.png', import.meta.url).href, alt: 'Style Example 4' },
  { src: new URL('../assets/pngExample5.png', import.meta.url).href, alt: 'Style Example 5' }
])

const onSlideChange = (index) => {
  console.log('Current slide:', index)
}

// Initialize dark mode based on system preference
onMounted(() => {
  $q.dark.set('auto')
})

// Watch for dark mode changes
watch(() => $q.dark.isActive, val => {
  console.log(val ? 'Dark mode enabled' : 'Light mode enabled')
})
</script>

<style lang="scss" scoped>
@import '../css/pages/index-page.scss';

:deep(.q-page) {
  background: var(--q-primary-bg);
  transition: background-color 0.3s ease;
}

.banner-section{
  margin-top: -81px !important;
}

.style-btn {
  font-family: var(--font-family);
  font-size: 1.2rem;
  padding: 12px 32px;
  background: var(--highlight-color);
  color: var(--text-color);
  border-radius: 8px;
  transition: all 0.3s ease;

  &:hover {
    transform: scale(1.05);
    opacity: 0.9;
  }
}
</style>
