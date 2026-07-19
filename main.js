// Navbar scroll effect
window.addEventListener('scroll', function () {
  var nav = document.getElementById('navbar');
  if (nav) nav.classList.toggle('scrolled', window.scrollY > 50);

  // Scroll progress bar
  var bar = document.getElementById('scroll-progress');
  if (bar) {
    var scrolled = window.scrollY / (document.body.scrollHeight - window.innerHeight);
    bar.style.transform = 'scaleX(' + Math.min(scrolled, 1) + ')';
  }

  // Back to top
  var btn = document.getElementById('back-top');
  if (btn) btn.classList.toggle('visible', window.scrollY > 400);
});

// Scroll reveal
var revealObs = new IntersectionObserver(function (entries) {
  entries.forEach(function (e) {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      revealObs.unobserve(e.target);
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.reveal, .reveal-left, .reveal-right').forEach(function (el) {
  revealObs.observe(el);
});

// Counter animation
function animateCounters() {
  document.querySelectorAll('[data-count]').forEach(function (el) {
    var target = +el.getAttribute('data-count');
    var current = 0;
    var step = target / 60;
    var timer = setInterval(function () {
      current = Math.min(current + step, target);
      el.textContent = Math.floor(current);
      if (current >= target) clearInterval(timer);
    }, 25);
  });
}
var cntObs = new IntersectionObserver(function (entries) {
  entries.forEach(function (e) {
    if (e.isIntersecting) { animateCounters(); cntObs.disconnect(); }
  });
}, { threshold: 0.3 });
var cntEl = document.querySelector('[data-count]');
if (cntEl) cntObs.observe(cntEl.closest('section') || cntEl);

// Bar chart animation
function animateBars() {
  document.querySelectorAll('.bar-fill[data-width]').forEach(function (el) {
    el.style.width = el.getAttribute('data-width');
  });
}
var barObs = new IntersectionObserver(function (entries) {
  entries.forEach(function (e) {
    if (e.isIntersecting) { animateBars(); barObs.disconnect(); }
  });
}, { threshold: 0.3 });
var barEl = document.querySelector('.bar-fill');
if (barEl) barObs.observe(barEl.closest('section') || barEl);

// Back to top click
document.addEventListener('DOMContentLoaded', function () {
  var btn = document.getElementById('back-top');
  if (btn) btn.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });

  // Active nav link
  var path = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(function (a) {
    var href = a.getAttribute('href');
    if (href === path || (path === '' && href === 'index.html')) a.classList.add('active');
  });
});
