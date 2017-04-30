<template>
  <div style="position:relative;">
    <!-- <vuc

      title="Add a photo with shoe"
      postAction='/upload'
    /> -->
    <form action="/upload" method="post" enctype="multipart/form-data">
      Select image to upload:
      <input type="file" name="file" id="file">
      <input type="submit" value="Upload Image" name="submit">
    </form>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      events: {
        progress(file, component) {
            console.log('progress ' + file.progress);
        },
        after(file, component) {
            console.log('after');
        },
        before(file, component) {
            console.log('before');
        }
      }
    }
  },
  components: {
    vuc: require('vue-upload-component')
  }
}
</script>

<style>
</style>
