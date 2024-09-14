pkgname = "libvterm"
pkgver = "0.3.3"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
hostmakedepends = ["libtool", "perl", "pkgconf"]
pkgdesc = "Abstract VT220/xterm/ECMA-48 emulation library"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "MIT"
url = "http://www.leonerd.org.uk/code/libvterm"
source = f"http://www.leonerd.org.uk/code/libvterm/libvterm-{pkgver}.tar.gz"
sha256 = "09156f43dd2128bd347cbeebe50d9a571d32c64e0cf18d211197946aff7226e0"
# crossbuild fails because of libtool
options = ["!cross"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libvterm-devel")
def _(self):
    return self.default_devel()
