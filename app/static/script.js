var rightTable = new Vue
({
  el: '#right-table',
  data: function () {
    return {
      myTable: [{
        id: 1,
        country: 'America',
        new: 30,
        infected: 100000,
      }, {
        id: 3,
        country: 'China',
        new: 10,
        infected: 30,
      }, {
        id: 2,
        country: 'Brazil',
        new: 20,
        infected: 200,
      }]
    }
  },
})
