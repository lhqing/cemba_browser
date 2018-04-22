<template>
  <div>
    <el-container>
      <el-aside class="aside bg-purple">
        Aside
      </el-aside>
      <el-container>
        <el-main class="main bg-purple-light">
          Main
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

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
</style>
