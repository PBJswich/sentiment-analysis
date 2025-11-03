document.addEventListener('DOMContentLoaded', () => {
    // Fetch and display Fear & Greed Index
    const fearGreedValue = document.getElementById('fear-greed-value');
    fetch('/fear-greed-index')
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                fearGreedValue.textContent = 'Error loading Fear & Greed Index.';
            } else {
                fearGreedValue.textContent = `${data.value} (${data.sentiment})`;
            }
        })
        .catch(error => {
            console.error('Error fetching Fear & Greed Index:', error);
            fearGreedValue.textContent = 'Error loading Fear & Greed Index.';
        });

    // Fetch and display stock news
    const articlesContainer = document.getElementById('articles');
    fetch('/stock-news')
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                articlesContainer.innerHTML = '<p>Error loading stock news.</p>';
                return;
            }

            articlesContainer.innerHTML = ''; // Clear existing articles

            data.forEach(article => {
                const articleElement = document.createElement('div');
                articleElement.classList.add('article');

                const titleElement = document.createElement('h3');
                const linkElement = document.createElement('a');
                linkElement.textContent = article.title;
                linkElement.href = article.link;
                linkElement.target = '_blank';
                titleElement.appendChild(linkElement);

                const sentimentElement = document.createElement('p');
                sentimentElement.innerHTML = `Sentiment: <span class="sentiment">${article.sentiment}</span>`;

                const sourceElement = document.createElement('p');
                sourceElement.textContent = `Source: ${article.source}`;

                articleElement.appendChild(titleElement);
                articleElement.appendChild(sentimentElement);
                articleElement.appendChild(sourceElement);

                articlesContainer.appendChild(articleElement);
            });
        })
        .catch(error => {
            console.error('Error fetching stock news:', error);
            articlesContainer.innerHTML = '<p>Error loading stock news.</p>';
        });
});
