  (function () {
    'use strict';

    // Animación de entrada
    function showEntryAnimation() {
      const overlay = document.createElement('div');
      overlay.style.position = 'fixed';
      overlay.style.inset = '0';
      overlay.style.background = '#0b0b0b';
      overlay.style.display = 'flex';
      overlay.style.alignItems = 'center';
      overlay.style.justifyContent = 'center';
      overlay.style.flexDirection = 'column';
      overlay.style.zIndex = '10000';
      overlay.style.color = '#ff2e8c';
      overlay.innerHTML = `
        <h2>FITNESS GYM</h2>
        <p style="opacity:.7">Cargando...</p>
      `;
      document.body.appendChild(overlay);

      setTimeout(() => {
        overlay.style.transition = 'opacity .8s ease';
        overlay.style.opacity = '0';
        setTimeout(() => overlay.remove(), 900);
      }, 1800);
    }

    // Efecto ripple en botones
    function setupButtonRipples() {
      document.querySelectorAll('.btn, .btn-reserva').forEach(btn => {
        btn.style.position = 'relative';
        btn.style.overflow = 'hidden';

        btn.addEventListener('click', e => {
          const circle = document.createElement('span');
          const rect = btn.getBoundingClientRect();
          const size = Math.max(rect.width, rect.height);

          circle.style.width = circle.style.height = size + 'px';
          circle.style.position = 'absolute';
          circle.style.background = 'rgba(255,255,255,.35)';
          circle.style.borderRadius = '50%';
          circle.style.left = e.clientX - rect.left - size / 2 + 'px';
          circle.style.top = e.clientY - rect.top - size / 2 + 'px';
          circle.style.transform = 'scale(0)';
          circle.style.transition = 'transform .5s, opacity .5s';

          btn.appendChild(circle);

          setTimeout(() => {
            circle.style.transform = 'scale(2)';
            circle.style.opacity = '0';
          }, 10);

          setTimeout(() => circle.remove(), 500);
        });
      });
    }

    // FAQ toggle
    function setupFAQ() {
      document.querySelectorAll('.faq-question').forEach(btn => {
        btn.addEventListener('click', () => {
          btn.parentElement.classList.toggle('open');
        });
      });
    }

    // Menú móvil
    function setupMobileMenu() {
      const nav = document.querySelector('nav');
      const menu = document.querySelector('nav ul.menu');
      if (!nav || !menu) return;

      const btn = document.createElement('button');
      btn.className = 'hamburger-btn';
      btn.innerHTML = '☰';
      btn.style.fontSize = '1.8rem';
      btn.style.background = 'none';
      btn.style.border = 'none';
      btn.style.cursor = 'pointer';
      btn.style.color = '#ff2e8c';

      nav.insertBefore(btn, nav.firstChild);

      btn.addEventListener('click', () => {
        menu.classList.toggle('open-menu');
      });
    }

    // Animación reveal al hacer scroll
    function setupRevealOnScroll() {
      const items = document.querySelectorAll('.reveal');

      function reveal() {
        const trigger = window.innerHeight * 0.85;
        items.forEach(el => {
          if (el.getBoundingClientRect().top < trigger) {
            el.classList.add('visible');
          }
        });
      }

      window.addEventListener('scroll', reveal);
      reveal();
    }

    // Efecto navbar al hacer scroll
    function setupNavbarScrollEffect() {
      const nav = document.querySelector('nav');
      window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
          nav.style.background = 'rgba(0,0,0,0.95)';
          nav.style.boxShadow = '0 2px 10px rgba(0,0,0,0.5)';
        } else {
          nav.style.background = 'rgba(0,0,0,0.8)';
          nav.style.boxShadow = 'none';
        }
      });
    }

    // Validaciones de formularios
    function setupFormValidations() {
      // Reserva
      const reservaForm = document.querySelector(".reserva-form");
      if(reservaForm){
          reservaForm.addEventListener("submit", (e) => {
              const clase = reservaForm.querySelector("select[name='clase']").value;
              if(clase === ""){
                  alert("Por favor selecciona una clase");
                  e.preventDefault();
              }
          });
      }

      // Registro
      const registroForm = document.querySelector(".registro-form");
      if(registroForm){
          registroForm.addEventListener("submit", (e) => {
              const password = registroForm.querySelector("input[name='password']").value;
              const confirmPassword = registroForm.querySelector("input[name='confirm_password']").value;
              if(password !== confirmPassword){
                  alert("Las contraseñas no coinciden");
                  e.preventDefault();
              }
              if(password.length < 6){
                  alert("La contraseña debe tener al menos 6 caracteres");
                  e.preventDefault();
              }
          });
      }

      // Login
      const loginForm = document.querySelector(".login-form");
      if(loginForm){
          loginForm.addEventListener("submit", (e) => {
              const email = loginForm.querySelector("input[name='email']").value.trim();
              const password = loginForm.querySelector("input[name='password']").value.trim();
              if(email === "" || password === ""){
                  alert("Por favor completa todos los campos");
                  e.preventDefault();
              }
          });
      }
  }

  // Mostrar/ocultar contraseña
  function setupShowPassword() {
      document.querySelectorAll(".toggle-password").forEach(toggle => { 
        toggle.addEventListener("click", () => {
        const input = toggle.previousElementSibling;
        if(input.type === "password"){
            input.type = "text";
            toggle.textContent = "Ocultar";
        } else {
            input.type = "password";
            toggle.textContent = "Mostrar";
        }
    });
});

  }

  document.addEventListener('DOMContentLoaded', () => {
    showEntryAnimation();
    setupButtonRipples();
    setupFAQ();
    setupMobileMenu();
    setupRevealOnScroll();
    setupNavbarScrollEffect();
    setupFormValidations();
    setupShowPassword();
  });

})();
