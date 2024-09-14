pkgname = "fish-shell"
pkgver = "3.7.1"
pkgrel = 3
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
sha256 = "614c9f5643cd0799df391395fa6bbc3649427bb839722ce3b114d3bbc1a3b250"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_shell("/usr/bin/fish")
