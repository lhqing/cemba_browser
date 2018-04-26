# cemba_browser

## Behind browser
[CEMBA data process pipeline](https://github.com/lhqing/cemba_data):
Processing raw sequencing data into canonical analysis results, and save this results in to MongoDB.

## Backend
Using python flask to build a RESTful API, gather datas from MongoDB and transfer them to frontend using Json via AJAX.

## Frontend
Using vue + vuex to build a single page application. Retrieve pre-computed data from backend and display it using certain visualization tools (echarts, plotly etc.).


