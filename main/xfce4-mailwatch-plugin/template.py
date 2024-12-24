pkgname = "xfce4-mailwatch-plugin"
pkgver = "1.3.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "pkgconf",
    "slibtool",
    "xfce4-dev-tools",
]
makedepends = [
    "exo-devel",
    "gnutls-devel",
    "gtk+3-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce mail watcher panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-only"
url = "https://docs.xfce.org/panel-plugins/xfce4-mailwatch-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-mailwatch-plugin/{pkgver[:-2]}/xfce4-mailwatch-plugin-{pkgver}.tar.bz2"
sha256 = "c4783f1533891cd2e0c34066da859864dce45a23caa6015b58cb9fa9d65a7e44"
