pkgname = "snapraid"
pkgver = "14.7"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-blkid",
]
hostmakedepends = [
    "autoconf",
    "automake",
]
makedepends = ["util-linux-blkid-devel"]
pkgdesc = "Parity-based backup program for disk arrays"
license = "GPL-3.0-or-later"
url = "https://www.snapraid.it"
source = f"https://github.com/amadvance/snapraid/releases/download/v{pkgver}/snapraid-{pkgver}.tar.gz"
sha256 = "fe4c71d444bade85fe390d2a58de1ea34b53109278b96fb19bc9ac9133eb07ff"
