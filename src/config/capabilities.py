from appium.options.android import UiAutomator2Options

def get_android_options():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"

    options.app_package = "com.crisoft.devsuite"
    options.app_activity = ".MainActivity"

    options.no_reset = False
    options.full_reset = False
    options.app_wait_activity = "*"
    options.app_wait_duration = 30000
    options.new_command_timeout = 300

    options.auto_grant_permissions = True

    return options
