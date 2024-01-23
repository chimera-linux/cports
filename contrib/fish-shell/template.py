pkgname = "fish-shell"
pkgver = "3.7.0"
pkgrel = 1
build_style = "cmake"
make_check_target = "fish_run_tests"
hostmakedepends = ["cmake", "ninja", "pkgconf", "gettext"]
makedepends = ["ncurses-devel", "pcre2-devel"]
checkdepends = ["python", "procps"]
pkgdesc = "Friendly interactive command line shell"
maintainer = "lunamothxyz <mail@lunamoth.xyz>"
license = "GPL-2.0-only"
url = "https://fishshell.com"
source = f"https://github.com/fish-shell/fish-shell/releases/download/{pkgver}/fish-{pkgver}.tar.xz"
sha256 = "df1b7378b714f0690b285ed9e4e58afe270ac98dbc9ca5839589c1afcca33ab1"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_shell("/usr/bin/fish")
