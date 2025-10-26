from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Set up efficient popup monitoring
    def handle_popup():
        try:
            page.get_by_role("link", name="close dialog").click()
        except:
            pass  # No popup found, continue

    # go to the page
    page.goto("https://www.cnn.com/markets/stocks/COF")

    priceWhenAdded = 212.58
    monthlyAspp = 1511.54
    monthlyAsppPlusContributions = monthlyAspp * 1.15
    stocksOwned = monthlyAsppPlusContributions / priceWhenAdded
    page.get_by_role("link", name="Agree").click()

    # Target the price class
    price_element = page.locator(".price-1zj6yB")
    currentPrice = (float(price_element.inner_text()))
    print("CURRENT PRICE IS " + str(currentPrice))

    netProfitOrLoss = (currentPrice * stocksOwned) - monthlyAsppPlusContributions
    profitOrLoss = ""
    if netProfitOrLoss >= 0:
        profitOrLoss = "PROFIT"
    else:
        profitOrLoss = "LOSS"
    print("NET " + profitOrLoss + " IS " + str(round(netProfitOrLoss, 2)))
    
    browser.close()