import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException

POLL_FREQUENCY = 0.5
IGNORED_EXCEPTIONS = (NoSuchElementException,)


class WebDriverWaitCustom:
    def __init__(self, driver, timeout, poll_frequency=POLL_FREQUENCY, ignored_exceptions=None):
        self._driver = driver
        self._timeout = float(timeout)
        self._poll = poll_frequency or POLL_FREQUENCY
        self._ignored_exceptions = tuple(ignored_exceptions) if ignored_exceptions else IGNORED_EXCEPTIONS

    def until(self, method, message=""):
        end_time = time.monotonic() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions:
                pass
            if time.monotonic() > end_time:
                break
            time.sleep(self._poll)
        raise TimeoutException(message)
