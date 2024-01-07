pkgname = "libexttextcat"
pkgver = "3.4.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-werror"]
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool"]
checkdepends = ["bash"]
pkgdesc = "N-Gram-Based Text Categorization library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://wiki.documentfoundation.org/Libexttextcat"
source = (
    f"https://dev-www.libreoffice.org/src/{pkgname}/{pkgname}-{pkgver}.tar.xz"
)
sha256 = "6d77eace20e9ea106c1330e268ede70c9a4a89744ddc25715682754eca3368df"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libexttextcat-progs")
def _progs(self):
    return self.default_progs()


@subpackage("libexttextcat-devel")
def _devel(self):
    return self.default_devel()
