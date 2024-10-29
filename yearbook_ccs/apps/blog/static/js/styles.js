const myModal = document.getElementById('myModal')
const myInput = document.getElementById('myInput')

myModal.addEventListener('shown.bs.modal', () => {
  myInput.focus()
})

const editModal = document.getElementById('editpostModal')
const editInput = document.getElementById('editBtn')

editModal.addEventListener('shown.bs.modal', () => {
  editInput.focus()
})

const filterModal = document.getElementById('myModal')
const filterInput = document.getElementById('myInput')

myModal.addEventListener('shown.bs.modal', () => {
  myInput.focus()
})