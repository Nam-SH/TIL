<template>
 <div id="app-2">
  <p v-text="message"></p>
  <p>{{ message }}</p>
</div>
</template>


<script>
  export default {
    name: 'app-2',
    data () {
      return {
        message: '<h1> hi </h1>',
      }
    }
  }
</script>


<style>

</style>