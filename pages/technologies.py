class Technologies:

    def __init__(self,page):
        self.page=page

        #technologies locator 
        self.technologies=page.locator('(//a[text()="Technologies"])[1]')

        #tech
        self.ecomm=page.locator('//a//strong[text()="eCommerce Development"]')
        self.mad=page.locator('(//a[@href="https://www.tranktechnologies.com/mobile-app-development-company"])[1]')

        #ecommerce
        self.magdev=page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.codeig=page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.big=page.locator('(//a[text()="Big Commerce"])[1]')
        self.cscart=page.locator('(//a[text()="CS-Cart Development"])[1]')
        self.nopecom=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.ldev=page.locator('(//a[text()="Laravel Development"])[1]')
        self.opencart=page.locator('(//a[text()="Opencart Development"])[1]')
        self.openpress=page.locator('(//a[text()="WordPress Development"])[1]')
        self.wordpress=page.locator('(//a[text()="WordPress Development"])[1]')
        self.shopify=page.locator('(//a[text()="Shopify Development"])[1]')
        self.nodejs=page.locator('(//a[text()="Node JS Development"])[1]')
        self.wocom=page.locator('(//a[text()="Woo Commerce"])[1]')
        self.prestadev=page.locator('(//a[text()="Prestashop Development"])[1]')
        self.drupal=page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
        self.wixdev=page.locator('(//a[text()="Wix Development"])[1]')
        self.joomla=page.locator('(//a[text()="Joomla Development"])[1]')
        self.rectjsdev=page.locator('(//a[text()="React JS Development"])[1]')
        self.express=page.locator('(//a[text()="Express JS Development"])[1]')

        self.ecom=[self.magdev,self.codeig,self.big,self.cscart,self.nopecom,self.ldev,self.opencart,self.openpress,self.wordpress,self.shopify,self.nodejs,self.wocom,self.prestadev,self.drupal,self.wixdev,self.joomla,self.rectjsdev,self.express]
        #mobiledev
        self.reactnative=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.xam=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.flut=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.swift=page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.enter=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.kotlin=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.idev=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.appoint=page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
        #list of mobiledev
        self.mobile=[self.reactnative,self.xam,self.flut,self.swift,self.enter,self.kotlin,self.idev,self.appoint]


    def techNav(self):

        for i in self.ecom:
            # ensure the top-level menu is visible, hover or click as fallback
            try:
                self.technologies.wait_for(state='visible', timeout=5000)
                self.technologies.hover()
            except Exception:
                try:
                    self.technologies.click(timeout=3000)
                except Exception:
                    pass

            # ensure the eCommerce submenu is visible
            try:
                self.ecomm.wait_for(state='visible', timeout=5000)
                self.ecomm.hover()
            except Exception:
                try:
                    self.ecomm.click(timeout=3000)
                except Exception:
                    pass

            # try to click the target item, force if it's intermittently obscured
            try:
                i.wait_for(state='visible', timeout=5000)
                i.click(timeout=5000)
            except Exception:
                try:
                    i.click(force=True)
                except Exception:
                    # give a short pause and continue to next
                    self.page.wait_for_timeout(1000)
                    continue

            self.page.wait_for_load_state("load")
            self.page.wait_for_timeout(2000)
            self.page.go_back()


    def techmobile(self):    
        for i in self.mobile:
                try:
                    self.technologies.wait_for(state='visible', timeout=5000)
                    self.technologies.hover()
                except Exception:
                    try:
                        self.technologies.click(timeout=3000)
                    except Exception:
                        pass

                try:
                    self.mad.wait_for(state='visible', timeout=5000)
                    self.mad.hover()
                except Exception:
                    try:
                        self.mad.click(timeout=3000)
                    except Exception:
                        pass

                self.page.wait_for_timeout(1000)

                try:
                    i.wait_for(state='visible', timeout=5000)
                    i.click(timeout=5000)
                except Exception:
                    try:
                        i.click(force=True)
                    except Exception:
                        self.page.wait_for_timeout(1000)
                        continue

                self.page.wait_for_load_state("load")
                self.page.wait_for_timeout(2000)
                self.page.go_back()
