console.log(M);
const dateEl = document.getElementById("id_time");
const selectEl = document.getElementById("id_play");

// time picker animation
M.Datepicker.init(dateEl, {
  format: "yyyy-mm-dd",
  defaultDate: new Date(),
  setDefaultDate: true,
  autoClose: true,
});

// widget animation
M.FormSelect.init(selectEl);
