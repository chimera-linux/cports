pkgname = "pax-utils"
pkgver = "1.3.8"
pkgrel = 1
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://github.com/gentoo/pax-utils"
source = f"https://dev.gentoo.org/~sam/distfiles/app-misc/pax-utils/pax-utils-{pkgver}.tar.xz"
sha256 = "12a168d1aeae2626efdbde3979da88a60ca80bb38e1db565e95ee441ff1d5a0c"
hardening = ["vis", "cfi"]
# see below
options = []


match self.profile().arch:
    case "ppc64le" | "ppc64":
        # FIXME lddtree/scanelf fail
        options += ["!check"]


@subpackage("pax-utils-lddtree")
def _(self):
    self.depends += ["python-pyelftools"]
    self.install_if = [self.parent, "python"]
    self.provides = [self.with_pkgver("lddtree")]
    self.pkgdesc = "Print ELF dependency trees"
    return ["usr/bin/lddtree"]


@subpackage("pax-utils-symtree")
def _(self):
    self.depends += [self.parent, "bash"]
    self.install_if = [self.parent, "bash"]
    self.provides = [self.with_pkgver("symtree")]
    self.pkgdesc = "Display libraries that satisfy undefined symbols"
    return ["usr/bin/symtree"]
