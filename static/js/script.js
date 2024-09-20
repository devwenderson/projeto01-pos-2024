const hamBurger = document.querySelector(".toggle-btn");

hamBurger.addEventListener("click", function () {
  document.querySelector("#sidebar").classList.toggle("expand");
});


const selectElement = document.getElementById('id_ano_letivo');

selectElement.addEventListener('change', function() {
  const form = document.getElementById('id_boletim_form');
  form.submit();
});


