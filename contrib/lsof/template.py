pkgname = "lsof"
pkgver = "4.98.0"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "groff",
    "gmake",
    "pkgconf",
]
makedepends = ["linux-headers"]
checkdepends = ["bash"]
pkgdesc = "List open files"
maintainer = "psykose <alice@ayaya.dev>"
license = "custom:lsof"
url = "https://lsof.readthedocs.io/en/latest"
source = f"https://github.com/lsof-org/lsof/releases/download/{pkgver}/lsof-{pkgver}.tar.gz"
sha256 = "2f8efa62cdf8715348b8f76bf32abf59f109a1441df35c686d23dccdeed34d99"
# FIXME: cfi
hardening = ["vis"]
# FIXME: weird failures
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
