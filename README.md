# account-generator
Creates accounts for Walmart, Bestbuy, Target, and Microsoft

If you want the script to run faster remove "options=chrome_options" from each of the functions drivers
should look like this:

  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 
The headless browser is just there to reduce resources but that's up to you.

Currently only the bestbuy generator works and the rest are close to being finished but I'm encountering a few issues which I'll try fix in my free time.


If you know how to fix some of the issues stated add me on discord ablog#5631

1. working around the PX button on walmart/finding the element to click
2. Finding element to click "account" then "create account" on target home page


notes: 
1. This only works with catchall emails
2. You have to verify everything even after you make the account through your gmail or mail
3. Download Python
4. Download Selenium
5. Download webdriver manager
