<template>
  <div>
    <el-container>
      <el-aside class="aside bg-purple">
        Aside
      </el-aside>
      <el-main class="main bg-purple-light">
        <TsneVisual></TsneVisual>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import TsneVisual from './TsneVisual'

export default {
  name: 'cluster',
  components: {
    'TsneVisual': TsneVisual
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
