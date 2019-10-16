from .basic_steps import BasicSteps
import time


class MainPageSteps(BasicSteps):
    def authorization_step(self, user_name, user_password):
        self.browser.find_element_by_id("mailbox:login").send_keys(user_name)
        self.browser.find_element_by_id("mailbox:submit").click()
        time.sleep(3)
        self.browser.find_element_by_id("mailbox:password").send_keys(user_password)
        self.browser.find_element_by_css_selector("input[value='Ввести пароль']").click()
        time.sleep(2)

    def send_email_step(self, addressee, text):
    	self.browser.find_element_by_partial_link_text("Написать письмо").click()
    	self.browser.find_element_by_css_selector("textarea[data-original-name='To']").send_keys(addressee)
    	time.sleep(2)
    	iframe_name = self.browser.find_element_by_css_selector("iframe[title='{#aria.rich_text_area}']")
    	self.browser.switch_to_frame(iframe_name)
    	time.sleep(5)
    	self.browser.find_element_by_id("tinymce").click()
    	self.browser.find_element_by_id("tinymce").send_keys(text)
    	time.sleep(5)
    	self.browser.switch_to.parent_frame()
    	self.browser.find_element_by_css_selector("div[data-name='send']").click()
    	time.sleep(5)
