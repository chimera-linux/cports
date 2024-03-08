pkgname = "libmd"
pkgver = "1.1.0"
pkgrel = 0
build_style = "gnu_configure"
# broken autoreconf
configure_gen = []
hostmakedepends = ["pkgconf"]
pkgdesc = "Message Digest functions from BSD systems"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-3-Clause AND BSD-2-Clause AND ISC AND Beerware AND custom:none"
url = "https://www.hadrons.org/software/libmd"
source = f"https://archive.hadrons.org/software/libmd/libmd-{pkgver}.tar.xz"
sha256 = "1bd6aa42275313af3141c7cf2e5b964e8b1fd488025caf2f971f43b00776b332"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libmd-devel")
def _devel(self):
    return self.default_devel()
