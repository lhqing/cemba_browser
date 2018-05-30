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
</style>
