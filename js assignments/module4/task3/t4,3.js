const form = document.getElementById("searchForm");
const input = document.getElementById("query");
const resultsDiv = document.getElementById("results");

form.addEventListener("submit", function(event) {
    event.preventDefault();

    const searchValue = input.value.trim();

    if (searchValue === "") {
        console.log("Please enter a TV show name.");
        return;
    }
    resultsDiv.innerHTML = '';

    fetch(`https://api.tvmaze.com/search/shows?q=${encodeURIComponent(searchValue)}`)
        .then(response => response.json())
        .then(data => {
            data.forEach(tvShow => {
                const show = tvShow.show;

                const article = document.createElement("article");

                const h2 = document.createElement("h2");
                h2.textContent = show.name;

                const link = document.createElement("a");
                link.href = show.url;
                link.textContent = "Details";
                link.target = "_blank";

                const img = document.createElement("img");
                img.src = show.image?.medium || ""; // optional chaining
                img.alt = show.name;

                const summaryDiv = document.createElement("div");
                summaryDiv.innerHTML = show.summary || "No summary available";

                article.appendChild(h2);
                article.appendChild(link);
                article.appendChild(img);
                article.appendChild(summaryDiv);

                resultsDiv.appendChild(article);
            });
        })
        .catch(error => {
            console.error("Error fetching data:", error);
        });
});
