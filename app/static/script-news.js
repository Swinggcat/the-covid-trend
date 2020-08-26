// TODO: 
// var myMap = new Vue
// ({
//   el: '#map',
//   data: function () {
//     return {
      
//     }
//   },
// })

// var myTrend = new Vue
// ({
//   el: '#trend',
//   data: function () {
//     return {
      
//     }
//   },
// })

// TODO: Test getData(), then add onload="getData" to #news.

var myNews = new Vue
({
  el: '#news',
  data: function () {
    return {
      retFilt: [{
        date1: '',
        date2: '',
        reg: '',
        key: ''
      }],
      newsData: [{
        id: 1,
        title: 'Title1',
        url: 'index.html'
      }, {
        id: 2,
        title: 'Title2',
        url: 'index.html'
      }, {
        id: 3,
        title: 'Title3',
        url: 'index.html'
      }]
    }
  },
  methods: {
    getData() {
      var request = new XMLHttpRequest();
      request.open('GET', 'our.db.url', true);
      request.send();

      var response = JSON.parse(request.responseText());
      for(it in response)
      {
        newsData.push(it);
      }
    },
    onSubmit() {
      console.log('Yes, you submitted, but nothing will happen');
    }
  }
})


// var myTable = new Vue({
//   data: function () {
//     tableData = [{
//       id: 1,
//       country: 'America',
//       new: 30,
//       infected: 100000,
//     }, {
//       id: 3,
//       country: 'China',
//       new: 10,
//       infected: 30,
//     }, {
//       id: 2,
//       country: 'Brazil',
//       new: 20,
//       infected: 200,
//     }]
//     return {
//       tableData
//     }
//   }
// })