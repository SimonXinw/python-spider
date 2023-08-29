

class ImageLoaded(object):
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        is_loaded = driver.execute_script(
            "return arguments[0].complete && typeof arguments[0].naturalWidth !== 'undefined' && arguments[0].naturalWidth > 0", element)
        if is_loaded:
            return element
        else:
            return False
