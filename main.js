'use strict';

let $cupcakeList = $('<ul>');

async function getCupcakeList() {
    return await axios.get('/api/cupcakes');
}

function addCupcakesToPage(response) {
    for (let i = 0; i < response.length; i++) {
        $cupcakeList.append(response.cupcakes[i])
    }
}

