(function () {

    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
           
                e.preventDefault();
                console.log('asdasdasd hola')
            
        });
    });
    
})();


$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
  })