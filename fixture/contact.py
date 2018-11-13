

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text('add new').click()
        # fill contact firm
        wd.find_element_by_name('lastname').click()
        wd.find_element_by_name('lastname').clear()
        wd.find_element_by_name('lastname').send_keys(contact.last_name)
        wd.find_element_by_name('firstname').click()
        wd.find_element_by_name('firstname').clear()
        wd.find_element_by_name('firstname').send_keys(contact.first_name)
        wd.find_element_by_name('address').click()
        wd.find_element_by_name('address').clear()
        wd.find_element_by_name('address').send_keys(contact.address)
        wd.find_element_by_name('email').click()
        wd.find_element_by_name('email').clear()
        wd.find_element_by_name('email').send_keys(contact.email)
        wd.find_element_by_name('mobile').click()
        wd.find_element_by_name('mobile').clear()
        wd.find_element_by_name('mobile').send_keys(contact.phone)
        # submit group creation
        wd.find_element_by_name('submit').click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name('selected[]').click()
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text('home').click()
