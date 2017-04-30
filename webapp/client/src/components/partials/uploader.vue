<template>
  <div style="position:relative;">

    <form enctype="multipart/form-data">
      <input name="file" type="file" />
      <input type="button" value="Upload" />
    </form>
    <progress></progress>
    <!-- <form action="/upload" method="post" enctype="multipart/form-data">
      Select image to upload:
      <input type="file" name="file" id="file">
      <input type="submit" value="Upload Image" name="submit">
    </form> -->

    <div v-if="results">
      
    </div>
  </div>
</template>

<script>

const $ = require('jquery');
export default {
  mounted: function() {
    var $file = $(this.$el).find(':file');
    var $progress = $(this.$el).find('progress');
    $file.on('change', function() {
      var file = this.files[0];
    });

    var _this = this;
    $(this.$el).find(':button').on('click', function() {
      $.ajax({
          // Your server script to process the upload
          url: '/upload',
          type: 'POST',

          // Form data
          data: new FormData($(_this.$el).find('form')[0]),

          // Tell jQuery not to process data or worry about content-type
          // You *must* include these options!
          cache: false,
          contentType: false,
          processData: false,

          // Custom XMLHttpRequest
          xhr: function() {
            var myXhr = $.ajaxSettings.xhr();
            if (myXhr.upload) {
                // For handling the progress of the upload
                myXhr.upload.addEventListener('progress', function(e) {
                    if (e.lengthComputable) {
                        $progress.attr({
                            value: e.loaded,
                            max: e.total,
                        });
                    }
                } , false);
            }
            return myXhr;
          },
          success: function(data, textStatus, jqXHR) {
            if(typeof data.error === 'undefined') {
              _this.results = data;
            } else {
              console.log('ERRORS: ' + data.error);
            }
        },
      });
    });
  },

  data: function() {
    return {
      results: undefined
    }
  }
}
</script>

<style>
</style>
