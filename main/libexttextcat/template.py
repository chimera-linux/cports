pkgname = "libexttextcat"
pkgver = "3.4.8"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-werror"]
# out of tree builds don't install .lm files
make_dir = "."
hostmakedepends = ["pkgconf", "automake", "libtool"]
checkdepends = ["bash"]
pkgdesc = "N-Gram-Based Text Categorization library"
license = "BSD-3-Clause"
url = "https://wiki.documentfoundation.org/Libexttextcat"
source = f"https://dev-www.libreoffice.org/src/libexttextcat/libexttextcat-{pkgver}.tar.xz"
sha256 = "93eb89fd4fc8f565806354e100e778b3ac9a24e5fc04c24e6a83fb1e9b6c9d59"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libexttextcat-progs")
def _(self):
    return self.default_progs()


@subpackage("libexttextcat-devel")
def _(self):
    return self.default_devel()
