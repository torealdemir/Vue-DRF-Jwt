<template>
    <h1 class="d-flex justify-content-center my-4 text-success">Projects!</h1>

    <div class="container-sm" >
        <div class="control">
            <form @submit.prevent="submitForm">
                <div class="mb-3">
                    <label for="project-name" class="form-label">Project Name</label>
                    <input type="text" v-model="project.title" class="form-control" id="project-name">
                </div>
                <div class="mb-3">
                    <label for="project-description" class="form-label">Description</label>
                    <input type="text" v-model="project.content" class="form-control" id="project-description">
                </div>
                <div class="mb-3">
                    <label for="short-description" class="form-label">Short Description</label>
                    <input type="text" v-model="project.short_description" class="form-control" id="short-description">
                </div>
                <div class="mb-3">
                    <label for="project-students" class="form-label">Active Students</label>
                    <input type="text" v-model="project.students" class="form-control" id="project-students">
                </div>
                <div class="my-4">
                    <label for="status">Choose a status:</label>

                    <select v-model="project.status" name="status" id="status" class="mx-3">
                    <option value="true">Active</option>
                    <option value="false">Passive</option>

                    </select>

                </div>
               
                <div class="mb-3">
                    <label for="project-img" class="form-label">Image</label>
                    <input type="file" class="form-control" v-on:change="handleImageUpload" id="project-img">
                </div>
               
                <div class="d-flex align-items-center justify-content-center my-4">
                    <button type="submit" class="btn btn-primary align-items-center">Submit</button>
                </div>
                
            </form>
        </div>
    </div>
<Footer />
</template>

<script>
import axios from 'axios';
import Footer from '@/components/Footer.vue'

export default {
  name: 'Projects',
  components: {
    Footer,
  },
  data() {
    return {
      project: {
        title: '',
        content: '',
        short_description: '',
        image: null,
        students: '',
      },
    };
  },
  methods: {
    async submitForm() {
      const token = localStorage.getItem('access');
      const formData = new FormData();
    
      formData.append('title', this.project.title);
      formData.append('content', this.project.content);
      formData.append('short_description', this.project.short_description);
      formData.append('students', this.project.students);
      formData.append('image', this.project.image);

      try {
        const response = await axios.post('ToCo/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            Authorization: `JWT ${token}`,
          },
        });

        console.log(response.data); // Log the response data
        alert('Project added!');
      } catch (error) {
        console.log(error); // Log any error details
        alert('Failed to add project.');
      }
    },
    handleImageUpload(event) {
      const file = event.target.files[0];
      this.project.image = file;
    },
  },
};
</script>
<style>
li {
    list-style:none;
}

</style>