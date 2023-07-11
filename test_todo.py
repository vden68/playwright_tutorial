import os

from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_todo(page) -> None:
    page.goto("https://playwright-todomvc.antonzimaiev.repl.co/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")


def test_login(page):
    page.goto('https://exaltedplushadware.antonzimaiev.repl.co/?')
    page.locator("#exampleInputEmail1").fill("admin@example.com")

def test_login2(page):
    page.goto('https://exaltedplushadware.antonzimaiev.repl.co/?')
    page.locator("#exampleInputEmail1").type("admin@example.com")

def test_checkbox(page):
    page.goto('https://checks-radios.antonzimaiev.repl.co/')
    page.locator("text=Default checkbox").check()
    page.locator("text=Checked checkbox").check()
    page.locator("text=Default radio").check()
    page.locator("text=Default checked radio").check()
    page.locator("text=Checked switch checkbox input").check()

def test_select(page):
    page.goto('https://select.antonzimaiev.repl.co/')
    page.select_option('#floatingSelect', value="3")
    page.select_option('#floatingSelect', index=1)
    page.select_option('#floatingSelect', label="Нашел и завел bug")

def test_select2(page):
    page.goto('https://select.antonzimaiev.repl.co/')
    page.select_option('#floatingSelect', value="3")
    page.select_option('#floatingSelect', index=1)
    page.select_option('#floatingSelect', label="Нашел и завел bug")

def test_select_multiple(page):
    page.goto('https://select.antonzimaiev.repl.co/')
    page.select_option('#skills', value=["playwright", "python"])

def test_drag_and_drop(page):
    page.goto('https://draganddrop.antonzimaiev.repl.co/')
    page.drag_and_drop("#drag", "#drop")

def test_dialogs(page):
    page.goto("https://dialog.antonzimaiev.repl.co/")
    page.get_by_text("Диалог Alert").click()
    page.get_by_text("Диалог Confirmation").click()
    page.get_by_text("Диалог Prompt").click()

def test_dialogs2(page):
    page.goto("https://dialog.antonzimaiev.repl.co/")
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_text("Диалог Confirmation").click()

def test_select_multiple(page):
    page.goto('https://upload.antonzimaiev.repl.co/')
    page.set_input_files("#formFile", "hello.txt")
    page.locator("#file-submit").click()

def test_select_multiple2(page):
    page.goto('https://upload.antonzimaiev.repl.co/')
    page.on("filechooser", lambda file_chooser: file_chooser.set_files("hello.txt"))
    page.locator("#formFile").click()

def test_download(page):

    page.goto("https://demoqa.com/upload-download")

    with page.expect_download() as download_info:
        page.locator("a:has-text(\"Download\")").click()

    download = download_info.value
    file_name = download.suggested_filename
    destination_folder_path = "./data/"
    download.save_as(os.path.join(destination_folder_path, file_name))


def test_new_tab(page):
    page.goto("https://tabs.antonzimaiev.repl.co/")
    with page.context.expect_page() as tab:
        page.get_by_text("Переход к Dashboard").click()

    new_tab = tab.value
    page.pause()
    assert new_tab.url == "https://tabs.antonzimaiev.repl.co/dashboard/index.html?"
    sign_out = new_tab.locator('.nav-link', has_text='Sign out')
    assert sign_out.is_visible()

def test_todo(page):
    page.goto('https://demo.playwright.dev/todomvc/#/')
    expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")
    input_field = page.get_by_placeholder('What needs to be done?')
    expect(input_field).to_be_empty()
    input_field.fill("Закончить курс по playwright")
    input_field.press('Enter')
    input_field.fill("Добавить в резюме, что умею автоматизировать")
    input_field.press('Enter')
    todo_item = page.get_by_test_id('todo-item')
    expect(todo_item).to_have_count(2)
    todo_item.get_by_role('checkbox').nth(0).click()
    expect(todo_item.nth(0)).to_have_class('completed')

def test_listen_network(page):
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))
    page.goto('https://osinit.ru/')

def test_inventory(page):
    response = page.request.get('https://petstore.swagger.io/v2/store/inventory')
    print(response.status)
    print(response.json())