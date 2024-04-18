pkgname = "janet"
pkgver = "1.34.0"
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
sha256 = "d49670c564dcff6f9f7945067fa2acbd3431d923c25fc4ce6e400de28eeb0b1b"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("janet-devel")
def _devel(self):
    return self.default_devel()
