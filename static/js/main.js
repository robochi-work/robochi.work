function showModal(id) {
  const m = document.getElementById(id);
  if (!m) return;
  m.setAttribute('aria-hidden', 'false');
}

function hideModal(id) {
  const m = document.getElementById(id);
  if (!m) return;
  m.setAttribute('aria-hidden', 'true');
}

document.addEventListener('DOMContentLoaded', () => {
  console.log("Проверка: ищем элементы...");

  console.log("modalOk:", document.getElementById('modal-ok'));
  console.log("howBtn:", document.getElementById('how-btn'));
  console.log("policyLink:", document.getElementById('policy-link'));

  let pendingBotUrl = null;

  document.querySelectorAll('.big-btn').forEach(btn => {
  if (btn.dataset.bot) {
    btn.addEventListener('click', () => {
      pendingBotUrl = btn.dataset.bot;
      showModal('telegram-modal');
    });
  }
});

  const modalOk = document.getElementById('modal-ok');
  if (modalOk) {
    modalOk.addEventListener('click', () => {
      hideModal('telegram-modal');
      if (pendingBotUrl) {
        window.open(pendingBotUrl, '_blank', 'noopener');
        pendingBotUrl = null;
      }
      window.location.href = '/';
    });
  }

  const howBtn = document.getElementById('how-btn');
if (howBtn) {
  howBtn.addEventListener('click', () => {
    const howModal = document.getElementById('how-modal');
    if (howModal) {
      showModal('how-modal'); 
    }
  });
}

  const policyLink = document.getElementById('policy-link');
if (policyLink) {
  policyLink.addEventListener('click', (e) => {
    const policyModal = document.getElementById('policy-modal');
    if (policyModal) {
      e.preventDefault();
      showModal('policy-modal');
    }
  });
}

  document.querySelectorAll('[data-close]').forEach(b => {
    b.addEventListener('click', () => {
      hideModal(b.getAttribute('data-close'));
    });
  });
});
