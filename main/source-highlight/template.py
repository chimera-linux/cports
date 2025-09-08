pkgname = "source-highlight"
pkgver = "3.1.9"
pkgrel = 9
build_style = "gnu_configure"
configure_args = [
    "--with-bash-completion=/usr/share/bash-completion/completions"
]
make_check_args = ["-j1"]
hostmakedepends = ["pkgconf", "automake", "slibtool"]
makedepends = ["boost-devel"]
pkgdesc = "Convert source code to syntax highlighted document"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/src-highlite"
source = f"$(GNU_SITE)/src-highlite/source-highlight-{pkgver}.tar.gz"
sha256 = "3a7fd28378cb5416f8de2c9e77196ec915145d44e30ff4e0ee8beb3fe6211c91"
options = ["!cross"]

tool_flags = {"CXXFLAGS": ["-Wno-dynamic-exception-spec", "-Wno-register"]}


def post_install(self):
    self.install_license("COPYING")


@subpackage("source-highlight-libs")
def _(self):
    return self.default_libs()


@subpackage("source-highlight-devel")
def _(self):
    self.depends += ["boost-devel"]
    return self.default_devel()
