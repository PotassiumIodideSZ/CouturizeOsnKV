<template>
  <footer class="footer-container">
    <div class="footer-content">
      <div class="footer-buttons">
        <q-btn
          flat
          no-caps
          class="footer-btn"
          label="Контакты"
          @click="$router.push('/contacts')"
        />
        <q-btn
          flat
          no-caps
          class="footer-btn"
          label="Помощь"
          @click="$router.push('/help')"
        />
      </div>
      <div class="footer-info">
        <span>2024</span>
        <span>© COUTURIZE</span>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'FooterMain'
}
</script>

<style scoped>
.footer-container {
  width: 100%;
  background: transparent;
  padding: 20px;
}

.footer-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.footer-buttons {
  display: flex;
  gap: 20px;
}

.footer-btn {
  color: #707070;
  font-size: 16px;
  transition: color 0.3s ease;
}

.footer-btn:hover {
  color: var(--q-primary);
}

.footer-info {
  display: flex;
  gap: 10px;
  color: #707070;
  font-size: 14px;
}

@media (max-width: 600px) {
  .footer-content {
    flex-direction: column;
    gap: 20px;
  }
  
  .footer-buttons {
    order: 2;
  }
  
  .footer-info {
    order: 1;
  }
}
</style>
