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
                    <input type="text" v-model="project.image" class="form-control" id="short-description">
                </div>
                <div class="mb-3">
                    <label for="project-students" class="form-label">Active Students</label>
                    <input type="text" v-model="project.students" class="form-control" id="project-students">
                </div>
                <!-- <div class="my-4">
                    <label for="status">Choose a status:</label>

                    <select v-model="project.status" name="status" id="status" class="mx-3">
                    <option value="true">Active</option>
                    <option value="false">Passive</option>

                    </select>

                </div> -->
               
                <div class="mb-3">
                    <label for="project-img" class="form-label">Image</label>
                    <input type="file" class="form-control" id="project-img">
                </div>
               
                <div class="d-flex align-items-center justify-content-center my-4">
                    <button type="submit" class="btn btn-primary align-items-center">Submit</button>
                </div>
                
            </form>
        </div>
    </div>
    <footer class="bg-dark">
        <div class="container py-4 text-center text-secondary">
            <span>All Rights Reserved @Metu Engineering Section</span>
            <div class="row py-6 mt-3">
            <ul>
                <li>
                <p>Adress:Odtu Engineering Section Material Engineering</p>
                </li>
                <li>
                <a href="#">Contact Us!</a>
                </li>
            </ul>
            
            </div>
            <div>
            </div>
        </div>
</footer>
</template>

<script>
import axios from 'axios';
export default {
    name:'Projects',
    data(){
        return {
            project: {
                title:'',
                content:'',
                short_description:'',
                image:null,
                students:'',
                // status:null,
            }
        }
    },
    methods: {
    async submitForm(){
        const token = localStorage.getItem('access')
        const formData = new FormData();

        formData.append('title', this.project.title);
        formData.append('content', this.project.content);
        formData.append('short_description', this.project.short_description);
        formData.append('students', this.project.students);
        formData.append('image', this.project.image);

        try {
            console.log(formData)
            const response = await axios.post('ToCo/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                    Authorization: `JWT ${token}`,
                },
            });
            // console.log(formData)
            // this.project.title = '';
            // this.project.content = '';
            // this.project.short_description='';
            // this.project.image=null;
            // this.project.students='';

            alert('Project added!');

        }catch (error){
        console.log(error);
    }
},
handleImageUpload(event){
    const file = event.target.files[0];
    this.blog.image=file;
}
    }}



</script>

<style>
li {
    list-style:none;
}

li {
    list-style: none;
}
</style>