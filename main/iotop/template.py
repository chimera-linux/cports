pkgname = "iotop"
pkgver = "1.27"
pkgrel = 0
build_style = "makefile"
hostmakedepends = [
    "pkgconf",
]
makedepends = [
    "linux-headers",
    "ncurses-devel",
]
pkgdesc = "Top-like utility for IO"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/Tomas-M/iotop"
source = f"https://github.com/Tomas-M/iotop/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ca643a9d11fb398158decd2094dcf74c3e4625d06c54300073a69f1e92c721ea"
hardening = ["cfi", "vis"]
# no tests
options = ["!check"]
