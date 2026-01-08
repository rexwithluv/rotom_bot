from playwright.async_api import async_playwright


async def get_iphone_stock() -> str:
    url = "https://www.mediamarkt.es/es/brand/apple/iphone/iphone-15-pro?brand=APPLE&refurbished_new_array=No"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080},
        )

        page = await context.new_page()

        try:
            await page.goto(url, timeout=120000)

            selector = 'span[class="sc-94eb08bc-0 AKpzk"]'

            await page.wait_for_selector(selector, timeout=60000)

            text_count = await page.inner_text(selector)

            await browser.close()
            return f"Número de artículos: {text_count}\n\nURL: {url}"

        except Exception as e:
            await browser.close()
            return f"Error obteniendo los datos de mediamarkt: {str(e)}"
