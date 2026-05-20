/* 101% v3 — mobile-first JS */

const TELEGRAM_USERNAME = 'LC101percent';
const PDF_URL = 'assets/lead-magnet.pdf';
const YANDEX_MAP_EMBED =
  'https://yandex.com/map-widget/v1/?ll=69.221%2C41.331&z=16&pt=69.221%2C41.331%2Cpm2rdm&mode=search&oid=21434464753';

const INTEREST_LABELS = {
  math: 'Математика для абитуриентов (8–11 кл)',
  math_5_8: 'Математика 5–8 классы',
  westminster: 'Подготовка к Westminster',
  premium: 'Индивидуально с Нодиром',
};

document.addEventListener('DOMContentLoaded', () => {
  initBurger();
  initForms();
  initPhoneMasks();
  initMapTrigger();
  initStickyCtaToggle();
});

function initBurger() {
  const burger = document.getElementById('navBurger');
  const menu = document.getElementById('mobileMenu');
  if (!burger || !menu) return;

  burger.addEventListener('click', () => {
    const open = burger.getAttribute('aria-expanded') === 'true';
    setMenu(!open);
  });

  menu.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', () => setMenu(false));
  });

  function setMenu(open) {
    burger.setAttribute('aria-expanded', String(open));
    menu.dataset.open = String(open);
    document.body.style.overflow = open ? 'hidden' : '';
  }
}

function initForms() {
  document.querySelectorAll('#heroForm, #leadForm').forEach(f => {
    f.addEventListener('submit', handleSubmit);
  });
}

function handleSubmit(e) {
  e.preventDefault();
  const form = e.currentTarget;
  const fd = new FormData(form);
  const name = (fd.get('name') || '').toString().trim();
  const phone = (fd.get('phone') || '').toString().trim();
  const interest = (fd.get('interest') || 'math').toString();

  if (!name || phone.replace(/\D/g, '').length < 9) {
    flashError(form, 'Заполните имя и телефон.');
    return;
  }

  const lines = [
    'Здравствуйте! Хочу получить «50 формул для нацсертификата» и записаться на 15-мин звонок.',
    '',
    `Имя: ${name}`,
    `Телефон: ${phone}`,
  ];
  if (form.querySelector('[name="interest"]')) {
    lines.push(`Интерес: ${INTEREST_LABELS[interest] || interest}`);
  }
  const message = lines.join('\n');

  triggerDownload(PDF_URL, '101-50-formul.pdf');
  setTimeout(() => {
    const tgUrl = `https://t.me/${TELEGRAM_USERNAME}?text=${encodeURIComponent(message)}`;
    window.open(tgUrl, '_blank', 'noopener');
  }, 400);

  showSuccess(form);
}

function triggerDownload(url, filename) {
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  a.style.display = 'none';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
}

function flashError(form, msg) {
  let err = form.querySelector('.form-error');
  if (!err) {
    err = document.createElement('p');
    err.className = 'form-error';
    err.style.cssText = 'margin-top:10px;color:#E74C3C;font-size:13px;font-weight:600;text-align:center;';
    form.appendChild(err);
  }
  err.textContent = msg;
}

function showSuccess(form) {
  const btn = form.querySelector('button[type="submit"]');
  if (!btn) return;
  const original = btn.textContent;
  btn.disabled = true;
  btn.textContent = '✓ PDF скачивается…';
  btn.style.background = '#27AE60';
  btn.style.color = '#fff';
  setTimeout(() => {
    btn.disabled = false;
    btn.textContent = original;
    btn.style.background = '';
    btn.style.color = '';
  }, 6000);
}

function initPhoneMasks() {
  document.querySelectorAll('input[type="tel"]').forEach(input => {
    input.addEventListener('focus', () => { if (!input.value) input.value = '+998 '; });
    input.addEventListener('input', maskPhone);
  });
}

function maskPhone(e) {
  const input = e.target;
  let digits = input.value.replace(/\D/g, '');
  if (digits.startsWith('998')) digits = digits.slice(3);
  digits = digits.slice(0, 9);
  const parts = ['+998 '];
  if (digits.length > 0) parts.push(digits.slice(0, 2));
  if (digits.length > 2) parts.push(' ' + digits.slice(2, 5));
  if (digits.length > 5) parts.push('-' + digits.slice(5, 7));
  if (digits.length > 7) parts.push('-' + digits.slice(7, 9));
  input.value = parts.join('');
}

function initMapTrigger() {
  const trigger = document.getElementById('mapTrigger');
  if (!trigger) return;
  trigger.addEventListener('click', () => {
    const iframe = document.createElement('iframe');
    iframe.src = YANDEX_MAP_EMBED;
    iframe.title = 'Карта расположения 101%';
    iframe.setAttribute('allowfullscreen', 'true');
    iframe.style.cssText = 'border:0;width:100%;height:100%;display:block;';
    const parent = trigger.parentElement;
    parent.innerHTML = '';
    parent.appendChild(iframe);
  });
}

/* Hide sticky CTA when lead form is visible (avoid CTA collision) */
function initStickyCtaToggle() {
  const sticky = document.getElementById('stickyCta');
  const leadForm = document.querySelector('#lead .lead__form');
  if (!sticky || !leadForm || !('IntersectionObserver' in window)) return;

  const obs = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      sticky.style.transform = entry.isIntersecting ? 'translateY(150%)' : 'translateY(0)';
      sticky.style.opacity = entry.isIntersecting ? '0' : '1';
    });
  }, { threshold: 0.3 });
  obs.observe(leadForm);
  sticky.style.transition = 'transform 0.25s, opacity 0.25s';
}
