from scraper import Twitter_scraper


login_username = "taskinccan"
password = "ufxlbM5*tZQn"
twitter_ai = Twitter_scraper()
twitter_ai.start_driver()
twitter_ai.driver.get("https://www.twitter.com/login")

twitter_ai.login(login_username, password)






