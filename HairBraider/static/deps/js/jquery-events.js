// Когда html документ готов (прорисован)
$(document).ready(function () {
    // Берем из разметки элемент по id - оповещения от django
    var notification = $('#notification');
    // И через 7 сек. убираем
    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');
        }, 3000);
    }

    // // Анимация при скролле
    window.addEventListener('scroll', function() {
        const scrollPosition = window.scrollY;
        const navbar = document.querySelector('.navbar');
    
        if (scrollPosition > 100) {
            navbar.classList.add('shadow-sm');
            navbar.classList.add('bg-white');
        } else {
            navbar.classList.remove('shadow-sm');
            navbar.classList.remove('bg-white');
        }
    });

    // Плавная прокрутка для якорных ссылок
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });


    if (typeof ProductGallery !== 'undefined' && document.getElementById('mainImage')) {
        const galleryContainer = document.getElementById('gallery-container');
        const images = [
            galleryContainer.dataset.main,
            ...JSON.parse(galleryContainer.dataset.additional)
        ];
        new ProductGallery(images);
    }

});