pkgname = "xfce4-notifyd"
pkgver = "0.9.4"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--disable-systemd"]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "gmake",
    "libtool",
    "pkgconf",
    "xfce4-dev-tools",
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
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-only"
url = "https://docs.xfce.org/apps/xfce4-notifyd/start"
source = f"$(XFCE_SITE)/apps/xfce4-notifyd/{pkgver[:-2]}/xfce4-notifyd-{pkgver}.tar.bz2"
sha256 = "ae6c128c055c44bd07202f73ae69ad833c5e4754f3530696965136e4d9ea7818"
