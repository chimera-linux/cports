pkgname = "xfce4-mailwatch-plugin"
pkgver = "1.4.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
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
license = "GPL-2.0-only"
url = "https://docs.xfce.org/panel-plugins/xfce4-mailwatch-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-mailwatch-plugin/{pkgver[:-2]}/xfce4-mailwatch-plugin-{pkgver}.tar.xz"
sha256 = "5c211025db1096663fa6b8cc41213464a6d71f24e76326499d857ff81ea3861f"
