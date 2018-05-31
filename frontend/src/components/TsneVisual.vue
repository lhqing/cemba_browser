<template>
  <div>
  <el-row>
    <el-col :span="12">
      <div>
        <div id="tsne_chart" :style="{width: '100%', height: '800px'}"></div>
        <el-form label-position="left" label-width="30%" :model="tsneChartControl">
          <el-form-item label="Cluster Selection">
            <el-select
              v-model="tsneChartControl.cluster"
              placeholder="Select Cluster Solution"
              value="tsneChartControl.cluster">
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
    <el-col :span="12">
      <div id="tree" :style="{width: '100%', height: '800px'}"></div>
    </el-col>
  </el-row>
  <el-row>
    <el-col :span="12">
      <div id="gene_chart" :style="{width: '100%', height: '800px'}"></div>
      <el-form :inline="false" :model="geneChartControlForm">
        <el-form-item label="Gene">
          <el-input v-model="geneChartControlForm.gene" placeholder="Input Gene Name"></el-input>
        </el-form-item>
        <el-form-item label="mC type">
          <el-select v-model="geneChartControlForm.mc_type" placeholder="Methylation Type">
            <el-option label="mCH" value="ch"></el-option>
            <el-option label="mCG" value="cg"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="Normalize by overall methylation">
          <el-switch
            v-model="geneChartControlForm.norm"
            active-color="#13ce66"
            inactive-color="#ff4949">
          </el-switch>
        </el-form-item>
        <el-form-item label="Gene Base Call Cutoff">
          <el-input-number v-model="geneChartControlForm.covCutoff" :min="5" :max="200"></el-input-number>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="updateGeneControl">Update</el-button>
        </el-form-item>
      </el-form>
    </el-col>
    <el-col>
      <div id="gene_sunburst" :style="{width: '600px', height: '600px'}"></div>
    </el-col>
  </el-row>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'
