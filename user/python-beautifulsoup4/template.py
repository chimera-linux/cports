pkgname = "python-beautifulsoup4"
pkgver = "4.13.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
depends = ["python-soupsieve"]
checkdepends = ["python-pytest"]
pkgdesc = "Screen-scraping library"
license = "MIT"
url = "https://www.crummy.com/software/BeautifulSoup"
source = f"$(PYPI_SITE)/b/beautifulsoup4/beautifulsoup4-{pkgver}.tar.gz"
sha256 = "dbb3c4e1ceae6aefebdaf2423247260cd062430a410e38c66f2baa50a8437195"


def post_install(self):
    self.install_license("LICENSE")
