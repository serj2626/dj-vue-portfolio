<template>
  <footer
    class="d-flex flex-wrap justify-content-around align-items-center py-3 my-4"
  >
    <div class="col-md-4 d-flex align-items-center gap-4">
      <a
        href="/"
        class="mb-3 me-2 mb-md-0 text-muted text-decoration-none lh-1"
      >
        <svg class="bi" width="30" height="24">
          <use xlink:href="#bootstrap"></use>
        </svg>
      </a>
      <span class="text-white fs-6">© 2024 Boytsov S.V   SPB</span>
    </div>

    <ul class="nav col-md-4 justify-content-end list-unstyled d-flex gap-2">
      <li class="ms-3">
        <a class="text-white" href="#"
          ><i class="fa-brands fa-telegram fa-xl" style="color: #74c0fc"></i
        ></a>
      </li>
      <li class="ms-3">
        <a class="text-white" href="#"
          ><i class="fa-brands fa-instagram fa-xl" style="color: #ffd43b"></i
        ></a>
      </li>
      <li class="ms-3">
        <a class="text-white" href="#"
          ><i class="fa-brands fa-linkedin fa-xl" style="color: #74c0fc"></i
        ></a>
      </li>
      <li class="ms-3">
        <a class="text-white" href="#"
          ><i class="fa-brands fa-vk fa-xl" style="color: #74c0fc"></i
        ></a>
      </li>
      <li class="ms-3">
        <a class="text-white" href="#"
          ><i class="fa-brands fa-github fa-xl" style="color: white"></i
        ></a>
      </li>
    </ul>
  </footer>
</template>

<style scoped>
li {
  transition: all .3s ease-in;

  &:hover {
    scale: 1.4;
  }
}
</style>
