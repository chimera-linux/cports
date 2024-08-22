pkgname = "xfce4-mailwatch-plugin"
pkgver = "1.3.1"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "intltool",
    "libtool",
    "pkgconf",
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
sha256 = "054964e9fe4ca668486400991ce1ea01d07aac7ba235f4b14d4a8f7d9800046a"
