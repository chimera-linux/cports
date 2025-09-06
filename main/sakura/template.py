pkgname = "sakura"
pkgver = "3.8.9"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "gettext", "ninja", "perl", "pkgconf"]
makedepends = ["vte-gtk3-devel"]
pkgdesc = "Libvte-based terminal emulator"
license = "GPL-2.0-only"
url = "https://launchpad.net/sakura"
source = f"{url}/trunk/{pkgver}/+download/sakura-{pkgver}.tar.gz"
sha256 = "0bf1151b08c05e3d151e827ee3f8f68639133f5462e3e0761f82946aa3fe50df"
hardening = ["cfi", "vis"]
# FIXME lintpixmaps
options = ["!lintpixmaps"]