import darkTheme from '../assets/dark.json'
export default {
  name: 'Tsne',
  data () {
    return {
      dataset: [
        ['3C_1', 6, 6, 6, 6, 6, 6, 'L5a', 37, 11],
        ['3C_10', 37, 0, 0, 0, 0, 0, 'L6', -15, -63],
        ['3C_100', 42, 37, 35, 33, 29, 28, 'Pv', -31, 45]
      ],
      tree: {
        'name': 'data',
        'children': [
          {
            'name': 'converters',
            'children': [
              {'name': 'Converters', 'value': 721},
              {'name': 'DelimitedTextConverter', 'value': 4294}]},
          {'name': 'DataUtil', 'value': 3322}]},
      treeChart: null,
      treeChartControl: {},
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
          {value: 7, label: 'Known Region'}]},
      geneChart: null,
      geneDataset: [['_id', 'tsne_2_1', 'tsne_2_2', 'cov', 'mc%', 'pass'],
        ['3C_0', -22, 6, 1905, 1.2, true],
        ['3C_1', 37, 11, 1136, 0.1, true]],
      geneInfo: {},
      geneChartControl: {
        gene: 'Rorb',
        gene_id: '',
        mc_type: 'ch',
        norm: true,
        symble: 4,
        normRange: [2, 98],
        covCutoff: 10},
      geneChartControlForm: {
        gene: 'Rorb',
        gene_id: '',
        mc_type: 'ch',
        norm: true,
        symble: 4,
        normRange: [2, 98],
        covCutoff: 10
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
          bottom: '10%'
        },
        grid: {
          left: '20%'
        },
        dataZoom: [
          {
            type: 'slider',
            show: true,
            xAxisIndex: [0],
            throttle: 0,
            realtime: false
          },
          {
            type: 'slider',
            show: true,
            yAxisIndex: [0],
            throttle: 0,
            realtime: false
          },
          {
            type: 'inside',
            show: true,
            xAxisIndex: [0],
            throttle: 0,
            realtime: false
          },
          {
            type: 'inside',
            show: true,
            yAxisIndex: [0],
            throttle: 0,
            realtime: false
          }
        ],
        series: this.getTsneSeries()
      }
    },
    treeOption () {
      return {
        tooltip: {
          trigger: 'item',
          triggerOn: 'mousemove'
        },
        series: [{
          type: 'sunburst',
          data: [this.tree],
          top: '0%',
          bottom: '20%',
          left: '40%',
          right: '0%',
          highlightPolicy: 'ancestor',
          levels: [{},
            {itemStyle: {color: '#076572'}},
            {itemStyle: {color: '#008496'}},
            {itemStyle: {color: '#09AA91'}},
            {itemStyle: {color: '#44C876'}},
            {itemStyle: {color: '#CCE754'}}]
        }],
        emphasis: {
          itemStyle: {
            color: '#FFD000'
          }
        },
        highlight: {
          itemStyle: {
            color: '#076572'
          }
        }
      }
    },
    geneOption () {
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
        visualMap: [{
          type: 'continuous',
          min: quantile(this.geneDataset.slice(1).map(x => x[4]), this.geneChartControl.normRange[0]),
          max: quantile(this.geneDataset.slice(1).map(x => x[4]), this.geneChartControl.normRange[1]),
          calculable: true,
          precision: 1,
          dimension: 4,
          top: '10%',
          outOfRange: {
            color: ['rgb(200,200,200)'],
            colorAlpha: [0]
          },
          hoverLink: false,
          realtime: false
        }, {
          type: 'piecewise',
          calculable: false,
          pieces: [
            {min: this.geneChartControl.covCutoff}, // 不指定 max，表示 max 为无限大（Infinity）。
            {max: this.geneChartControl.covCutoff} // 不指定 min，表示 min 为无限大（-Infinity）。
          ],
          dimension: 3,
          bottom: '10%',
          inRange: {
            colorAlpha: [0.3, 1]
          },
          outOfRange: {
            color: ['rgba(255,255,255,.0)']
          },
          hoverLink: false
        }],
        dataset: {
          source: this.geneDataset
        },
        series: [{
          name: 'gene',
          type: 'scatter',
          symbolSize: this.geneChartControl.symble,
          encode: {
            x: 'tsne_2_1',
            y: 'tsne_2_2'
          },
          animation: false,
          progressive: 100,
          progressiveThreshold: 3000
        }]
      }
    }
  },
  watch: {
    dataset: function () {
      this.changeTsneScatter(false)
    },
    tsneOption: function () {
      this.changeTsneScatter(true)
    },
    treeOption: function () {
      this.changeTree(true)
    },
    geneOption: function () {
      console.log('change gene')
      setTimeout(
        this.changeGeneScatter(true), 3000
      )
    }
  },
  methods: {
    setTsneScatter: function () {
      let dom = document.getElementById('tsne_chart')
      this.tsneChart = this.$echarts.init(dom, 'dark')
      window.addEventListener('resize', this.tsneChart.resize)
      this.tsneChart.setOption(this.tsneOption)
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
          large: false,
          largeThreshold: 1,
          progressive: 400,
          progressiveThreshold: 3000
        }
      }).value()
    },
    changeTsneScatter (notMerge) {
      this.tsneChart.setOption(this.tsneOption, notMerge)
    },
    setTree: function () {
      let dom = document.getElementById('tree')
      this.treeChart = this.$echarts.init(dom, 'dark')
      window.addEventListener('resize', this.treeChart.resize)
      this.treeChart.setOption(this.treeOption)
    },
    changeTree (notMerge) {
      console.log('changetree')
      this.treeChart.setOption(this.treeOption, notMerge)
    },
    getDataFromBackend () {
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
    getGeneDataFromBackend () {
      const path = `http://127.0.0.1:5000/api/gene?gene_name=${this.geneChartControl.gene}&mc_type=${this.geneChartControl.mc_type}&normalize=${this.geneChartControl.norm}`
      axios.get(path)
        .then(response => {
          this.geneDataset = response.data.dataset
          this.geneInfo = response.data.gene_info
        })
        .catch(error => {
          console.log(error)
        })
    },
    setGeneScatter () {
      let dom = document.getElementById('gene_chart')
      this.geneChart = this.$echarts.init(dom, 'dark')
      window.addEventListener('resize', this.geneChart.resize)
      this.geneChart.setOption(this.geneOption)
    },
    changeGeneScatter (notMerge) {
      this.geneChart.setOption(this.geneOption, true)
    },
    updateGeneControl () {
      this.geneChartControl = this.geneChartControlForm
      this.getGeneDataFromBackend()
    }
  },
  mounted () {
    this.$nextTick(
      function () {
        this.setTsneScatter()
        this.setTree()
        this.setGeneScatter()
      }
    )
  },
  created () {
    this.$nextTick(
      function () {
        this.$echarts.registerTheme('dark', darkTheme)
        this.getDataFromBackend()
        this.getGeneDataFromBackend()
      }
    )
  }
}

function sortNumber (a, b) {
  return a - b
}

function quantile (array, percentile) {
  array.sort(sortNumber)
  let index = percentile / 100.0 * (array.length - 1)
  let result = null
  if (Math.floor(index) === index) {
    result = array[index]
  } else {
    let i = Math.floor(index)
    let fraction = index - i
    result = array[i] + (array[i + 1] - array[i]) * fraction
  }
  console.log(percentile)
  console.log(index)
  console.log(Math.floor(index))
  console.log(result)
  return result
}
</script>

<style scoped>
</style>
