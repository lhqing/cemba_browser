<template>
  <div>
    <el-container>
      <el-col :span="24">
        <el-main class="grid-content bg-purple-light">
          What is CEMBA?
        </el-main>
        <el-main class="grid-content bg-purple">
          What data do we have?
        </el-main>
        <el-main class="grid-content bg-purple-light">
          Basic status?
        </el-main>
      </el-col>
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
  .grid-content {
    border-radius: 4px;
    min-height: 400px;
  }
</style>
