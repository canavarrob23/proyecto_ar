const btnDelete= document.querySelectorAll('.btn-delete');
if(btnDelete) {
  const btnArray = Array.from(btnDelete);
  btnArray.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      if(!confirm('Esta Seguro de Eliminar?')){
        e.preventDefault();
      }
    });
  })
}

function act(){
  var i=document.getElementById("crud").value = "act";
}

function act_reg(){
  var i=document.getElementById("reg").value = "act";
}

function enviarFormu() {
  var formulario = document.getElementById("producto");
  formulario.submit();
}

function enviar() {
  document.getElementById("producto").submit();
}

function cambiarAction(nuevaAccion) {
  const formulario = document.getElementById('producto');
  formulario.action = nuevaAccion;
  // console.log("El action del formulario ahora es:", formulario.action);
}