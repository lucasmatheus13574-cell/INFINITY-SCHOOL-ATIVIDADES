const form = document.querySelector('#contactForm');
const alertBox = document.querySelector('#formAlert');
const themeToggle = document.querySelector('#toggleTheme');
const themeLabel = document.querySelector('#themeLabel');

const setTheme = (theme) => {
  document.body.classList.toggle('dark', theme === 'dark');
  localStorage.setItem('preferredTheme', theme);
  themeLabel.textContent = theme === 'dark' ? 'Claro' : 'Escuro';
};

const initTheme = () => {
  const stored = localStorage.getItem('preferredTheme');
  if (stored === 'dark' || stored === 'light') {
    setTheme(stored);
    return;
  }

  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  setTheme(prefersDark ? 'dark' : 'light');
};

const toggleTheme = () => {
  const current = document.body.classList.contains('dark') ? 'dark' : 'light';
  setTheme(current === 'dark' ? 'light' : 'dark');
};

const showAlert = (message, success = true) => {
  alertBox.textContent = message;
  alertBox.classList.add('show');
  alertBox.style.borderColor = success ? 'rgba(45, 116, 255, 0.3)' : 'rgba(255, 100, 100, 0.4)';
  alertBox.style.background = success ? 'rgba(45, 116, 255, 0.13)' : 'rgba(255, 100, 100, 0.12)';
  alertBox.style.color = success ? 'var(--color-primary-variant)' : '#b33';

  setTimeout(() => {
    alertBox.classList.remove('show');
  }, 4200);
};

const validateForm = () => {
  if (!form.checkValidity()) {
    showAlert('Por favor, preencha todos os campos corretamente.', false);
    return false;
  }

  const message = form.message.value.trim();
  if (message.length < 10) {
    showAlert('A mensagem deve ter pelo menos 10 caracteres.', false);
    return false;
  }

  return true;
};

form.addEventListener('submit', (event) => {
  event.preventDefault();

  if (!validateForm()) {
    return;
  }

  showAlert('Obrigado! Sua mensagem foi enviada (simulada).', true);
  form.reset();
});

themeToggle.addEventListener('click', toggleTheme);

initTheme();
