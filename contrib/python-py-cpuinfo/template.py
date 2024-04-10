pkgname = "python-py-cpuinfo"
pkgver = "9.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Python module for getting CPU info"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/workhorsy/py-cpuinfo"
source = f"$(PYPI_SITE)/p/py-cpuinfo/py-cpuinfo-{pkgver}.tar.gz"
sha256 = "3cdbbf3fac90dc6f118bfd64384f309edeadd902d7c8fb17f02ffa1fc3f49690"


def post_install(self):
    self.install_license("LICENSE")
