pkgname = "asahi-fwextract"
pkgver = "0.7.9"
pkgrel = 0
archs = ["aarch64"]
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-setuptools"]
depends = ["lzfse", "python"]
pkgdesc = "Asahi Linux firmware extractor"
license = "MIT"
url = "https://github.com/AsahiLinux/asahi-installer"
source = f"https://github.com/AsahiLinux/asahi-installer/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b41f39360ce6cd6de299c4f25cd69718530a5619b16fb7a1eed666083bd909e1"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
