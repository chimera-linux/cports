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
source = f"https://tangled.org/@jcg.re/tessen/archive/v{pkgver}>{pkgver}.tar.gz"
sha256 = "a19a15bfa1cedf802403168a60ecf3fa5a758d4ac88bdf32224661f239eb121b"
# checks require shellcheck which isn't packaged (yet)
options = ["!check"]
