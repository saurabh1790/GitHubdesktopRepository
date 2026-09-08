class Portfolio:

    def __init__(self,page):
        self.page=page
        
        self.portfolio=page.locator('//a[text()="Portfolio"]')
        self.facebook=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/facebook.png"]')
        self.link=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/linkedin.png"]')
        self.insta=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/Insta.png"]')
        self.pin=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/pinterest.png"]')
        self.twitter=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/twitter.png"]')
        self.youtube=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/youtube.png"]')
        self.qoura=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/quora.png"]')

        #view more 
        self.icdhomework=page.locator('//a[@href="https://www.icshomework.in/"]')
        self.wingpharma=page.locator('//a[@href="https://www.wingspharma.com/"]')
        self.arena=page.locator('//a[@href="https://arenasonipat.com/"]')
        self.home=page.locator('//a[@href="https://home360stores.com/"]')
        self.clubmeeting=page.locator('//div[@class="cm-content"])[5]//a')
        self.cordcable=page.locator('//a[@href="https://cordscable.tranktechnologies.com/"]')


        

    def portfo(self):
        self.portfolio.click()
        
        self.page.wait_for_timeout(3000)
        self.page.wait_for_load_state(state="load")
        self.viewmore=[self.icdhomework,self.wingpharma,self.arena,self.home,self.clubmeeting,self.cordcable]
        for portlist_link in self.portlist:
            with self.page.context.expect_page() as new_page_info:
                portlist_link.click()
            new_tab = new_page_info.value
            new_tab.wait_for_load_state("load")
            new_tab.close()
        
    def viewmore(self):
        self.portfolio.click()
        self.page.locator('//p[text()="Follow Us"]').hover()
        self.page.wait_for_timeout(3000)
        self.page.wait_for_load_state(state="load")
        self.portlist=[self.facebook,self.link,self.insta,self.pin,self.twitter,self.youtube,self.qoura]
        for portlist_link in self.portlist:
            with self.page.context.expect_page() as new_page_info:
                portlist_link.click()
            new_tab = new_page_info.value
            new_tab.wait_for_load_state("load")
            new_tab.close()      
