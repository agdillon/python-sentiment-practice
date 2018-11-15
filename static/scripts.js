document.addEventListener('DOMContentLoaded', () => {
  let form = document.getElementById('form')
  let searchBlank = document.getElementById('search_term')
  let chartDiv = document.getElementById('chart_div')
  let infoDiv = document.getElementById('info_div')

  function displayChartData(data) {
    console.log(data)
    let { search_term: searchTerm, number_of_tweets: numberOfTweets,
      polarity_list: polarityList, timestamp } = data

    let averagePolarity = polarityList.reduce((accum, el) => accum + el)/polarityList.length

    searchBlank.value = ''
    form.hidden = true

    chartDiv.hidden = false
    infoDiv.hidden = false

    infoDiv.innerHTML = `<ul>
      <li>Average polarity (-1 to 1): ${averagePolarity.toFixed(5)}</li>
      <li>Search term: ${searchTerm}</li>
      <li>Number of tweets: ${numberOfTweets}</li>
      <li>Time of search: ${timestamp}</li>
      </ul>`
  }

  form.addEventListener('submit', (ev) => {
    ev.preventDefault()

    axios.post('/', { search_term: searchBlank.value })
      .then((response) => {
        displayChartData(response.data)
      })
      .catch(err => {
        // add actual error handling
        console.log(err)
      })
  })
})
