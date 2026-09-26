pkgname = "dillo-plus"
pkgver = "3.3.0"
pkgrel = 0
build_style = "makefile"
makedepends = [
    "fltk-devel",
    "giflib-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libxcursor-devel",
    "libxfixes-devel",
    "libxinerama-devel",
    "openssl3-devel",
]
pkgdesc = "Lightweight web browser"
license = "GPL-3.0-or-later"
url = "https://github.com/crossbowerbt/dillo-plus"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c4beaf2961607911ce2fac03341055498558bcfd6c6562f46e5b137958f85773"
# FIXME int: crashes
hardening = ["vis", "!int"]
# Makefile has no automated check target
# test/Makefile generates visual/interactive tests (mostly)
options = ["etcfiles", "!check"]
