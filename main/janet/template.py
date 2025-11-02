pkgname = "janet"
pkgver = "1.39.1"
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
sha256 = "a43489328b88846e5cddbdad9274f25ee9854e337e52490a74bb7955de03c650"

if self.profile().arch == "ppc":
    broken = "fails to boot"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("janet-devel")
def _(self):
    return self.default_devel()
