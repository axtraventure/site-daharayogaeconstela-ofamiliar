// Dahara Yoga e Constelação Familiar - Interactive Script

document.addEventListener('DOMContentLoaded', () => {
    // 1. Hero Background Slideshow Transition
    const slides = document.querySelectorAll('.hero-slide');
    let currentSlide = 0;
    
    if (slides.length > 1) {
        setInterval(() => {
            slides[currentSlide].classList.remove('opacity-100');
            slides[currentSlide].classList.add('opacity-0');
            
            currentSlide = (currentSlide + 1) % slides.length;
            
            slides[currentSlide].classList.remove('opacity-0');
            slides[currentSlide].classList.add('opacity-100');
        }, 5000); // Transitions background slide every 5 seconds
    }

    // 2. Active Anchor Navigation on Scroll
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    
    window.addEventListener('scroll', () => {
        let currentActiveSectionId = '';
        const scrollPosition = window.scrollY + 120; // offset

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            
            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                currentActiveSectionId = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('text-primary', 'font-semibold');
            link.classList.add('text-titleMain');
            
            if (link.getAttribute('href') === `#${currentActiveSectionId}`) {
                link.classList.remove('text-titleMain');
                link.classList.add('text-primary', 'font-semibold');
            }
        });
    });
});
