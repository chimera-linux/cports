pkgname = "pulsemixer"
pkgver = "1.5.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-setuptools"]
depends = ["libpulse"]
pkgdesc = "CLI and curses mixer for PulseAudio"
maintainer = "Denis Strizhkin <strdenis02@gmail.com>"
license = "MIT"
url = "https://github.com/GeorgeFilipkin/pulsemixer"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2ccc850d2e414300f7513ac36334c0be16ef300fef6f45a3e3f05f83c50fd19d"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
