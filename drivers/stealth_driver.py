from fake_useragent import UserAgent

def create_driver():
    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f"user-agent={UserAgent().random}")
    options.add_argument("--start-maximized")
    
    driver = uc.Chrome(options=options)
    return driver
