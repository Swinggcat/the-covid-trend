//国家索引
var country = ['Alabama', 'Alaska', 'American Samoa', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Diamond Princess', 'District of Columbia', 'Florida', 'Georgia', 'Grand Princess', 'Guam', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Northern Mariana Islands', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virgin Islands', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'];

var usaDataBasic = [27312, 695, 0, 40937, 13606, 162798, 29656, 45429, 10444, 49, 9847, 82719, 60030, 103, 188, 744, 3632, 134185, 41013, 24460, 11644, 12995, 48634, 2836, 62969, 106151, 66497, 31296, 20641, 17069, 630, 17231, 11854, 5436, 167703, 10065, 385142, 46934, 3166, 30, 42422, 8904, 6218, 84289, 6003, 16213, 20556, 6050, 32114, 97699, 15344, 1130, 73, 55775, 26784, 2376, 23456, 1114]
var usaData = {
  "code": 200,
  "msg": "success",
  "newslist": []
}

usaDataBasic.forEach(function(item,idx){
  usaData.newslist.push({
    provinceShortName:country[idx],
    confirmedCount:item
  })
})