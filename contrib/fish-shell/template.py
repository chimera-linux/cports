pkgname = "fish-shell"
pkgver = "3.6.4"
pkgrel = 0
build_style = "cmake"
make_build_args = ["--target", "all", "fish_tests"]
hostmakedepends = ["cmake", "ninja", "pkgconf", "gettext"]
makedepends = ["ncurses-devel", "pcre2-devel"]
checkdepends = ["python", "procps"]
pkgdesc = "Friendly interactive command line shell"
maintainer = "lunamothxyz <mail@lunamoth.xyz>"
license = "GPL-2.0-only"
url = "https://fishshell.com"
source = f"https://github.com/fish-shell/{pkgname}/releases/download/{pkgver}/fish-{pkgver}.tar.xz"
sha256 = "0f3f610e580de092fbe882c8aa76623ecf91bb16fdf0543241e6e90d5d4bc393"
# FIXME int: test fail
hardening = ["vis", "cfi", "!int"]


def do_check(self):
    # fails to find test script via ctest in out-of-tree builddir
    with self.pushd(self.make_dir):
        self.do("./fish_tests")


def post_install(self):
    self.install_shell("/usr/bin/fish")
