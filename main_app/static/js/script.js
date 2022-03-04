console.log(M);

// time picker animation
const dateEl = document.getElementById("id_time");

M.Datepicker.init(dateEl, {
  format: "yyyy-mm-dd",
  defaultDate: new Date(),
  setDefaultDate: true,
  autoClose: true,
});
