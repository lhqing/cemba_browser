<template>
  <div>
    <div id="mychart" :style="{width: '400px', height: '400px'}"></div>
    <button @click="addSymbleSize">Increase size</button>
    <button @click="changeTsneScatter">Increase size</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Tsne',
  data () {
    return {
      dataset: [
        ['_id', 'tsne_2_1', 'tsne_2_2'],
        ['3C_0', 0, 0],
        ['3C_1', 0, 0]],
      symble: 5,
      myChart: null
    }
  },
  mounted () {
    this.$nextTick(
      function () {
        this.setTsneScatter()
      }
    )
  },
  watch: {
    dataset: function () {
      this.changeTsneScatter()
    },
    opt: function () {
      this.changeTsneScatter()
    }
  },
  computed: {
    opt () {
      return {
        xAxis: {},
        yAxis: {},
        dataset: {
          source: this.dataset
        },
        series: [{
          symbolSize: this.symble,
          type: 'scatter',
          encode: {
            x: 'tsne_2_1',
            y: 'tsne_2_2'
          }
        }]
      }
    }
  },
  methods: {
    setTsneScatter () {
      let dom = document.getElementById('mychart')
      this.myChart = this.$echarts.init(dom)
      window.addEventListener('resize', this.myChart.resize)
      this.myChart.setOption(this.opt)
    },
    changeTsneScatter () {
      console.log('changetsne')
      this.myChart.setOption(this.opt)
    },
    changeTsneSize () {
      this.myChart.setOption({})
    },
    getTsneFromBackend () {
      const path = 'http://127.0.0.1:5000/api/tsne'
      axios.get(path)
        .then(response => {
          this.dataset = response.data.dataset
        })
        .catch(error => {
          console.log(error)
        })
    },
    addSymbleSize () {
      this.symble = this.symble + 1
      console.log(this.symble)
    }
  },
  created () {
    this.$nextTick(
      function () {
        this.getTsneFromBackend()
      }
    )
  }
}
</script>

<style scoped>

</style>
