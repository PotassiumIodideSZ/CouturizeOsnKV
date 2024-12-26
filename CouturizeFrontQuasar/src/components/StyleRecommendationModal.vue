<template>
  <q-dialog v-model="isOpen" persistent>
    <q-card class="recommendation-modal">
      <q-card-section class="row items-center q-pb-none">
        <div class="text-h6">Создание новой рекомендации</div>
        <q-space />
        <q-btn icon="close" flat round dense v-close-popup />
      </q-card-section>

      <q-card-section class="q-pt-md">
        <div class="row q-col-gutter-md">
          <!-- Сезон -->
          <div class="col-12">
            <div class="text-h6 q-mb-sm">Выберите сезон:</div>
            <div class="row q-gutter-sm">
              <q-radio v-model="season" val="winter" label="Зима" />
              <q-radio v-model="season" val="spring" label="Весна" />
              <q-radio v-model="season" val="summer" label="Лето" />
              <q-radio v-model="season" val="autumn" label="Осень" />
            </div>
          </div>

          <!-- Стиль -->
          <div class="col-12">
            <div class="text-h6 q-mb-sm">Выберите стиль:</div>
            <div class="row q-gutter-sm">
              <q-radio v-model="selectedStyle" val="business" label="Деловой" />
              <q-radio v-model="selectedStyle" val="sport" label="Спортивный" />
              <q-radio v-model="selectedStyle" val="casual" label="Кэжуал" />
              <q-radio v-model="selectedStyle" val="underwear" label="Бельевой" />
              <q-radio v-model="selectedStyle" val="outerwear" label="Верхняя одежда" />
            </div>
          </div>

          <!-- Стоимость -->
          <div class="col-12">
            <div class="text-h6 q-mb-sm">Стоимость, руб</div>
            <q-slider
              v-model="price"
              :min="0"
              :max="1000000"
              label
              label-always
              :label-value="formatPrice(price)"
              color="primary"
            />
          </div>
        </div>
      </q-card-section>

      <q-card-actions align="center" class="q-pa-md">
        <q-btn
          label="ДАЛЕЕ"
          color="primary"
          class="full-width"
          @click="onSubmit"
          :loading="loading"
        />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script>
import { ref, computed } from 'vue'
import { checkAuthAndRedirect } from '../utils/auth'
import api from '../utils/axios'

export default {
  name: 'StyleRecommendationModal',
  props: {
    modelValue: Boolean,
    imageUrl: String,
    occasion: String,
    style: String,
    budget: String
  },
  emits: ['update:modelValue', 'submit'],
  data() {
    return {
      redirectPath: '/',
      season: null,
      selectedStyle: null,
      price: 0,
      loading: false,
      error: null
    }
  },
  computed: {
    isOpen: {
      get() {
        if (this.modelValue) {
          if (!checkAuthAndRedirect(this.redirectPath)) {
            this.$emit('update:modelValue', false)
            return false
          }
          return true
        }
        return false
      },
      set(value) {
        this.$emit('update:modelValue', value)
      }
    }
  },
  methods: {
    checkAuthAndClose() {
      if (this.modelValue && !checkAuthAndRedirect(this.redirectPath)) {
        this.$emit('update:modelValue', false)
      }
    },
    closeModal() {
      this.$emit('update:modelValue', false)
    },
    resetForm() {
      this.season = null
      this.selectedStyle = null
      this.price = 0
    },
    formatPrice(value) {
      return new Intl.NumberFormat('ru-RU').format(value)
    },
    onSubmit() {
      if (!checkAuthAndRedirect(this.redirectPath)) return
      if (!this.season || !this.selectedStyle) {
        this.$q.notify({
          color: 'negative',
          message: 'Пожалуйста, заполните все обязательные поля',
          position: 'top'
        })
        return
      }

      this.$emit('submit', {
        season: this.season,
        style: this.selectedStyle,
        price: this.price
      })
      this.resetForm()
      this.closeModal()
    }
  },
  beforeMount() {
    if (this.modelValue && !checkAuthAndRedirect(this.redirectPath)) {
      this.$emit('update:modelValue', false)
    }
  }
}
</script>

<style lang="scss" scoped>
.recommendation-modal {
  min-width: 400px;
  padding: 1rem;
  background: #333333;
  color: white;
}

:deep(.q-radio) {
  .q-radio__inner {
    color: white;
  }
  .q-radio__label {
    color: white;
  }
}

:deep(.q-slider) {
  .q-slider__track-container {
    background: rgba(255, 255, 255, 0.3);
  }
  .q-slider__pin-value-marker-text {
    font-size: 12px;
  }
}

.text-h6 {
  color: white;
  font-size: 1.25rem;
  font-weight: 500;
}

.q-btn {
  &.full-width {
    background: #FF5733;
    color: white;
    font-weight: 500;
    border-radius: 8px;
    height: 48px;

    &:hover {
      background: darken(#FF5733, 10%);
    }
  }
}
</style>
