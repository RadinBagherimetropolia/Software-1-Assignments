const form = document.getElementById("searchForm");
const input = document.getElementById("query");

form.addEventListener("submit", function(event) {
    event.preventDefault();

    const searchValue = input.value.trim();

    if (searchValue === "") {
        console.log("Please enter a TV show name.");
        return;
    }
    fetch(`https://api.tvmaze.com/search/shows?q=${searchValue}`)
        .then(response => response.json())
        .then(data => {
            console.log("Search result:", data);
        })
        .catch(error => {
            console.error("Error fetching data:", error);
        });
});
