function fetchUrlAndTitle() {

    const pageTitle = document.title
    const pageUrl = document.location.href
    return {
        'title': pageTitle,
        'url': pageUrl
    }
}

async function sendData(dataFetcher) {
    const url = new URL(
        'http://localhost:56789'
    )

    await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(
                dataFetcher()
            )
        }
    )
}


window.onkeydown = function (event) {
    if (event.ctrlKey && event.altKey && event.code === 'Space') {
        let ignore = sendData(fetchUrlAndTitle);
    }
}
