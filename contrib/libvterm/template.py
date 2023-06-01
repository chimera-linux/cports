pkgname = "libvterm"
pkgver = "0.3.2"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_check_target = "test"
hostmakedepends = ["gmake", "libtool", "perl", "pkgconf"]
pkgdesc = "Abstract VT220/xterm/ECMA-48 emulation library"
license = "MIT"
url = "http://www.leonerd.org.uk/code/libvterm"
source = f"http://www.leonerd.org.uk/code/libvterm/libvterm-{pkgver}.tar.gz"
sha256 = "91eb5088069f4e6edab69e14c4212f6da0192e65695956dc048016a0dab8bcf6"
# crossbuild fails because of libtool
options = ["!cross"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libvterm-devel")
def _devel(self):
    return self.default_devel()
