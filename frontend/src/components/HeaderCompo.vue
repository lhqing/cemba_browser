<template>
  <el-menu
    :default-active="$route.path"
    class="el-menu-demo"
    mode="horizontal"
    @select="handleSelect"
    background-color="#545c64"
    text-color="#fff"
    active-text-color="#ffd04b"
    :router=true
    :unique-opened=true>
    <el-menu-item index="/">Home</el-menu-item>
    <el-submenu index="/overview">
      <template slot="title">Overview</template>
      <el-menu-item index="/overview/rs1">RS1</el-menu-item>
      <el-menu-item index="/overview/rs2">RS2</el-menu-item>
      <el-menu-item index="/overview/compute">Computed Data Sets</el-menu-item>
    </el-submenu>
    <el-submenu index="/celltype">
      <template slot="title">Cell Type</template>
      <el-menu-item index="/celltype/cluster">Cluster</el-menu-item>
      <el-menu-item index="/celltype/gene">Marker Gene</el-menu-item>
      <el-menu-item index="/celltype/dmr">DMR</el-menu-item>
    </el-submenu>
    <el-menu-item index="/about">About</el-menu-item>
  </el-menu>
</template>

<script>
export default {
  data () {
    return {
      activeIndex: '1',
      activeIndex2: '1'
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>
