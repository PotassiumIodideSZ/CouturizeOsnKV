<template>
  <div class="product-grid-container">
    <h2 v-if="title" class="text-center text-h4 q-mb-xl">
      <span v-if="highlightFirstWord" class="highlight">{{ firstWord }}</span>
      <template v-if="highlightFirstWord"> </template>
      {{ restOfTitle }}
    </h2>
    <div class="product-grid">
      <div v-for="(product, index) in products" :key="index" class="product-card">
        <q-img
          :src="product.image"
          :alt="product.title"
          class="product-image"
          :ratio="4/5"
        />
        <div class="product-price">{{ formatPrice(product.price) }} руб</div>
        <q-btn
          class="product-button full-width"
          color="primary"
          :label="product.buttonText || 'МАГАЗИН'"
          no-caps
          @click="$emit('product-click', product)"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProductGrid',
  props: {
    title: {
      type: String,
      default: ''
    },
    highlightFirstWord: {
      type: Boolean,
      default: true
    },
    products: {
      type: Array,
      required: true,
      validator: (value) => {
        return value.every(product => 
          typeof product === 'object' && 
          'image' in product && 
          'price' in product
        )
      }
    }
  },
  computed: {
    firstWord() {
      return this.title.split(' ')[0]
    },
    restOfTitle() {
      return this.title.split(' ').slice(1).join(' ')
    }
  },
  methods: {
    formatPrice(price) {
      return price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ")
    }
  }
}
</script>

<style lang="scss" scoped>
.product-grid-container {
  width: 100%;
  padding: 40px 20px;
  background: var(--dark-page);

  h2 {
    color: white;
    font-weight: 500;
    margin-bottom: 40px;

    .highlight {
      color: var(--q-primary);
    }
  }
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 30px;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;

  @media (max-width: 1024px) {
    grid-template-columns: repeat(2, 1fr);
    max-width: 800px;
  }

  @media (max-width: 600px) {
    grid-template-columns: 1fr;
    max-width: 400px;
    gap: 20px;
    padding: 0 10px;
  }
}

.product-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: white;
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.3s ease;

  &:hover {
    transform: translateY(-5px);
  }
}

.product-image {
  width: 100%;
  background: white;
}

.product-price {
  font-family: 'Inter';
  color: black;
  font-size: 1.5rem;
  font-weight: 500;
  padding: 15px 0;
}

.product-button {
  border-radius: 0;
  height: 50px;
  font-size: 1.1rem;
  letter-spacing: 1px;
}

@media (max-width: 600px) {
  .product-price {
    font-size: 1.2rem;
    padding: 10px 0;
  }

  .product-button {
    height: 40px;
    font-size: 1rem;
  }
}
</style>
