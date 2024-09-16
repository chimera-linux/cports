pkgname = "janet"
pkgver = "1.36.0"
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
sha256 = "104aa500d4a43c2c147851823fd8b7cd06a90d01efcdff71529ff1fa68953bb4"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("janet-devel")
def _(self):
    return self.default_devel()
