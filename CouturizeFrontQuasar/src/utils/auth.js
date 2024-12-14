// For both Options API and Composition API
export function checkAuthAndRedirect(redirectPath = '/profile') {
  const token = localStorage.getItem('access_token')
  if (!token) {
    localStorage.removeItem('access_token')  // Clear any invalid token
    localStorage.setItem('redirectPath', redirectPath)
    window.location.href = '/#/login'
    return false
  }
  return true
}

export function logout() {
  localStorage.removeItem('access_token')
  localStorage.removeItem('redirectPath')
  window.location.href = '/#/login'
}

export function getRedirectPath() {
  const path = localStorage.getItem('redirectPath')
  localStorage.removeItem('redirectPath') // Clear it after getting it
  return path || '/profile' // Default to profile if no redirect path
}

export function handleSuccessfulLogin(token) {
  localStorage.setItem('access_token', token)
  const redirectPath = getRedirectPath()
  window.location.href = '/#' + redirectPath
}
