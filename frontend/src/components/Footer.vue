<template>
<footer class="d-flex flex-wrap justify-content-around align-items-center py-3 my-4 border-footer">

    <div class="col-md-4 d-flex align-items-center">
      <a href="/" class="mb-3 me-2 mb-md-0 text-muted text-decoration-none lh-1">
        <svg class="bi" width="30" height="24"><use xlink:href="#bootstrap"></use></svg>
      </a>
      <span class="text-white">© 2024 Boytsov S.V., SPB</span>
    </div>

    <ul class="nav col-md-4 justify-content-end list-unstyled d-flex">
      <li class="ms-3"><a class="text-white" href="#"><i class="fa-brands fa-telegram fa-xl" style="color: #74C0FC;"></i></a></li>
      <li class="ms-3"><a class="text-white" href="#"><i class="fa-brands fa-instagram fa-xl" style="color: #ef3506;"></i></a></li>
      <li class="ms-3"><a class="text-white" href="#"><i class="fa-brands fa-linkedin fa-xl" style="color: #74C0FC;"></i></a></li>
    </ul>

  </footer>
</template>

<style scoped>
.border-footer {
  animation-name: border1;
  animation-duration: 2s;
  animation-iteration-count: infinite;
  animation-timing-function: linear;
  
  /* border-top: 1px solid #03e9f4; */
}

@keyframes border1 {
  0% {
    border-top: 1px solid #9fecf0;
  }
  50% {
    border-top: 1px solid #48e1ea;
  }
  100% {
    border-top: 1px solid #03e9f4;
  }
}
</style>