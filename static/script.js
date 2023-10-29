const container = document.getElementById('container');
const switchInput = document.getElementById('switch');

switchInput.addEventListener('change', () => {
  if (switchInput.checked) {
    container.classList.add('active');
  } else {
    container.classList.remove('active');
  }
})