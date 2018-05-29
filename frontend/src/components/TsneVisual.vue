<template>
  <el-row>
    <el-col :span="10">
      <div>
        <div id="tsne_chart" :style="{width: '600px', height: '600px'}"></div>
        <el-form label-position="left" label-width="30%" :model="tsneChartControl">
          <el-form-item label="Cluster Selection">
            <el-select v-model="tsneChartControl.cluster" placeholder="Select Cluster Solution">
              <el-option
                v-for="item in tsneChartControl.clusters"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="Symble Size">
            <el-slider
              v-model="tsneChartControl.symble"
              show-input
              :min=2 :max=20
              :debounce="1000"
              input-size="mini">
            </el-slider>
          </el-form-item>
        </el-form>
      </div>
    </el-col>
    <el-col :span="10">
      <div id="tree" :style="{width: '600px', height: '600px'}"></div>
    </el-col>
  </el-row>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'
export default {
  name: 'Tsne',
  data () {
    return {
      dataset: [
        ['3C_1', 6, 6, 6, 6, 6, 6, 'L5a', 37, 11],
        ['3C_10', 37, 0, 0, 0, 0, 0, 'L6', -15, -63],
        ['3C_100', 42, 37, 35, 33, 29, 28, 'Pv', -31, 45]
      ],
      tree: {},
      treeChart: null,
      tsneChart: null,
      tsneChartControl: {
        symble: 4,
        cluster: 7,
        clusters: [
          {value: 1, label: 'Resolution 0.2'},
          {value: 2, label: 'Resolution 0.3'},
          {value: 3, label: 'Resolution 0.5'},
          {value: 4, label: 'Resolution 0.7'},
          {value: 5, label: 'Resolution 0.9'},
          {value: 6, label: 'Resolution 1'},
          {value: 7, label: 'Known Region'}]
      }
    }
  },
  computed: {
    tsneOption () {
      return {
        xAxis: {
          show: false
        },
        yAxis: {
          show: false
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          type: 'scroll',
          orient: 'vertical',
          left: 10,
          top: '20%',
          bottom: '20%'
        },
        grid: {
          left: '20%'
        },
        dataZoom: [
          {
            type: 'slider',
            show: true,
            xAxisIndex: [0],
            throttle: 0
          },
          {
            type: 'slider',
            show: true,
            yAxisIndex: [0],
            throttle: 0
          },
          {
            type: 'inside',
            show: true,
            xAxisIndex: [0],
            throttle: 0
          },
          {
            type: 'inside',
            show: true,
            yAxisIndex: [0],
            throttle: 0
          }
        ],
        series: this.getTsneSeries()
      }
    },
    treeOption () {
      return {}
    }
  },
  watch: {
    dataset: function () {
      this.changeTsneScatter(false)
    },
    tsneOption: function () {
      console.log('symble size')
      console.log(this.cluster)
      this.changeTsneScatter(true)
    }
  },
  methods: {
    setTsneScatter: function () {
      let dom = document.getElementById('tsne_chart')
      this.tsneChart = this.$echarts.init(dom)
      window.addEventListener('resize', this.tsneChart.resize)
      this.tsneChart.setOption(this.tsneOption)
    },
    setTree: function () {
      let dom = document.getElementById('tree')
      this.treeChart = this.$echarts.init(dom)
      window.addEventListener('resize', this.treeChart.resize)
      this.treeChart.setOption(this.treeOption)
    },
    getTsneSeries () {
      let symble = this.tsneChartControl.symble
      let curDataset = this.dataset.slice(1)
      return _.chain(curDataset).groupBy(x => (x[this.tsneChartControl.cluster])).map(function (v, i) {
        return {
          name: i,
          type: 'scatter',
          symbolSize: symble,
          data: v.map(x => x.slice(-2)),
          animation: false,
          large: true,
          largeThreshold: 1
        }
      }).value()
    },
    changeTsneScatter (notMerge) {
      console.log('changetsne')
      this.tsneChart.setOption(this.tsneOption, notMerge)
    },
    getTsneFromBackend () {
      const path = 'http://127.0.0.1:5000/api/cluster'
      axios.get(path)
        .then(response => {
          this.dataset = response.data.dataset
          this.tree = response.data.cluster_tree
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
  mounted () {
    this.$nextTick(
      function () {
        this.setTsneScatter()
      }
    )
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
