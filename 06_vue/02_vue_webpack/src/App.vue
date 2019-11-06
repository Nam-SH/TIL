<template>
<div>
  <h1>여기는 vue 최상위 문서</h1>
  <todo-list category="취업특강"></todo-list>
  <todo-list category="SSAFY"></todo-list>
  <todo-list category="기타"></todo-list>
  </div>
</template>

<script>
  import TodoList from './components/TodoList.vue'

  export default {
    components: {
      TodoList
    }
  }
</script>

<style>

</style>