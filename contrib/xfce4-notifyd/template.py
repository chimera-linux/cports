pkgname = "xfce4-notifyd"
pkgver = "0.9.6"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dhelper-path-prefix=/usr/libexec", "-Dsystemd=disabled"]
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
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-only"
url = "https://docs.xfce.org/apps/xfce4-notifyd/start"
# source = f"$(XFCE_SITE)/apps/xfce4-notifyd/{pkgver[:-2]}/xfce4-notifyd-{pkgver}.tar.bz2"
source = f"https://gitlab.xfce.org/apps/xfce4-notifyd/-/archive/xfce4-notifyd-{pkgver}/xfce4-notifyd-xfce4-notifyd-{pkgver}.tar.gz"
sha256 = "5650ab00b1bb9119d6990af53a9a798cdfc18193965c5c5c9fbf7f0bfed82525"
