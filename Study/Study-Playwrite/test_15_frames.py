from playwright.sync_api import sync_playwright

def test_iframe_and_nested():
    with sync_playwright() as p:
        page = p.chromium.launch(headless=True).new_page()
        page.goto("https://the-internet.herokuapp.com/frames")
        page.click("text=iFrame")
        editor = page.frame_locator("iframe#mce_0_ifr").locator("body#tinymce")
        editor.fill("Hello Frames!")
        assert "Hello Frames!" in editor.text_content()
