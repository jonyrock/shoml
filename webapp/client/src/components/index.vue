<template>
  <div class="container">
    <div class="row text-center">
      <div class="col-xs-12">
        <h1>Shoml<br> <small> Shoes photo resolver </small></h1>
      </div>
    </div>
    <hr>
    <div class="row text-center">
      <div class="col-xs-8 col-xs-offset-2">
        <uploader />
      </div>
    </div>
  </div>
</template>

<script>

export default {
  components: {
    'uploader': require('./partials/uploader')
  }
}

</script>


<style scoped>
h1 {
  font-size: 40px;
}
.btn {
  display: block;
  margin-bottom: 20px
}
</style>
