(function () {

    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro de eliminar el contacto?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
    
})();


(function () {

    const btnEliminacion = document.querySelectorAll(".btnEliminacion_nota");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro de eliminar la nota?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
    
})();




function mostrar() {
    div = document.getElementById('flotante');
    div.style.display = '';
}

function cerrar() {
    div = document.getElementById('flotante');
    div.style.display = 'none';
}
