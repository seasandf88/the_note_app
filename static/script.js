const addNoteBtn = document.getElementById("add-note")
const noteDialog = document.getElementById("note-dialog")
const formCancel = document.getElementById("form-cancel")
const deleteButtons = document.querySelectorAll(".delete-button")
const cards = document.querySelectorAll(".card")
const editDialog = document.getElementById

addNoteBtn.addEventListener("click", () => noteDialog.showModal())

formCancel.addEventListener("click", () => noteDialog.close())


deleteButtons.forEach(button => {
  button.addEventListener("click", () => console.log("hello"))
});

cards.forEach(card => {
  card.addEventListener("click", (e) => {

  })
})