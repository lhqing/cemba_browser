<template>
  <div>
    <el-col>
      <el-main class="main bg-purple-light">
        Main
      </el-main>
      <el-main>
        <el-collapse v-model="activeNames" @change="handleChange" :accordion=true>
          <el-collapse-item title="Slice 3" name="1">
            <el-container>
              <el-row :gutter="20" type="flex" justify="center">
                <el-col :span="5" :offset="0">
                  <img src="../assets/test_atlas.svg" class="atlas">
                </el-col>
                <el-col :span="15" :offset="8" >
                  <el-table
                    ref="multipleTable"
                    :data="tableData"
                    tooltip-effect="dark"
                    height="300"
                    style="width: 100%"
                    @selection-change="handleSelectionChange"
                    :default-sort = "{prop: 'region', order: 'ascending'}">
                    <el-table-column
                      type="selection"
                      width="55">
                    </el-table-column>
                    <el-table-column
                      prop="region"
                      label="region"
                      width="120"
                      sortable>
                    </el-table-column>
                    <el-table-column
                      prop="name"
                      label="name"
                      width="120"
                      sortable>
                    </el-table-column>
                    <el-table-column
                      prop="count"
                      label="cell count"
                      width="120"
                      sortable>
                    </el-table-column>
                  </el-table>
                </el-col>
              </el-row>
            </el-container>
          </el-collapse-item>
          <el-collapse-item title="Slice 1" name="2">
            <div>atlas</div>
            <div>table</div>
          </el-collapse-item>
          <el-collapse-item title="Slice 2" name="3">
            <div>atlas</div>
            <div>table</div>
          </el-collapse-item>
          <el-collapse-item title="Slice 4" name="4">
            <div>atlas</div>
            <div>table</div>
          </el-collapse-item>
        </el-collapse>
      </el-main>
    </el-col>
  </div>
</template>

<script>
export default {
  data () {
    return {
      activeNames: ['1'],
      tableData: [{
        region: '3A',
        name: 'XXX',
        count: '1000'
      }, {
        region: '3B',
        name: 'XXX',
        count: '1001'
      }, {
        region: '3C',
        name: 'XXX',
        count: '1002'
      }, {
        region: '3D',
        name: 'XXX',
        count: '1003'
      }, {
        region: '3E',
        name: 'XXX',
        count: '1000'
      }, {
        region: '3F',
        name: 'XXX',
        count: '1234'
      }, {
        region: '3G',
        name: 'XXX',
        count: '1321'
      }, {
        region: '3G',
        name: 'XXX',
        count: '1414'
      }, {
        region: '3G',
        name: 'XXX',
        count: '1523'
      }]
    }
  },
  methods: {
    handleChange (val) {
      console.log(val)
    },
    toggleSelection (rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.multipleTable.toggleRowSelection(row)
        })
      } else {
        this.$refs.multipleTable.clearSelection()
      }
    },
    handleSelectionChange (val) {
      this.multipleSelection = val
      console.log(this.multipleSelection)
    }
  },
  components: {
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
    min-width: 200px;
  }
  .main{
    border-radius: 4px;
    min-height: 500px;
    min-width: 600px;
  }
  .atlas{
    height: 300px;
    width: 400px;
  }
  svg:hover circle{
    fill: #F6831D;
    stroke-dashoffset: 0;
    stroke-dasharray: 700;
    stroke-width: 2;
  }
</style>
