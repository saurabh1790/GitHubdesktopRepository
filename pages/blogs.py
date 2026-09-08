class Blog:

    def __init__(self,page):
        self.page=page
        self.blog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')
        #allblog locator
        self.appdev=page.locator('(//a[text()="App Development"])[1]')
        self.webdev=page.locator('(//a[text()="Web Development"])[1]')
        self.softdev=page.locator('(//a[text()="Software Development"])[1]')
        self.dmarket=page.locator('(//a[text()="Digital Marketing"])[1]')
        self.emark=page.locator('(//a[text()="Email Marketing"])[1]')
        self.art=page.locator('(//a[text()="Artificial Intelligence"])[2]')
        self.uiux=page.locator('(//a[text()="UI UX Design"])[1]')

        self.blogg=[self.appdev,self.webdev,self.softdev,self.dmarket,self.emark,self.art,self.uiux]

    def fblo(self):
            for i in self.blogg:
                self.blog.click()
                i.click()
                self.page.wait_for_load_state("load")
                self.page.wait_for_timeout(2000)
                self.page.go_back()
                self.page.wait_for_load_state("load")


