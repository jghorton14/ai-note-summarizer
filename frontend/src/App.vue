<template>
  <div id="app">
    <h1>Drag and Drop File Upload</h1>
    <div 
      class="drop-area" 
      @dragover.prevent 
      @dragenter.prevent 
      @drop.prevent="handleDrop"
      @click="openFileDialog"
    >
      <template v-if="!isUploading">
        Drop files here or click to select
      </template>
      <div v-else class="spinner"></div>
    </div>
    <input 
      type="file" 
      ref="fileInput" 
      style="display: none" 
      @change="handleFileSelect" 
      multiple
    >
    <div v-if="uploadedFiles.length > 0" class="file-list">
      <h3>Uploaded Files:</h3>
      <ul>
        <li v-for="file in uploadedFiles" :key="file">{{ file }}</li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const fileInput = ref(null);
const isUploading = ref(false);
const uploadedFiles = ref([]);

const handleDrop = async (event) => {
  const files = event.dataTransfer.files;
  await uploadFiles(files);
};

const openFileDialog = () => {
  fileInput.value.click();
};

const handleFileSelect = async (event) => {
  const files = event.target.files;
  await uploadFiles(files);
};

const uploadFiles = async (files) => {
  const formData = new FormData();
  
  uploadedFiles.value = [];
  
  for (let i = 0; i < files.length; i++) {
    formData.append('file', files[i]);
    uploadedFiles.value.push(files[i].name);
  }

  try {
    isUploading.value = true;
    const response = await axios.post('http://localhost:5001/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    console.log(response.data);
  } catch (error) {
    console.error(error);
    uploadedFiles.value = []; // Clear the list if upload fails
  } finally {
    isUploading.value = false;
  }
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

.spinner {
  border: 4px solid rgba(0, 0, 0, 0.1);
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border-left-color: #09f;
  animation: spin 1s ease infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.file-list {
  margin-top: 20px;
  text-align: center;
}

.file-list ul {
  list-style-type: none;
  padding: 0;
}

.file-list li {
  margin: 5px 0;
}
</style>