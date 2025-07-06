pkgname = "thunar-archive-plugin"
pkgver = "0.6.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
]
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "gtk+3-devel",
    "libxfce4util-devel",
    "thunar-devel",
]
pkgdesc = "Thunar archive plugin"
license = "LGPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/thunar/archive"
source = f"$(XFCE_SITE)/thunar-plugins/thunar-archive-plugin/{pkgver[:-2]}/thunar-archive-plugin-{pkgver}.tar.xz"
sha256 = "692708cd047c7a552f2f85fe2ee32f19c7d5be5bf695d0288e8cadf50289db06"
