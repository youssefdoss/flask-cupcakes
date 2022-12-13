"use strict";

let $cupcakeList = $("ul");
// Add a global constant for the base url
/** getCupcakeList: Returns all cupcakes from the API */
async function getCupcakeList() {
  // Just return response.data.cupcakes
  return await axios.get("http://localhost:5001/api/cupcakes");
}

/** addCupcakesToPage: Append all cupcakes to the UI */
async function addCupcakesToPage() {
  $cupcakeList.empty();
  let response = await getCupcakeList();

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

/** getFormValues: Pull all values out of the form */
function getFormValues() {
  const flavor = $('#flavor').val();
  const size = $('#size').val();
  const rating = $('#rating').val();
  const image = $('#image').val();

  return {flavor: flavor, size: size, rating: rating, image: image};
}

async function createCupcake() {
  const formValues = getFormValues();
  await axios.post('http://localhost:5001/api/cupcakes', formValues);
  await addCupcakesToPage();
}

$('button').on('click', createCupcake);

addCupcakesToPage();
