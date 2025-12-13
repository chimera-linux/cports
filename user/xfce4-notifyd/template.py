pkgname = "xfce4-notifyd"
pkgver = "0.9.7"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dsystemd=disabled"]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "meson",
    "pkgconf",
]
makedepends = [
    "dbus-devel",
    "elogind-devel",
    "glib-devel",
    "gtk+3-devel",
    "gtk-layer-shell-devel",
    "libcanberra-devel",
    "libnotify-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "sqlite-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce notification daemon"
license = "GPL-2.0-only"
url = "https://docs.xfce.org/apps/xfce4-notifyd/start"
# source = f"$(XFCE_SITE)/apps/xfce4-notifyd/{pkgver[:-2]}/xfce4-notifyd-{pkgver}.tar.bz2"
source = f"https://gitlab.xfce.org/apps/xfce4-notifyd/-/archive/xfce4-notifyd-{pkgver}/xfce4-notifyd-xfce4-notifyd-{pkgver}.tar.gz"
sha256 = "2b0cb5abc1aa59bc70f9208bb648cfd6616120765ca24c3f2c716182d38c3630"
