"use strict";

let $cupcakeList = $("ul");

async function getCupcakeList() {
  return await axios.get("http://localhost:5001/api/cupcakes");
}

async function addCupcakesToPage() {
  let response = await getCupcakeList();
  console.log(response);
  for (let i = 0; i < response.data.cupcakes.length; i++) {
    let cupcake = response.data.cupcakes[i];
    $cupcakeList.append(`
    <li>
      <h3>${cupcake.flavor}</h3>
      <img src="${cupcake.image}" style="width: 200px">
      <ul>
        <li>Size - ${cupcake.size}</li>
        <li>Rating - ${cupcake.rating}</li>
      </ul>
    </li>`);
  }
}

// let response = await getCupcakeList();
addCupcakesToPage();
