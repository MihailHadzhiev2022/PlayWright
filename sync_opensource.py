from asyncio import wait_for

from playwright.sync_api import sync_playwright , expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    user_name = page.locator("//input[@name='username']")
    user_name.fill("Admin")

    password_field = page.locator("//input[@type='password']")
    password_field.fill("admin123")

    login_button = page.locator("//button[@type='submit']")
    login_button.click()


    dashboard = page.locator("//h6[contains(@class, 'oxd-text') and text()='Dashboard']")
    expect(dashboard).to_be_visible()

    # Verify that Search is working as expected
    search_button = page.locator("//input[@placeholder='Search']")
    search_button.fill('PIM')
    pim_locator = page.locator("//a[contains(@href, 'pim/viewPimModule')]//span[text()='PIM']")
    expect(pim_locator).to_be_visible()  #When we typed Pim, only Pim is visible
    leave_locator = page.locator("//a[contains(@href, 'leave/viewLeaveModule')]//span[text()='Leave']")
    expect(leave_locator).not_to_be_visible()

    #Delete Pim from Search, Menu is visible
    search_button.fill('')
    expect(pim_locator).to_be_visible()
    expect(leave_locator).to_be_visible()

    #Test Pim menu
    pim_locator.click()
    #located all list items:
    configuration = page.locator("//li[contains(@class, 'oxd-topbar-body-nav-tab')]//span[contains(text(), 'Configuration')]")
    employee_list = page.locator("//li[contains(@class,'oxd-topbar-body-nav-tab')]//a[contains(text(), 'Employee List')]")
    add_employee = page.locator("//li[contains(@class, 'oxd-topbar-body-nav-tab')]//a[contains(text(), 'Add Employee')]")
    reports = page.locator("//li[contains(@class,'oxd-topbar-body-nav-tab')]//a[contains(text(), 'Reports')]")

    expect(configuration).to_be_visible()
    expect(employee_list).to_be_visible()
    expect(add_employee).to_be_visible()
    expect(reports).to_be_visible()

    #When we click Configuration: Verify menu: Optional Fields, Custom Fields, Data import, Reporthing Methods, Termination

    configuration.click()
    optional_field = page.locator("//ul[contains(@class, 'oxd-dropdown-menu')]//a[contains(@class, 'oxd-topbar-body-nav-tab-link') and contains(text(), 'Optional Fields')]")
    expect(optional_field).to_be_visible()
    optional_field.click()
    show_deprecated_fields = page.locator("//h6[text()='Show Deprecated Fields']")
    expect(show_deprecated_fields).to_be_visible()























