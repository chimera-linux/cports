pkgname = "libmpdclient"
pkgver = "2.27"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dtest=true"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["check-devel"]
pkgdesc = "Asynchronous API library for interfacing with MPD"
license = "BSD-2-Clause AND BSD-3-Clause"
url = "https://musicpd.org/libs/libmpdclient"
source = f"https://www.musicpd.org/download/libmpdclient/2/libmpdclient-{pkgver}.tar.xz"
sha256 = "88945b5abc11d8f4cea2bb7028e545024a6e060650bd65527a29bc9400daead8"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("LICENSES/BSD-2-Clause.txt")
    self.install_license("LICENSES/BSD-3-Clause.txt")


@subpackage("libmpdclient-devel")
def _(self):
    return self.default_devel()
