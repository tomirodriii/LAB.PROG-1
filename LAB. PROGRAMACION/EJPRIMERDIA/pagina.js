
let button1 = document.getElementById("calculo")
let montop = document.getElementById("dineropagado")
let porcprop = document.getElementById("propinas")


  button1.addEventListener ("click", function () {

    
    let datoValue = parseFloat(montop.value)
    let prop = parseFloat(porcprop.value)

    let propina = datoValue * prop
    let total = propina + datoValue

    let propTotal = document.getElementById("propinaResultado") 
    let Total = document.getElementById("totalResultado")

    propTotal.textContent = "Propina: $" + propina
    Total.textContent = "Total: $" + total

    console.log("Tu propina es de:", propTotal, "Y tu total pagado es:", Total);
  })





