pkgname = "gigolo"
pkgver = "0.6.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gettext",
    "glib-devel",
    "meson",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
]
pkgdesc = "Xfce GIO/GVFS frontend"
license = "GPL-2.0-only"
url = "https://docs.xfce.org/apps/gigolo/start"
source = f"$(XFCE_SITE)/apps/gigolo/{pkgver[:-2]}/gigolo-{pkgver}.tar.xz"
sha256 = "f27dbb51abe8144c1b981f2d820ad1b279c1bc4623d7333b7d4f5f4777eb45ed"
