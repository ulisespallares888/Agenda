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





function myFunction(id_nota,titulo_nota,contenido_nota,CSRF_TOKEN) {
    
    $('#exampleModalLong').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget) // Button that triggered the modal
        // Extract info from data-* attributes
        // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
        // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
        var modal = $(this)
        //modal.find('.modal-body from').val(recipient)
        modal.find('.modal-body input').val(titulo_nota)
        modal.find('.modal-body textarea').val(contenido_nota)
        modal.find('.modal-body form').val(CSRF_TOKEN)
        console.log(id_nota)

    })
  }







function mostrar() {
    div = document.getElementById('flotante');
    div.style.display = '';
}

function cerrar() {
    div = document.getElementById('flotante');
    div.style.display = 'none';
}
