pkgname = "janet"
pkgver = "1.43.1"
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
sha256 = "01e82762eac894af315db2e1e0cecdf3a935a27e2cde79ec1b8840a8a5ae0e85"


def post_install(self):
    self.install_license("LICENSE")


@split("devel")
def _(self):
    return self.default_devel()
