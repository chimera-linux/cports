pkgname = "fish-shell"
pkgver = "3.7.0"
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
sha256 = "df1b7378b714f0690b285ed9e4e58afe270ac98dbc9ca5839589c1afcca33ab1"
# FIXME int: test fail
hardening = ["vis", "cfi", "!int"]


def do_check(self):
    # fails to find test script via ctest in out-of-tree builddir
    with self.pushd(self.make_dir):
        self.do("./fish_tests")


def post_install(self):
    self.install_shell("/usr/bin/fish")
