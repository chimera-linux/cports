pkgname = "seatd"
pkgver = "0.7.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dexamples=disabled",
    "-Dlibseat-logind=elogind",
    "-Dwerror=false",
]
hostmakedepends = ["meson", "pkgconf", "scdoc"]
makedepends = ["elogind-devel", "linux-headers"]
pkgdesc = "Seat management daemon"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://kl.wtf/projects/seatd"
source = f"https://git.sr.ht/~kennylevinsen/{pkgname}/archive/{pkgver}.tar.gz"
sha256 = "210ddf8efa1149cde4dd35908bef8e9e63c2edaa0cdb5435f2e6db277fafff3c"

system_groups = ["_seatd"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "seatd")


@subpackage("libseat")
def _lib(self):
    self.pkgdesc = "Universal seat management library"

    return self.default_libs()


@subpackage("libseat-devel")
def _dev(self):
    self.pkgdesc = "Universal seat management library (development files)"

    return self.default_devel()
