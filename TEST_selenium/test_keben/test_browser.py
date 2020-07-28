from test_keben.base import Base


class Test_browser(Base):
    def test_browser(self):
        self.driver.get('http://home-testing-studio.com')
