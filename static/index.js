const frase = document.getElementById("frase")
const categoria = document.getElementById("categoria")

const getTarefa = () => {
  fetch("/get-tarefa")
  .then(response => response.json())
  .then(data => {
    frase.innerHTML = data.data[0].quote
    categoria.innerHTML = "Category: " + data.data[0].category
  })
}
