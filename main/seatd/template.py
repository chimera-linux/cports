pkgname = "seatd"
pkgver = "0.8.0"
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
sha256 = "a562a44ee33ccb20954a1c1ec9a90ecb2db7a07ad6b18d0ac904328efbcf65a0"

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
