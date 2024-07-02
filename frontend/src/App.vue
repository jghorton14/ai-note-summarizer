<template>
  <div id="app">
    <h1>Drag and Drop File Upload</h1>
    <div 
      class="drop-area" 
      @dragover.prevent 
      @dragenter.prevent 
      @drop.prevent="handleDrop"
    >
      Drop files here
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  methods: {
    async handleDrop(event) {
      const files = event.dataTransfer.files;
      const formData = new FormData();
      
      for (let i = 0; i < files.length; i++) {
        formData.append('file', files[i]);
      }

      try {
        const response = await axios.post('http://localhost:5001/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
        console.log(response.data);
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>

<style>
.drop-area {
  width: 300px;
  height: 200px;
  border: 2px dashed #cccccc;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 50px auto;
  cursor: pointer;
}
</style>
