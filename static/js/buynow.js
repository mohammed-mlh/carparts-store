const BuynowBtn = document.querySelector('#buynow-btn')
const BuynowForm = document.querySelector('#buynow-form')


console.log(BuynowBtn);
BuynowForm.addEventListener('submit', e => {
  e.preventDefault()
  console.log(Object.fromEntries(new FormData(BuynowForm))
)
})