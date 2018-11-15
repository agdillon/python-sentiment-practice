document.addEventListener('DOMContentLoaded', () => {
  let form = document.getElementById('form')
  let searchBlank = document.getElementById('search_term')
  let numberBlank = document.getElementById('number_of_tweets')
  let chartDiv = document.getElementById('chart_div')
  let infoDiv = document.getElementById('info_div')
  let backButton = document.getElementById('back')

  function displayChartData(data) {
    console.log(data)
    let { search_term: searchTerm, number_of_tweets: numberOfTweets,
      polarity_list: polarityList, timestamp } = data

    let averagePolarity = polarityList.reduce((accum, el) => accum + el)/polarityList.length

    searchBlank.value = ''
    numberBlank.value = ''
    form.hidden = true

    // items
    let chartData = []
    for (let i = 0; i < polarityList.length; i++) {
      let dataObj = { x: i + 1, y: polarityList[i], group: 0 }
      if (polarityList[i] < 0) {
        dataObj.group = -1
      }
      else if (polarityList[i] > 0) {
        dataObj.group = 1
      }
      chartData.push(dataObj)
    }

    let dataset = new vis.DataSet(chartData)

    // groups
    let groups = new vis.DataSet()
    groups.add({
      id: -1,
      content: 'Negative',
      className: 'negative'
    })
    groups.add({
      id: 0,
      content: 'Neutral',
      className: 'neutral'
    })
    groups.add({
      id: 1,
      content: 'Positive',
      className: 'positive'
    })

    let options = {
      sort: false,
      sampling: false,
      style: 'points',
      showMajorLabels: false,
      showMinorLabels: false,
      drawPoints: {
        size: 4,
        style: 'circle'
      },
      dataAxis: {
        left: {
          title: {
            text: 'Sentiment'
          },
          range: {
            min: -1.25,
            max: 1.25
          }
        }
      }
    }
    let scatterPlot = new vis.Graph2d(chartDiv, dataset, options)

    infoDiv.innerHTML = `<ul>
      <li>Average polarity (-1 to 1): ${averagePolarity.toFixed(5)}</li>
      <li>Search term: ${searchTerm}</li>
      <li>Number of tweets: ${numberOfTweets}</li>
      <li>Time of search: ${timestamp}</li>
      </ul>`

      chartDiv.hidden = false
      infoDiv.hidden = false
      backButton.hidden = false
  }

  form.addEventListener('submit', (ev) => {
    ev.preventDefault()

    axios.post('/', { search_term: searchBlank.value, number_of_tweets: numberBlank.value })
      .then((response) => {
        displayChartData(response.data)
      })
      .catch(err => {
        // add actual error handling
        console.log(err)
      })
  })

  backButton.addEventListener('click', () => {
    chartDiv.innerHTML = ''
    chartDiv.hidden = true
    infoDiv.hidden = true
    backButton.hidden = true
    form.hidden = false
  })
})
