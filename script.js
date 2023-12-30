
// get the html file
document.getElementById("getData").addEventListener("click", fetchData);

function fetchData() {
    // Replace the URL with the actual URL of the webpage you want to fetch data from
    const url = "https://www.youtube.com/results?search_query=how+to+integrate+python+code+withjs";

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Network response was not ok: ${response.statusText}`);
            }
            return response.text();
        })
        .then(html => {
            // Extract the data from the HTML (modify this part based on the webpage structure)
            const data = extractDataFromHTML(html);

            // Handle the extracted data, for example, update the result container
            document.getElementById("resultContainer").innerHTML = JSON.stringify(data, null, 2);
        })
        .catch(error => {
            console.error("Error fetching data:", error);
            document.getElementById("resultContainer").innerHTML = "Error fetching data";
        });
}

function extractDataFromHTML(html) {
    // Implement your logic to extract data from the HTML
    // This could involve using methods like DOM manipulation, regular expressions, etc.
    // For demonstration purposes, let's assume you want to extract text inside all <p> elements
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');
    const paragraphs = doc.querySelectorAll('p');

    const extractedData = [];
    paragraphs.forEach(p => {
        extractedData.push(p.textContent.trim());
    });

    return extractedData;
}