<template>
  <div style="position:relative;">

    <form enctype="multipart/form-data">
      <input name="file" type="file" />

      <input v-if="!loading" type="button" value="Upload" />
      <span v-if="loading" type="button" value="Upload"> Loading </span>
    </form>
    <progress></progress>

    <div v-if="results" id="results">
      <hr/>
      <div v-for="item in results.candidates">
        <img :src="item.image" /> <br/>
        <small> n: {{ item.name }} w: {{ item.weight.toFixed(3) }}</small>
      </div>
    </div>
  </div>
</template>

<script>

const $ = require('jquery');
export default {
  mounted: function() {
    var _this = this;

    var $file = $(this.$el).find(':file');
    var $progress = $(this.$el).find('progress');

    this.$file = $file;
    this.$progress = $progress;
    $file.on('change', function() {
      var file = this.files[0];
    });


    $(this.$el).find(':button').on('click', function() {
      _this.results = undefined;
      _this.loading = true;
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
              _this.getResults(data);
            } else {
              console.log('ERRORS: ' + data.error);
            }
          },
      });
    });
  },

  data: function() {
    return {
      results: undefined,
      loading: false
    }
  },
  methods: {
    getResults: function(data) {
      this.loading = false;
      this.results = data;
      this.$file.val('');
    }
  }
}
</script>

<style scoped>
  #results img{
    width: 200px;
  }
  #results small {
    color: gray;
  }
</style>
