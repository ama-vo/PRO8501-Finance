// URL de l'API Django
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

    let chart = null;
    let currentPeriod = "1y";
    let requestId = 0;

    // Correspondance entre ticker et domaine de l'entreprise
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

    // Afficher le logo de l'entreprise sélectionnée
    function updateCompanyLogo(symbol) {

        const normalizedSymbol = symbol.trim().toUpperCase();
        const domain = COMPANY_DOMAINS[normalizedSymbol];

        // Réinitialisation
        logoEl.classList.add("d-none");
        logoEl.removeAttribute("src");

        logoFallbackEl.textContent = normalizedSymbol.slice(0, 2) || "?";
        logoFallbackEl.classList.remove("d-none");

        // Aucun domaine connu
        if (!domain) return;

        // Gestion du chargement
        logoEl.onload = () => {
            logoEl.classList.remove("d-none");
            logoFallbackEl.classList.add("d-none");
        };

        logoEl.onerror = () => {
            logoEl.classList.add("d-none");
            logoFallbackEl.classList.remove("d-none");
        };

        // API Logo Hunter
        logoEl.src = `https://logos.hunter.io/${encodeURIComponent(domain)}`;
        logoEl.alt = `Logo de ${normalizedSymbol}`;
    }

    // Couleurs du graphique
    Chart.defaults.color = "#adb5bd";
    Chart.defaults.borderColor = "rgba(255, 255, 255, 0.08)";

    function showError(message) {
        errorBox.textContent = message;
        errorBox.classList.toggle("d-none", !message);
    }

    // Récupération des données boursières
    async function loadHistory() {

        const symbol = symbolInput.value.trim();
        if (!symbol) return;

        const myRequest = ++requestId;
        showError("");

        try {
            const url = API_URL.replace("SYMBOL", encodeURIComponent(symbol));
            const response = await fetch(`${url}?period=${currentPeriod}`);

            let data = {};
            try {
                data = await response.json();
            } catch {
                // Réponse non JSON
            }

            if (myRequest !== requestId) return;

            if (!response.ok) {
                throw new Error(data.error || "Impossible de récupérer les données.");
            }

            drawChart(data);

        } catch (error) {
            if (myRequest !== requestId) return;
            showError(error.message || "Impossible de récupérer les données.");
        }
    }

    // Construction du graphique
    function drawChart(data) {

        const first = data.values[0];
        const last = data.values[data.values.length - 1];

        const change = ((last - first) / first) * 100;
        const isUp = change >= 0;
        const color = isUp ? "#22c55e" : "#ef4444";

        // Mise à jour de l'en-tête
        titleEl.textContent = data.symbol;

        // Mise à jour du logo
        updateCompanyLogo(data.symbol);

        priceEl.textContent = last.toLocaleString("fr-FR", {
            minimumFractionDigits: 2
        });

        variationEl.textContent =
            `${isUp ? "+" : ""}${change.toFixed(2)} %`;

        variationEl.className =
            "fs-6 " + (isUp ? "text-success" : "text-danger");

        // Destruction de l'ancien graphique
        if (chart) chart.destroy();

        chart = new Chart(document.getElementById("stock-chart"), {
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
                    fill: true,
                }],
            },

            options: {
                responsive: true,
                maintainAspectRatio: false,

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
                    },
                },
            },
        });
    }

    // Soumission du formulaire
    form.addEventListener("submit", (event) => {
        event.preventDefault();
        loadHistory();
    });

    // Changement de période
    periodButtons.forEach((button) => {

        button.addEventListener("click", () => {

            currentPeriod = button.dataset.period;

            periodButtons.forEach((b) => {
                b.classList.toggle("active", b === button);
            });

            loadHistory();
        });
    });

    // Premier affichage
    loadHistory();
