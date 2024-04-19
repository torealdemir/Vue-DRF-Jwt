<template>
    <h1 class="d-flex justify-content-center my-4 text-success">Projects!</h1>

    <div class="container-sm" >
        <div class="control">
            <form @submit.prevent="submitForm">
                <div class="mb-3">
                    <label for="project-name" class="form-label">Project Name</label>
                    <input type="text" class="form-control" id="project-name">
                </div>
                <div class="mb-3">
                    <label for="project-description" class="form-label">Description</label>
                    <input type="text" class="form-control" id="project-description">
                </div>
                <div class="mb-3">
                    <label for="short-description" class="form-label">Short Description</label>
                    <input type="text" class="form-control" id="short-description">
                </div>
                <div class="mb-3">
                    <label for="project-students" class="form-label">Active Students</label>
                    <input type="text" class="form-control" id="project-students">
                </div>
                <div class="my-4">
                    <label for="status">Choose a status:</label>

                    <select name="status" id="status" class="mx-3">
                    <option value="active">Active</option>
                    <option value="passive">Passive</option>

                    </select>

                </div>
               
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
export default {
    name:'Projects',
}

</script>

<style>
li {
    list-style:none;
}

li {
    list-style: none;
}
</style>