pkgname = "libexttextcat"
pkgver = "3.4.6"
pkgrel = 1
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
sha256 = "6d77eace20e9ea106c1330e268ede70c9a4a89744ddc25715682754eca3368df"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libexttextcat-progs")
def _(self):
    return self.default_progs()


@subpackage("libexttextcat-devel")
def _(self):
    return self.default_devel()
