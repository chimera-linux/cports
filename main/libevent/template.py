pkgname = "libevent"
pkgver = "2.1.12"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["openssl-devel"]
pkgdesc = "Abstract asynchronous event notification library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://libevent.org"
source = f"https://github.com/libevent/libevent/releases/download/release-{pkgver}-stable/{pkgname}-{pkgver}-stable.tar.gz"
sha256 = "92e6de1be9ec176428fd2367677e61ceffc2ee1cb119035037a27d346b0403bb"
hardening = ["!cfi"]  # TODO
# test suite does not like our env
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libevent-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
