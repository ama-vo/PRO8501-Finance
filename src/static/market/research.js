
const API_URL = document.getElementById("research-page").dataset.apiUrl;

const form = document.getElementById("stock-form");
const symbolInput = document.getElementById("symbol");
const periodButtons = document.querySelectorAll("#periods button");
const errorBox = document.getElementById("stock-error");

const titleEl = document.getElementById("stock-symbol");
const priceEl = document.getElementById("stock-price");
const variationEl = document.getElementById("stock-variation");

const logoEl = document.getElementById("stock-logo");
const logoFallbackEl = document.getElementById("stock-logo-fallback");

const REFRESH_INTERVAL = 60 * 1000;

let chart = null;
let currentPeriod = "7d";
let requestId = 0;
let displayedSymbol = null;

const COMPANY_DOMAINS = {
    "AAPL": "apple.com",
    "MSFT": "microsoft.com",
    "GOOGL": "google.com",
    "GOOG": "google.com",
    "AMZN": "amazon.com",
    "META": "meta.com",
    "NVDA": "nvidia.com",
    "TSLA": "tesla.com",
    "NFLX": "netflix.com",
    "OR.PA": "loreal.com",
    "MC.PA": "lvmh.com",
    "AIR.PA": "airbus.com",
    "TTE.PA": "totalenergies.com",
    "SAN.PA": "sanofi.com",
    "BNP.PA": "group.bnpparibas",
    "SU.PA": "se.com",
    "RMS.PA": "hermes.com",
    "CS.PA": "axa.com",
    "V": "visa.com",
    "MA": "mastercard.com",
    "KO": "coca-colacompany.com",
    "PEP": "pepsico.com",
    "DIS": "thewaltdisneycompany.com",
    "IBM": "ibm.com",
    "INTC": "intel.com",
    "AMD": "amd.com",
    "ADBE": "adobe.com",
    "CRM": "salesforce.com",
    "PYPL": "paypal.com"
};


// Affichage du logo
function updateCompanyLogo(symbol) {

    const normalizedSymbol = symbol.trim().toUpperCase();
    const domain = COMPANY_DOMAINS[normalizedSymbol];

    logoEl.classList.add("d-none");
    logoEl.removeAttribute("src");

    logoFallbackEl.textContent = normalizedSymbol.slice(0, 2) || "?";
    logoFallbackEl.classList.remove("d-none");

    if (!domain) return;

    logoEl.onload = () => {
        logoEl.classList.remove("d-none");
        logoFallbackEl.classList.add("d-none");
    };

    logoEl.onerror = () => {
        logoEl.classList.add("d-none");
        logoFallbackEl.classList.remove("d-none");
    };

    logoEl.src = `https://logos.hunter.io/${encodeURIComponent(domain)}`;
    logoEl.alt = `Logo de ${normalizedSymbol}`;
}


// Configuration Chart.js
Chart.defaults.color = "#adb5bd";
Chart.defaults.borderColor = "rgba(255, 255, 255, 0.08)";


function showError(message) {
    errorBox.textContent = message;
    errorBox.classList.toggle("d-none", !message);
}


// Récupération des données
async function loadHistory() {

    const symbol = symbolInput.value.trim();

    if (!symbol) return;

    const myRequest = ++requestId;

    showError("");

    try {

        const url = API_URL.replace(
            "SYMBOL",
            encodeURIComponent(symbol)
        );

        const response = await fetch(
            `${url}?period=${currentPeriod}`
        );

        let data = {};

        try {
            data = await response.json();
        } catch {
            // Réponse non JSON
        }

        if (myRequest !== requestId) return;

        if (!response.ok) {
            throw new Error(
                data.error || "Impossible de récupérer les données."
            );
        }

        drawChart(data);

    } catch (error) {

        if (myRequest !== requestId) return;

        showError(
            error.message || "Impossible de récupérer les données."
        );
    }
}


// Mise à jour du graphique
function drawChart(data) {

    if (!data.values || data.values.length === 0) {
        showError("Aucune donnée disponible pour ce ticker.");
        return;
    }

    const first = data.values[0];
    const last = data.values[data.values.length - 1];

    const change = first ? ((last - first) / first) * 100 : 0;

    const isUp = change >= 0;
    const color = isUp ? "#22c55e" : "#ef4444";

    // Informations de l'entreprise
    titleEl.textContent = data.symbol;

    if (displayedSymbol !== data.symbol) {
        updateCompanyLogo(data.symbol);
        displayedSymbol = data.symbol;
    }

    // Prix
    priceEl.textContent = last.toLocaleString("fr-FR", {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    });

    variationEl.textContent =
        `${isUp ? "+" : ""}${change.toFixed(2)} %`;

    variationEl.className =
        "fs-6 " + (isUp ? "text-success" : "text-danger");


    if (!chart) {

        chart = new Chart(
            document.getElementById("stock-chart"),
            {
                type: "line",

                data: {
                    labels: data.labels,

                    datasets: [{
                        label: data.symbol,
                        data: data.values,
                        borderColor: color,
                        backgroundColor: color + "22",
                        borderWidth: 2,
                        pointRadius: 0,
                        pointHoverRadius: 4,
                        tension: 0.2,
                        fill: true
                    }]
                },

                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    animation: false,

                    interaction: {
                        mode: "index",
                        intersect: false
                    },

                    plugins: {
                        legend: {
                            display: false
                        }
                    },

                    scales: {
                        x: {
                            ticks: {
                                maxTicksLimit: 8
                            }
                        }
                    }
                }
            }
        );

        return;
    }


    chart.data.labels = data.labels;

    chart.data.datasets[0].label = data.symbol;
    chart.data.datasets[0].data = data.values;

    chart.data.datasets[0].borderColor = color;
    chart.data.datasets[0].backgroundColor = color + "22";

    chart.update("none");
}


form.addEventListener("submit", (event) => {

    event.preventDefault();

    loadHistory();

});


periodButtons.forEach((button) => {

    button.addEventListener("click", () => {

        currentPeriod = button.dataset.period;

        periodButtons.forEach((b) => {
            b.classList.toggle("active", b === button);
        });

        loadHistory();

    });

});


loadHistory();


setInterval(() => {

    if (currentPeriod === "7d" && !document.hidden) {
        loadHistory();
    }

}, REFRESH_INTERVAL);

