pkgname = "fish-shell"
pkgver = "3.5.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf", "gettext-tiny"]
makedepends = ["ncurses-devel", "pcre2-devel"]
checkdepends = ["python", "procps-ng"]
pkgdesc = "Friendly interactive command line shell"
maintainer = "lunamothxyz <mail@lunamoth.xyz>"
license = "GPL-2.0-only"
url = "https://fishshell.com"
source = f"https://github.com/fish-shell/{pkgname}/releases/download/{pkgver}/fish-{pkgver}.tar.xz"
sha256 = "a6d45b3dc5a45dd31772e7f8dfdfecabc063986e8f67d60bd7ca60cc81db6928"

def post_install(self):
    self.install_shell("/usr/bin/fish")
