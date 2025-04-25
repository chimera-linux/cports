pkgname = "bpytop"
pkgver = "1.0.68"
pkgrel = 0
build_style = "makefile"
depends = [
    "python-psutil",
]
pkgdesc = "Linux/OSX/FreeBSD resource monitor"
license = "Apache-2.0"
url = "https://github.com/aristocratos/bpytop"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3a936f8899efb66246e82bbcab33249bf94aabcefbe410e56f045a1ce3c9949f"
# The package has no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
