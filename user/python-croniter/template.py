pkgname = "python-croniter"
pkgver = "6.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-dateutil", "python-pytz"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Iteration support for datetime objects with cron like format"
license = "MIT"
url = "https://github.com/pallets-eco/croniter"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5b13012a70272e484f4644669ddae75e84a5597c41b44a5f628337e7c6acf329"


def post_install(self):
    self.install_license("LICENSE")
