var form = document.getElementById('form')
  form.addEventListener('submit',function(event){
    event.preventDefault()

    var Subject = document.getElementById('Subject').value

    console.log(Subject)

    var Message = document.getElementById('Message').value

    console.log(Message)

  })