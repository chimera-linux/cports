pkgname = "janet"
pkgver = "1.41.2"
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
sha256 = "168e97e1b790f6e9d1e43685019efecc4ee473d6b9f8c421b49c195336c0b725"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("janet-devel")
def _(self):
    return self.default_devel()
