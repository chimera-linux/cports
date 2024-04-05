pkgname = "janet"
pkgver = "1.33.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Depoll=true"]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Dynamic Lisp dialect and bytecode VM"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "MIT"
url = "https://janet-lang.org"
source = (
    f"https://github.com/janet-lang/janet/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "c9018fbd69b825cfc706d8c40e9464be37e924ce07089933e92f4f931ccf0d8d"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("janet-devel")
def _devel(self):
    return self.default_devel()
