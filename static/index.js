const frase = document.getElementById("frase")

const getTarefa = () => {
  fetch("/get-tarefa")
  .then(response => response.json())
  .then(data => {
    frase.innerHTML = data.data[0].quote
  })
}
