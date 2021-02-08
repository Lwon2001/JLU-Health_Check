import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# 隐式等待10s
driver.implicitly_wait(10)

# 服务大厅地址
url = "https://ehall.jlu.edu.cn/jlu_portal/index"
driver.get(url)

# 登录
driver.find_element_by_id("username").send_keys("用户名")
driver.find_element_by_id("password").send_keys("密码")
button1 = driver.find_element_by_id("login-submit")
button1.click()

# 登录完毕，点击”本科生每日健康打卡“按钮
driver.find_elements_by_class_name("center")[10].click()

# 获得当前页面句柄
sreach_windows = driver.current_window_handle

# 获得当前所有打开的窗口的句柄
all_handles = driver.window_handles

# 点击在线办理
driver.find_element_by_link_text("在线办理").click()

# 切换网页(若浏览器未自动切换到新弹出网页)
for handle in all_handles:
    if handle != sreach_windows:
        driver.switch_to.window(handle)

# 填写地址
province = driver.find_element_by_xpath('/html/body/div[4]/form/div/div[3]/div[2]/div[1]/div[1]/div['
                                        '2]/table/tbody/tr[2]/td/div/table/tbody/tr[11]/td[2]/div/div/div/div/input')
city = driver.find_element_by_xpath('/html/body/div[4]/form/div/div[3]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr['
                                    '2]/td/div/table/tbody/tr[11]/td[4]/div/div/div/div/input')
county = driver.find_element_by_xpath('/html/body/div[4]/form/div/div[3]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr['
                                      '2]/td/div/table/tbody/tr[11]/td[6]/div/div/div/div/input')
street = driver.find_element_by_xpath('/html/body/div[4]/form/div/div[3]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr['
                                      '2]/td/div/table/tbody/tr[11]/td[8]/div/input')
province.send_keys(Keys.CONTROL, 'a')
province.send_keys("省")
province.send_keys(Keys.ENTER)
city.send_keys(Keys.CONTROL, 'a')
city.send_keys("市")
city.send_keys(Keys.ENTER)
county.send_keys(Keys.CONTROL, 'a')
county.send_keys("区")
county.send_keys(Keys.ENTER)
street.send_keys(Keys.CONTROL, 'a')
street.send_keys("详细地址")
street.send_keys(Keys.ENTER)

# ‘14天内是否前往中高风险地区’选否
risk_n = driver.find_element_by_id('V1_CTRL43')
risk_n.is_selected()

# 体温状态选择正常
temp_status_y = driver.find_element_by_id('V1_CTRL28')
temp_status_y.is_selected()

# 点击提交按钮
submit = driver.find_element_by_link_text('提交')
submit.click()
time.sleep(1)

# 点击好
driver.find_element_by_xpath("//*[contains(text(),'好')]/../button ").click()




