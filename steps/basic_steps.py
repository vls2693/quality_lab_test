class BasicSteps(object):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_browser_step(self):
        self.browser.get(self.url)
        self.browser.maximize_window()
