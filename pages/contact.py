class Contact:

    def __init__(self,page):
        self.page=page
        

        self.contact=page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')


        

        self.name=page.locator('(//input[@placeholder="Your Name"])[2]')
        self.email=page.locator('(//input[@placeholder="Your Mail"])[2]')
        self.sendotp=page.locator('(//button[text()="Send OTP"])[2]')
        

    def contactus(self):
        self.contact.click()
        self.name.fill("saurabh")
        self.email.fill("abc@gmail.com")
        self.page.once("dialog",lambda dialog: dialog.accept())
        self.sendotp.click()
