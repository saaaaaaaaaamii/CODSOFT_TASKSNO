// NovaCloud Landing Page Script - Task 2 (CodSoft Level 1)

document.addEventListener('DOMContentLoaded', () => {
  // 1. MOBILE MENU TOGGLE
  const menuToggle = document.getElementById('menu-toggle');
  const navLinks = document.getElementById('nav-links');
  const navItems = document.querySelectorAll('.nav-item');

  if (menuToggle && navLinks) {
    menuToggle.addEventListener('click', () => {
      navLinks.classList.toggle('open');
      menuToggle.classList.toggle('open');
    });

    navItems.forEach(item => {
      item.addEventListener('click', () => {
        navLinks.classList.remove('open');
        menuToggle.classList.remove('open');
      });
    });
  }

  // 2. PRICING BILLING SWITCH (Monthly / Annual with 20% discount)
  const billingSwitch = document.getElementById('billing-switch');
  const labelMonthly = document.getElementById('label-monthly');
  const labelAnnual = document.getElementById('label-annual');
  const priceValues = document.querySelectorAll('.price-val');
  let isAnnual = false;

  if (billingSwitch) {
    billingSwitch.addEventListener('click', () => {
      isAnnual = !isAnnual;
      billingSwitch.classList.toggle('annual', isAnnual);
      
      if (isAnnual) {
        labelAnnual.classList.add('active');
        labelMonthly.classList.remove('active');
      } else {
        labelMonthly.classList.add('active');
        labelAnnual.classList.remove('active');
      }

      priceValues.forEach(el => {
        const val = isAnnual ? el.getAttribute('data-annual') : el.getAttribute('data-monthly');
        el.style.opacity = '0';
        el.style.transform = 'translateY(-10px)';
        setTimeout(() => {
          el.textContent = val;
          el.style.opacity = '1';
          el.style.transform = 'translateY(0)';
        }, 150);
      });
    });
  }

  // 3. FAQ ACCORDION INTERACTIVITY
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question');
    const answer = item.querySelector('.faq-answer');

    questionBtn.addEventListener('click', () => {
      const isOpen = item.classList.contains('open');

      // Close all other FAQ items for a clean single-open accordion
      faqItems.forEach(otherItem => {
        if (otherItem !== item) {
          otherItem.classList.remove('open');
          const otherAnswer = otherItem.querySelector('.faq-answer');
          if (otherAnswer) otherAnswer.style.maxHeight = null;
        }
      });

      if (isOpen) {
        item.classList.remove('open');
        answer.style.maxHeight = null;
      } else {
        item.classList.add('open');
        answer.style.maxHeight = answer.scrollHeight + 'px';
      }
    });
  });

  // 4. NAVBAR BLUR & SCROLL DETECTOR
  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      navbar.style.borderBottomColor = 'rgba(59, 130, 246, 0.3)';
      navbar.style.boxShadow = '0 10px 25px rgba(0, 0, 0, 0.4)';
    } else {
      navbar.style.borderBottomColor = '';
      navbar.style.boxShadow = '';
    }
  });
});
