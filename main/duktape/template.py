pkgname = "duktape"
pkgver = "2.7.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["-f", "Makefile.sharedlibrary"]
make_install_args = ["-f", "Makefile.sharedlibrary", "INSTALL_PREFIX=/usr"]
make_check_target = ""
make_check_args = ["-f", "Makefile.cmdline"]
hostmakedepends = ["gmake", "pkgconf"]
pkgdesc = "Embeddeable JavaScript engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://duktape.org"
source = f"https://github.com/svaarala/duktape/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "90f8d2fa8b5567c6899830ddef2c03f3c27960b11aca222fa17aa7ac613c2890"
hardening = ["vis", "cfi"]


# a simple self-test in place of a real testsuite
def post_check(self):
    self.do(self.chroot_cwd / "duk", "-e", "print('hello world', 5 + 10)")


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("duktape-devel")
def _devel(self):
    return self.default_devel()
