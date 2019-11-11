<template>
  <div id="app">
    <search-bar @inputChange="onInputChange"> </search-bar>
    <video-list :videos="videos"></video-list>
  </div>
</template>

<script>
  import axios from 'axios'
  import SearchBar from './components/SearchBar'
  import videoList from './components/VideoList'
  const API_KEY = 'AIzaSyCXoglBd5AKcRnpoZ_mi95K_VTwPArdyw0'
  const API_URL = 'https://www.googleapis.com/youtube/v3/search'

  export default {
    name: 'App',
    data() {
      return {
        videos: []
      }
    },
    components: {
      SearchBar,
      },
    methods: {
      onInputChange(inputvalue) {
        axios.get(API_URL, {
          params: {
            key: API_KEY,
            type: 'video',
            part: 'snippet',
            q: inputvalue,
          }
        })
        .then(response => {
          this.videos = response.data.items
          console.log(response)
        })
        .catch(err => {
          console.log(err)
        })
      }
    },
  }
</script>

<style>
</style>