pkgname = "glew"
pkgver = "2.2.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_install_target = "install.all"
make_install_args = ["SYSTEM=linux-clang"]
hostmakedepends = ["pkgconf", "gmake"]
makedepends = ["libxext-devel", "libxmu-devel", "libxi-devel", "glu-devel"]
pkgdesc = "OpenGL Extension Wrangler Library"
maintainer = "eater <=@eater.me>"
license = "BSD-3-Clause"
# sourceforge site is outdated, so use github instead
url = "https://github.com/nigels-com/glew"
source = f"https://github.com/nigels-com/glew/releases/download/glew-{pkgver}/glew-{pkgver}.tgz"
sha256 = "d4fc82893cfb00109578d0a1a2337fb8ca335b3ceccf97b97e5cc7f08e4353e1"
# no tests
options = ["!check"]


def do_build(self):
    self.make.build([
        "CC=" + self.get_tool("CC"),
        "LD=" + self.get_tool("CC"),
        f"CFLAGS.EXTRA=-fPIC {self.get_cflags(shell=True)} {self.get_ldflags(shell=True)}",
        f"LDFLAGS.EXTRA={self.get_ldflags(shell=True)}",
        "AS=" + self.get_tool("AS"),
        "AR=" + self.get_tool("AR"),
        "SYSTEM=linux-clang"
    ])


@subpackage("glew-devel")
def _devel(self):
    return self.default_devel()
