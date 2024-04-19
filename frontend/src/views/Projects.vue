<template>
    <h1 class="d-flex justify-content-center my-4 text-success">Projects!</h1>

    <div class="container-sm" >
        <div class="control">
            <form @submit.prevent="submitForm">
                <div class="mb-3">
                    <label for="project-name" class="form-label">Project Name</label>
                    <input type="text" v-model="username" class="form-control" id="project-name">
                </div>
                <div class="mb-3">
                    <label for="project-description" class="form-label">Description</label>
                    <input type="password" v-model="password" class="form-control" id="project-description">
                </div>
                <div class="mb-3">
                    <label for="short-description" class="form-label">Short Description</label>
                    <input type="password" v-model="repassword" class="form-control" id="short-description">
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>
    </div>

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
</style>