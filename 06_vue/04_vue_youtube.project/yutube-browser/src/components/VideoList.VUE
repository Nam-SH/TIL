<template>
  <div>
    <ul>
      VideoList
      {{ videos.length }}
    </ul>

  </div>
</template>

<script>
  export default {
    name: 'VideoList',
    props: {
      videos: {
        type: Array,
        required: true,
      }
    }
  }
</script>

<style lang="scss" scoped>

</style>