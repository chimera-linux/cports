pkgname = "janet"
pkgver = "1.37.1"
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
sha256 = "85a87115fb7b59a3fb4dab7d291627ce109eecdcf84b403ec8787ef54082519f"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("janet-devel")
def _(self):
    return self.default_devel()
