# UK Supermarket Basket Checker

A lightweight web app that lets you:

- Paste a shopping list
- Select UK supermarkets to compare
- See estimated basket totals and cheapest option
- Click one button to jump to the cheapest supermarket site with your list as a search query

## Fastest way to run (no git, no compile, no install)

1. Open the project folder.
2. Double-click `index.html`.
3. The app will open in your browser.

That is all — no build step and no terminal required.

## Optional: run with a tiny local server

If your browser blocks any file-mode behaviour, use:

```bash
python3 -m http.server 8000
```

Then open the browser and go to localhost on port 8000.

## Notes

- The app uses a built-in demo price catalogue plus fallback estimation for unknown items.
- Real-time supermarket pricing and full automated checkout require official retailer APIs and authenticated integrations.
