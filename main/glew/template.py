pkgname = "glew"
pkgver = "2.2.0"
pkgrel = 0
build_style = "makefile"
make_build_args = ["SYSTEM=linux-clang"]
make_install_target = "install.all"
make_install_args = ["SYSTEM=linux-clang"]
make_use_env = True
hostmakedepends = ["pkgconf"]
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

tool_flags = {
    "CFLAGS": ["-fPIC"],
}


def init_configure(self):
    cfl = self.get_cflags(shell=True)
    ldfl = self.get_ldflags(shell=True)

    self.make_build_args += [
        "CC=" + self.get_tool("CC"),
        "LD=" + self.get_tool("CC"),
        "AR=" + self.get_tool("AR"),
        "AS=" + self.get_tool("AS"),
        "RANLIB=" + self.get_tool("RANLIB"),
        "CFLAGS.EXTRA=" + cfl,
        "LDFLAGS.EXTRA=" + f"{cfl} {ldfl}",
    ]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("glew-devel")
def _(self):
    return self.default_devel()
