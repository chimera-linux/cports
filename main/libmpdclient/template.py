pkgname = "libmpdclient"
pkgver = "2.23"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dtest=true"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["check-devel"]
pkgdesc = "Asynchronous API library for interfacing with MPD"
license = "BSD-2-Clause AND BSD-3-Clause"
url = "https://musicpd.org/libs/libmpdclient"
source = f"https://www.musicpd.org/download/libmpdclient/2/libmpdclient-{pkgver}.tar.xz"
sha256 = "4a1b6c7f783d8cac3d3b8e4cbe9ad021c45491e383de3b893ea4eedefbc71607"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("LICENSES/BSD-2-Clause.txt")
    self.install_license("LICENSES/BSD-3-Clause.txt")


@subpackage("libmpdclient-devel")
def _(self):
    return self.default_devel()
