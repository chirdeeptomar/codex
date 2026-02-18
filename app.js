const supermarkets = [
  {
    id: "tesco",
    name: "Tesco",
    searchBaseUrl: "https://www.tesco.com/groceries/en-GB/search?query=",
  },
  {
    id: "sainsburys",
    name: "Sainsbury's",
    searchBaseUrl: "https://www.sainsburys.co.uk/gol-ui/SearchResults/",
  },
  {
    id: "asda",
    name: "Asda",
    searchBaseUrl: "https://groceries.asda.com/search/",
  },
  {
    id: "morrisons",
    name: "Morrisons",
    searchBaseUrl: "https://groceries.morrisons.com/search?entry=",
  },
  {
    id: "aldi",
    name: "Aldi",
    searchBaseUrl: "https://groceries.aldi.co.uk/en-GB/search?text=",
  },
];

const priceCatalog = {
  milk: { tesco: 1.55, sainsburys: 1.6, asda: 1.48, morrisons: 1.52, aldi: 1.4 },
  bread: { tesco: 1.2, sainsburys: 1.25, asda: 1.1, morrisons: 1.22, aldi: 1.05 },
  eggs: { tesco: 2.45, sainsburys: 2.5, asda: 2.35, morrisons: 2.4, aldi: 2.2 },
  bananas: { tesco: 1.18, sainsburys: 1.2, asda: 1.14, morrisons: 1.16, aldi: 1.1 },
  apples: { tesco: 1.6, sainsburys: 1.64, asda: 1.55, morrisons: 1.58, aldi: 1.45 },
  chicken: { tesco: 4.95, sainsburys: 5.1, asda: 4.85, morrisons: 4.9, aldi: 4.5 },
  pasta: { tesco: 1, sainsburys: 1.05, asda: 0.95, morrisons: 0.98, aldi: 0.89 },
  rice: { tesco: 2.5, sainsburys: 2.6, asda: 2.45, morrisons: 2.48, aldi: 2.2 },
  tomatoes: { tesco: 1.4, sainsburys: 1.46, asda: 1.35, morrisons: 1.39, aldi: 1.22 },
  cheese: { tesco: 2.95, sainsburys: 3.05, asda: 2.9, morrisons: 2.94, aldi: 2.6 },
};

const fallbackMultiplierBySupermarket = {
  tesco: 1,
  sainsburys: 1.03,
  asda: 0.97,
  morrisons: 0.99,
  aldi: 0.9,
};

const supermarketOptions = document.getElementById("supermarketOptions");
const compareButton = document.getElementById("compareButton");
const shoppingListElement = document.getElementById("shoppingList");
const resultsSection = document.getElementById("resultsSection");
const summary = document.getElementById("summary");
const tableWrap = document.getElementById("tableWrap");
const orderButton = document.getElementById("orderButton");

let latestResult = null;

function gbp(value) {
  return new Intl.NumberFormat("en-GB", {
    style: "currency",
    currency: "GBP",
  }).format(value);
}

function seedSupermarketOptions() {
  supermarkets.forEach((store) => {
    const wrapper = document.createElement("label");
    wrapper.className = "checkbox-item";

    const input = document.createElement("input");
    input.type = "checkbox";
    input.value = store.id;
    input.checked = true;

    const text = document.createElement("span");
    text.textContent = store.name;

    wrapper.append(input, text);
    supermarketOptions.appendChild(wrapper);
  });
}

function parseShoppingList() {
  return shoppingListElement.value
    .split("\n")
    .map((item) => item.trim().toLowerCase())
    .filter(Boolean);
}

function selectedSupermarkets() {
  const checked = supermarketOptions.querySelectorAll('input[type="checkbox"]:checked');
  return Array.from(checked).map((option) => option.value);
}

function estimateUnknownItemPrice(item, supermarketId) {
  const baseline = Math.max(0.8, item.length * 0.27);
  return baseline * fallbackMultiplierBySupermarket[supermarketId];
}

function calculateTotal(itemList, supermarketId) {
  return itemList.reduce((sum, item) => {
    const found = priceCatalog[item]?.[supermarketId];
    const price = found ?? estimateUnknownItemPrice(item, supermarketId);
    return sum + price;
  }, 0);
}

function buildTable(rows, cheapestId) {
  const table = document.createElement("table");
  table.innerHTML = `
    <thead>
      <tr>
        <th>Supermarket</th>
        <th>Estimated total</th>
      </tr>
    </thead>
    <tbody>
      ${rows
        .map(
          (row) => `
          <tr class="${row.id === cheapestId ? "cheapest" : ""}">
            <td>${row.name}</td>
            <td>${gbp(row.total)}</td>
          </tr>
        `
        )
        .join("")}
    </tbody>
  `;

  tableWrap.innerHTML = "";
  tableWrap.appendChild(table);
}

function comparePrices() {
  const items = parseShoppingList();
  const stores = selectedSupermarkets();

  if (!items.length) {
    alert("Please add at least one shopping list item.");
    return;
  }

  if (!stores.length) {
    alert("Please select at least one supermarket.");
    return;
  }

  const rows = supermarkets
    .filter((store) => stores.includes(store.id))
    .map((store) => ({
      ...store,
      total: Number(calculateTotal(items, store.id).toFixed(2)),
    }))
    .sort((a, b) => a.total - b.total);

  const cheapest = rows[0];
  latestResult = { items, cheapest };

  summary.innerHTML = `
    <p><strong>Cheapest option:</strong> ${cheapest.name}</p>
    <p><strong>Basket total:</strong> ${gbp(cheapest.total)}</p>
  `;

  buildTable(rows, cheapest.id);
  resultsSection.classList.remove("hidden");
  orderButton.classList.remove("hidden");
}

function goToCheapestOrderPage() {
  if (!latestResult) {
    return;
  }

  const { cheapest, items } = latestResult;
  const listAsQuery = encodeURIComponent(items.join(" "));
  const url = `${cheapest.searchBaseUrl}${listAsQuery}`;
  window.open(url, "_blank", "noopener");
}

seedSupermarketOptions();
compareButton.addEventListener("click", comparePrices);
orderButton.addEventListener("click", goToCheapestOrderPage);
