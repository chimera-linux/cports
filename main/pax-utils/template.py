pkgname = "pax-utils"
pkgver = "1.3.7"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dlddtree_implementation=python",
    "-Duse_libcap=enabled",
    "-Duse_fuzzing=false",
]
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "libcap-devel",
    "linux-headers",
]
checkdepends = [
    "bash",
    "python-pyelftools",
]
pkgdesc = "ELF related utils for ELF binaries"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-only"
url = "https://github.com/gentoo/pax-utils"
source = f"https://dev.gentoo.org/~sam/distfiles/app-misc/pax-utils/pax-utils-{pkgver}.tar.xz"
sha256 = "108362d29668d25cf7b0cadc63b15a4c1cfc0dbc71adc151b33c5fe7dece939a"
hardening = ["vis", "cfi"]
# see below
options = []


match self.profile().arch:
    case "ppc64le" | "ppc64":
        # FIXME lddtree/scanelf fail
        options += ["!check"]


@subpackage("lddtree")
def _(self):
    self.depends += ["python-pyelftools"]
    self.install_if = [self.parent, "python"]
    self.pkgdesc = "Print ELF dependency trees"
    return ["usr/bin/lddtree"]


@subpackage("symtree")
def _(self):
    self.depends += [self.parent, "bash"]
    self.install_if = [self.parent, "bash"]
    self.pkgdesc = "Display libraries that satisfy undefined symbols"
    return ["usr/bin/symtree"]
