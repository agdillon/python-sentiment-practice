const axios = require('axios')

document.addEventListener('DOMContentLoaded', () => {
  let form = document.getElementById('form')

  form.addEventListener('submit', (ev) => {
    ev.preventDefault()

    // get data out of form
    let search_term = document.getElementById('search_term').value

    axios.post('/', { search_term })
      .then()
      .catch()
  })
})
