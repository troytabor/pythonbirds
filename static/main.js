function calculateTotalInfections() {
    fetch('/calculate-total-infections')
        .then(response => response.json())
        .then(data => {
            let formattedInfections = (+data.total_infections).toLocaleString(); // Formatting the number
            document.getElementById('totalInfections').textContent = `Total bird flu infections: ${formattedInfections}`;
        })
        .catch(error => console.error('Error:', error));
}

function calculateByLocation(state) {
    if (!state) return; // Skip if the state is not selected
    fetch(`/infections-by-location?state=${state}`)
        .then(response => response.json())
        .then(data => {
            let formattedInfectionsByLocation = (+data.infections_by_location).toLocaleString(); // Formatting the number
            document.getElementById('infectionsByLocation').textContent = `Total infections by location (${state}): ${formattedInfectionsByLocation}`;
        })
        .catch(error => console.error('Error:', error));
}

function calculateByTime(year) {
    if (!year) return; // Skip if the year is not selected
    fetch(`/infections-by-time?year=${year}`)
        .then(response => response.json())
        .then(data => {
            let formattedInfectionsByTime = (+data.infections_by_time).toLocaleString(); // Formatting the number
            document.getElementById('infectionsByTime').textContent = `Total infections by time (Year ${year}): ${formattedInfectionsByTime}`;
        })
        .catch(error => console.error('Error:', error));
}

function loadContent(url, targetDivId) {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(html => {
            document.getElementById(targetDivId).innerHTML = html;
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation: ', error);
            document.getElementById(targetDivId).innerHTML = 'Failed to load content.';
        });
}

function loadIntoIframe(url) {
    document.getElementById('contentFrame').src = url;
}
