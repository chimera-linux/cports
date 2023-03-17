pkgname = "fish-shell"
pkgver = "3.6.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf", "gettext-tiny"]
makedepends = ["ncurses-devel", "pcre2-devel"]
checkdepends = ["python", "procps"]
pkgdesc = "Friendly interactive command line shell"
maintainer = "lunamothxyz <mail@lunamoth.xyz>"
license = "GPL-2.0-only"
url = "https://fishshell.com"
source = f"https://github.com/fish-shell/{pkgname}/releases/download/{pkgver}/fish-{pkgver}.tar.xz"
sha256 = "97044d57773ee7ca15634f693d917ed1c3dc0fa7fde1017f1626d60b83ea6181"
# FIXME int: test fail
hardening = ["vis", "cfi", "!int"]

def post_install(self):
    self.install_shell("/usr/bin/fish")
