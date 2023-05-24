pkgname = "libvterm"
pkgver = "0.3.1"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_check_target = "test"
hostmakedepends = ["gmake", "libtool", "perl", "pkgconf"]
pkgdesc = "Abstract VT220/xterm/ECMA-48 emulation library"
license = "MIT"
url = "http://www.leonerd.org.uk/code/libvterm"
source = f"http://www.leonerd.org.uk/code/libvterm/libvterm-{pkgver}.tar.gz"
sha256 = "25a8ad9c15485368dfd0a8a9dca1aec8fea5c27da3fa74ec518d5d3787f0c397"
# crossbuild fails because of libtool
options = ["!cross"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libvterm-devel")
def _devel(self):
    return self.default_devel()
