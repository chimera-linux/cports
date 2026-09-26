pkgname = "pyradio"
pkgver = "0.9.3.11.31"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python",
    "python-charset-normalizer",
    "python-dateutil",
    "python-dnspython",
    "python-netifaces",
    "python-psutil",
    "python-rapidfuzz",
    "python-requests",
    "python-rich",
]
pkgdesc = "Command line internet radio player"
license = "MIT"
url = "https://github.com/coderholic/pyradio"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e4aca283ac05295020f6d187f90e902199a6897afe1fcaf6aa9304e098c3266d"
# check: no test suite ships with the project
# cross: blocked by python-rapidfuzz's !cross
options = ["!check", "!cross"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("docs/*.1", glob=True)
    self.install_file(
        "pyradio/icons/pyradio.png",
        "usr/share/icons/hicolor/512x512/apps",
    )
    self.install_file("devel/pyradio.desktop", "usr/share/applications")
