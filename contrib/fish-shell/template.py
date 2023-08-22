pkgname = "fish-shell"
pkgver = "3.6.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf", "gettext"]
makedepends = ["ncurses-devel", "pcre2-devel"]
checkdepends = ["python", "procps"]
pkgdesc = "Friendly interactive command line shell"
maintainer = "lunamothxyz <mail@lunamoth.xyz>"
license = "GPL-2.0-only"
url = "https://fishshell.com"
source = f"https://github.com/fish-shell/{pkgname}/releases/download/{pkgver}/fish-{pkgver}.tar.xz"
sha256 = "55402bb47ca6739d8aba25e41780905b5ce1bce0a5e0dd17dca908b5bc0b49b2"
# FIXME int: test fail
hardening = ["vis", "cfi", "!int"]


def post_install(self):
    self.install_shell("/usr/bin/fish")
