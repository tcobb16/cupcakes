async function getCupcakes() {
    console.log("page loaded");
    const cupcakesResponse = await axios.get("/api/cupcakes");
    const $list = $("#cupcakeList");
    for (cupcake of cupcakesResponse.data.cupcakes){
        const $li = $("li");
        const $p = $("p");
        $p.val(`flavor:${cupcake["flavor"]}`);
        console.log(`cupcake loaded: ${cupcake["flavor"]}`);

        // $li.append("<p></p>");
        $list.append($li);
    }
    console.log("page done");
}

getCupcakes();