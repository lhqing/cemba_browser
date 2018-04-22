<template>
  <div id="app">
    <el-container>
      <el-header>
        <HeaderCompo></HeaderCompo>
      </el-header>
      <el-main>
        <router-view></router-view>
      </el-main>
      <el-footer>
        <FooterCompo></FooterCompo>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
import HeaderCompo from '@/components/HeaderCompo'
import FooterCompo from '@/components/FooterCompo'

export default {
  name: 'App',
  components: {
    'HeaderCompo': HeaderCompo,
    'FooterCompo': FooterCompo
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 1px;
}
</style>
