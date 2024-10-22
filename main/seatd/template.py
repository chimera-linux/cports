pkgname = "seatd"
pkgver = "0.9.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dexamples=disabled",
    "-Dlibseat-logind=elogind",
]
hostmakedepends = ["meson", "pkgconf", "scdoc"]
makedepends = ["elogind-devel", "linux-headers"]
pkgdesc = "Seat management daemon"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://sr.ht/~kennylevinsen/seatd"
source = f"https://git.sr.ht/~kennylevinsen/seatd/archive/{pkgver}.tar.gz"
sha256 = "4276d1380c67e30a63c289b35f7bf955e126e6daf3596cd5aa6080670aa1214c"


def post_install(self):
    self.install_license("LICENSE")
    self.install_sysusers(self.files_path / "seatd.conf")
    self.install_service(self.files_path / "seatd")


@subpackage("libseat")
def _(self):
    self.pkgdesc = "Universal seat management library"

    return self.default_libs()


@subpackage("libseat-devel")
def _(self):
    self.pkgdesc = "Universal seat management library"

    return self.default_devel()
