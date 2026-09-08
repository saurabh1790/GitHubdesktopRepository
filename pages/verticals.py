class V:
    #if we define anything under constructor it will be called at priority level 
    #define locators and method 
    def __init__(self,page): 
        self.page=page
        #put all the vertical locators
        self.verticals=page.locator('(//a[text()="Verticals"])[1]')
        #vertical menu locators
        self.trading=page.locator('//strong[text()="Trading1"]')
        self.retail=page.locator('//strong[text()="Retail and Ecommerce"]')
        self.healthcare=page.locator('//strong[text()="Healthcare"]')
        self.fintech=page.locator('//strong[text()="Fintech"]')
        self.customApp=page.locator('//strong[text()="Custom App"]')

        #trading locators
        self.stocktrading=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.papertrading=page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.cfdtraining=page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.tradingappdev=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.algotrading=page.locator('//a[text()="Algo Trading"]')
        self.customtrading=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.webportaltrading=page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')

        #declare list 
        self.tradinglist=[self.stocktrading,self.papertrading,self.cfdtraining,self.tradingappdev,self.algotrading,self.customtrading,self.webportaltrading]

        #retailandecommerce
        self.ecomwebsite=page.locator('(//a[text()="eCommerce Website Development"])[1]')
        self.ecomappdev=page.locator('(//a[text()="eCommerce App Development"])[1]')

        self.ecommerce=[self.ecomwebsite,self.ecomappdev]

    

        self.page.wait_for_load_state("load")
        self.page.wait_for_timeout(5000)

        #healthcare
        self.diet=page.locator('(//a[text()="Diet & Nutritions"])[1]')
        self.healthtrack=page.locator('(//a[text()="Health tracking App"])[1]')

        self.heal=[self.diet,self.healthtrack]

    

        #fintech
        self.possoft=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.crypto=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company-in-india"])[1]')

        self.fin=[self.possoft,self.crypto]

    

    #custom app
        self.dappdev=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.hrmdev=page.locator('(//a[text()="HRM Development"])[1]')
        self.trav=page.locator('(//a[text()="Travel"])[1]')
        self.dateapp=page.locator('(//a[text()="Dating App Development"])[1]')
        self.crmdev=page.locator('(//a[text()="CRM Development"])[1]')
        self.crmdevusa=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
        self.erpdev=page.locator('(//a[text()="ERP App Development"])[1]')
        self.learn=page.locator('(//a[text()="E-Learning"])[1]')
        self.realestate=page.locator('(//a[text()="Real Estate"])[1]')

        self.capp=[self.dappdev,self.hrmdev,self.trav,self.dateapp,self.crmdev,self.erpdev,self.learn,self.realestate]

    #define methods 
    def tradingNav(self):  #if we define method in class , pass arg as self - mandatory 
        for i in self.tradinglist:
            self.verticals.hover()
            self.trading.hover()
            self.page.wait_for_timeout(2000)
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()


    def retailandecommerce(self):
        for i in self.ecommerce:
                self.verticals.hover()
                self.retail.hover()
                self.page.wait_for_timeout(2000)
                i.click()
                self.page.wait_for_load_state("load")
                self.page.go_back()

    def vhealthcare(self):
        for i in self.heal:
                self.verticals.hover()
                self.healthcare.hover()
                self.page.wait_for_timeout(2000)
                i.click()
                self.page.wait_for_load_state("load")
                self.page.wait_for_timeout(2000)
                self.page.go_back()


    def fintechh(self):
         for i in self.fin:
            self.verticals.hover()
            self.fintech.hover()
            self.page.wait_for_timeout(2000)
            i.click()
            self.page.wait_for_load_state("load")
            self.page.wait_for_timeout(2000)
            self.page.go_back()

    def customapp(self):
         for i in self.capp:
                 self.verticals.hover()
                 self.customApp.hover()
                 self.page.wait_for_timeout(2000)
                 i.click()
                 self.page.wait_for_load_state("load")
                 self.page.wait_for_timeout(2000)
                 self.page.go_back()
#we will not call function here . We will call function in test folder
