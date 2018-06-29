from selenium import webdriver
from win10toast import ToastNotifier


# Enter Instagram username on 0th element, and status on the 1st element
girls = [['instagram username', 'current instagram status']
		]

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(chrome_options = options)
toaster = ToastNotifier()

repeat = True
while(repeat):
	for girl in girls:
		driver.get('https://instagram.com/' + girl[0])
		if('Page Not Found' not in driver.title):
			html_tag = driver.find_elements_by_class_name('-vDIg')
			if(girl[1] not in html_tag[0].text):
				toaster.show_toast('Gebetan Notifier', girl[0] + ' status has changed! go to her profile!')
				repeat = False
			print('Masih')
		else:
			toaster.show_toast('Gebetan Notifier', girl[0] + ' is not found. Maybe she changed her username? :/ ')
			repeat = False