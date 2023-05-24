pkgname = "libtermkey"
pkgver = "0.22"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_check_target = "test"
hostmakedepends = ["gmake", "libtool", "pkgconf", "perl"]
makedepends = ["unibilium-devel"]
pkgdesc = "Library for processing keyboard entry from terminal-based programs"
license = "MIT"
url = "http://www.leonerd.org.uk/code/libtermkey"
source = f"{url}/{pkgname}-{pkgver}.tar.gz"
sha256 = "6945bd3c4aaa83da83d80a045c5563da4edd7d0374c62c0d35aec09eb3014600"
# crossbuild fails because of libtool
options = ["!cross"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libtermkey-devel")
def _devel(self):
    return self.default_devel()
