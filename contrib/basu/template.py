pkgname = "basu"
pkgver = "0.2.1"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gperf",
    "meson",
    "pkgconf",
]
makedepends = [
    "libcap",
]
pkgdesc = "Standalone sd-bus library and busctl extracted from systemd"
maintainer = "Umar Getagazov <umar@handlerug.me>"
license = "LGPL-2.1-or-later"
url = "https://sr.ht/~emersion/basu"
source = f"https://git.sr.ht/~emersion/basu/archive/v{pkgver}.tar.gz"
sha256 = "43b327073d1ac7bc6cbc0d3dfff729348fc970dfff0551ad40e366332e990204"
# FIXME: cfi
hardening = ["vis", "!cfi"]


@subpackage("basu-devel")
def _devel(self):
    return self.default_devel()
