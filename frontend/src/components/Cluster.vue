<template>
  <div>
    <el-container>
      <el-aside class="aside bg-purple">
        Aside
      </el-aside>
      <el-main class="main bg-purple-light">
        <div id="myChart" :style="{width: '400px', height: '400px'}"></div>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'hello',
  data () {
    return {
      data: [
        [10.0, 8.04],
        [8.0, 6.95],
        [13.0, 7.58],
        [9.0, 8.81],
        [11.0, 8.33],
        [14.0, 9.96],
        [6.0, 7.24],
        [4.0, 4.26],
        [12.0, 10.84],
        [7.0, 4.82],
        [5.0, 5.68]
      ]
    }
  },
  mounted () {
    this.drawLine()
  },
  methods: {
    drawLine () {
      // 基于准备好的dom，初始化echarts实例
      let myChart = this.$echarts.init(document.getElementById('myChart'))
      // 绘制图表
      myChart.setOption({
        xAxis: {},
        yAxis: {},
        series: [{
          symbolSize: 20,
          data: this.data,
          type: 'scatter'
        }]
      })
    }
  }
}
</script>

<style>
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .aside {
    min-height: 500px;
    min-width: 20%;
  }
  .main{
    border-radius: 4px;
    min-height: 500px;
    min-width: 50%;
  }
</style>
