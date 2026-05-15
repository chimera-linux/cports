pkgname = "tessen"
pkgver = "2.3.0"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["scdoc"]
depends = [
    "libnotify",
    "wl-clipboard",
    "wtype",
]
pkgdesc = "Interactive menu to autotype and copy pass data"
license = "GPL-2.0-only"
url = "https://tangled.org/@jcg.re/tessen"
source = f"{url}/archive/v{pkgver}>{pkgver}.tar.gz"
sha256 = "ec316b5bbf89baf5caa7d2a15d71a9ae6c30b1f2987421d1b31b396c5871cf2d"
# checks require shellcheck which isn't packaged (yet)
options = ["!check"]
