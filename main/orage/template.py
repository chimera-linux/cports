pkgname = "orage"
pkgver = "4.20.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-x11-tray-icon"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "pkgconf",
    "slibtool",
    "xfce4-dev-tools",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "libical-devel",
    "libnotify-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
]
pkgdesc = "Xfce time-managing app"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/orage/start"
source = f"$(XFCE_SITE)/apps/orage/{pkgver[:-2]}/orage-{pkgver}.tar.bz2"
sha256 = "6bfd3da084c2977fb5cee26c8e94bf55e358da8e86dd2a83c6fa9174f24672a1"
