from playwright.sync_api import sync_playwright

# work in progress, doesn't work yet
with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        args=[
            '--ignore-certificate-errors',
            '--ignore-ssl-errors',
            '--ignore-certificate-errors-spki-list',
            '--disable-web-security',
            '--allow-running-insecure-content'
        ]
    )
    
    context = browser.new_context(
        ignore_https_errors=True  # Ignore HTTPS certificate errors
    )
    
    page = context.new_page()
    page.goto("https://mail.google.com")

    # fill in the email
    page.get_by_role("textbox", name="Email or phone").click()
    page.get_by_role("textbox", name="Email or phone").fill("tylertam571@gmail.com")
    page.get_by_role("textbox", name="Email or phone").press("Enter")

    page.wait_for_timeout(1000)

    # # fill in the password
    # page.get_by_placeholder("Password").fill("Joshua123!")
    # page.get_by_role("button", name="Next").click()

    # # check if logged in
    # page.wait_for_timeout(1000)