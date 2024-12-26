<template>
  <q-page class="flex flex-center column">
    <ColorPalettes
      title="ВАШИ ЦВЕТОВЫЕ ГАММЫ"
      :palettes="[
        ['color1', 'color2', 'color3', 'color4'],
        ['color1', 'color2', 'color3', 'color4'],
        ['color1', 'color2', 'color3', 'color4']
      ]"
    />
    
    <TextSection>
      <p><span class="highlight">Вашему</span> типу фигуры подходят как обтягивающие, так и свободные силуэты. Важно выбирать вещи, подчеркивающие ваши достоинства и скрывающие недостатки. У вас песчаные часы, выбирайте платья с акцентом на талии.</p>
      <p>Чтобы подчеркнуть свою фигуру, вам стоит акцентировать внимание на талии. Отличным решением будут пояса или платья с высокой талией, которые помогут выделить эту часть тела. Выбирайте изделия с А-образным силуэтом, так как они красиво обрисовывают ваши изгибы.</p>
      <p>Отдавайте предпочтение топам с V-образными или сердцевидными вырезами, которые привлекут внимание к вашему лицу. Обтягивающие блузы и топы</p>
    </TextSection>

    <image-carousel-main
        title="ПРИМЕРЫ ОБРАЗОВ"
        :images="carouselImages"
        :visible-count="3"
        :image-ratio="1.33"
        :base-width="300"
        :center-scale="1.1"
        @slide-change="onSlideChange"
      />
    
    <ProductGrid
      title="Платья, которые могут Вам подойти"
      :products="dressProducts"
      @product-click="handleProductClick"
    />

    <ProductGrid
      title="Что можно надеть на верх"
      :products="topProducts"
      @product-click="handleProductClick"
    />

    <ProductGrid
      title="Что можно надеть на низ"
      :products="bottomProducts"
      @product-click="handleProductClick"
    />

    <ProductGrid
      title="Головные уборы"
      :products="hatProducts"
      @product-click="handleProductClick"
    />

    <ProductGrid
      title="Аксессуары, которые могут скрасить Ваш образ"
      :products="accessoryProducts"
      @product-click="handleProductClick"
    />
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import ColorPalettes from 'components/ColorPalettes.vue'
import TextSection from 'components/TextSection.vue'
import ProductGrid from 'components/ProductGrid.vue'
import ImageCarouselMain from 'components/ImageCarouselMain.vue'

defineOptions({
  name: 'StylePage'
})

const carouselImages = ref([
  { src: new URL('../assets/pngExample1.png', import.meta.url).href, alt: 'Style Example 1' },
  { src: new URL('../assets/pngExample2.png', import.meta.url).href, alt: 'Style Example 2' },
  { src: new URL('../assets/pngExample3.png', import.meta.url).href, alt: 'Style Example 3' },
  { src: new URL('../assets/pngExample4.png', import.meta.url).href, alt: 'Style Example 4' },
  { src: new URL('../assets/pngExample5.png', import.meta.url).href, alt: 'Style Example 5' }
])

// Helper function to create product arrays
const createProducts = (count, imagePrefix, basePrice) => {
  return Array(count).fill(null).map((_, index) => ({
    image: new URL(`../assets/${imagePrefix}${index + 1}.png`, import.meta.url).href,
    price: basePrice,
    title: 'Товар ' + (index + 1)
  }))
}


const dressProducts = ref(createProducts(4, 'dress', 6000))
const topProducts = ref(createProducts(4, 'top', 3000))
const bottomProducts = ref(createProducts(4, 'bottom', 4000))
const hatProducts = ref(createProducts(4, 'hat', 1500))
const accessoryProducts = ref(createProducts(4, 'accessory', 2000))

const handleProductClick = (product) => {
  console.log('Product clicked:', product)
  // Here you can handle the shop button click
  // For example, open the product in a new tab or navigate to the shop
}
</script>

<style lang="scss" scoped>
.q-page {
  background: var(--dark-page);
  min-height: 100vh;
  width: 100%;
}

// Add spacing between product grids
:deep(.product-grid-container) {
  margin-bottom: 40px;

  &:last-child {
    margin-bottom: 0;
  }
}
</style>
