<script setup>
import axios from "axios";
import { reactive } from "vue";
import { useToast } from "vue-toastification";

const toast = useToast();

const form = reactive({
  name: "",
  email: "",
  message: "",
});

const validateForm = () => {
  if (!form.name || !form.email || !form.message) {
    toast.error("Заполните все поля");
    return false;
  }
  return true;
}

const submit = async () => {
  if (validateForm()) {
    try{
      await axios.post("api/contacts/create/", { ...form });
      toast.success("Сообщение успешно отправлено");
      form.name = "";
      form.email = "";
      form.message = "";
    }catch{
      toast.error("Что-то пошло не так");
    }
    
  }
};
</script>

<template>
  <div
    class="col-md-4 mx-auto text-white py-5"
  >
    <p class="text-center mb-5 title">Связаться с мной</p>
    <form @submit.prevent="submit" method="post">
      <div class="mb-3">
        <label for="name" class="form-label">Имя</label>
        <input
          v-model="form.name"
          type="text"
          class="form-control"
          id="name"
          name="name"
        />
      </div>
      <div class="mb-3">
        <label for="email" class="form-label">Почта</label>
        <input
          v-model="form.email"
          type="email"
          class="form-control"
          id="email"
          name="email"
        />
      </div>
      <div class="mb-3">
        <label for="message" class="form-label">Сообщение</label>
        <textarea
          v-model="form.message"
          class="form-control"
          id="message"
          name="message"
        ></textarea>
      </div>
      <button class="btn w-100">Отправить</button>
    </form>
  </div>
</template>

<style scoped>
.title {
  font-size: 3rem;
  color: #c61fad;
  text-shadow: 2px 2px 5px #03e9f4;
}

.btn {
  background: linear-gradient(90deg, #42494f, #03e9f4);
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 10px;
  margin-top: 20px;
  font-size: 20px;
}

.btn:hover {
  background: linear-gradient(90deg, #42494f, #c61fad);
  color: white;
}

input,
textarea {
  background: #42494f;
  border: none;
  padding: 10px 15px;
  border-radius: 10px;
  margin-top: 20px;
  font-size: 20px;
  color: white;
}

input:focus,
textarea:focus {
  border-color: #03e9f4;
}
</style>
