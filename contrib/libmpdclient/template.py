pkgname = "libmpdclient"
pkgver = "2.22"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dtest=true"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["check-devel"]
pkgdesc = "Asynchronous API library for interfacing with MPD"
maintainer = "avgwst <avgwst@tutanota.de>"
license = "BSD-2-Clause AND BSD-3-Clause"
url = "https://musicpd.org/libs/libmpdclient"
source = (
    f"https://www.musicpd.org/download/{pkgname}/2/{pkgname}-{pkgver}.tar.xz"
)
sha256 = "eac15b82b5ba5ed0648af580221eb74657394f7fe768e966d9e9ebb27435429f"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("LICENSES/BSD-2-Clause.txt")
    self.install_license("LICENSES/BSD-3-Clause.txt")


@subpackage("libmpdclient-devel")
def _devel(self):
    return self.default_devel()
