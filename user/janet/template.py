pkgname = "janet"
pkgver = "1.42.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Depoll=true"]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Dynamic Lisp dialect and bytecode VM"
license = "MIT"
url = "https://janet-lang.org"
source = (
    f"https://github.com/janet-lang/janet/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "2391f8c6565742dad1c5e8872ad1d570b64a239d5d1ef11a188fc6b400457a04"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("janet-devel")
def _(self):
    return self.default_devel()
