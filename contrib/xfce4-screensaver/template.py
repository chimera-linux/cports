pkgname = "xfce4-screensaver"
pkgver = "4.18.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-xf86gamma-ext"]
make_cmd = "gmake"
# check target fails without this
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
    "intltool",
    "libtool",
    "pkgconf",
    "xfce4-dev-tools",
]
makedepends = [
    "dbus-glib-devel",
    "elogind-devel",
    "garcon-devel",
    "glib-devel",
    "gtk+3-devel",
    "libwnck-devel",
    "libx11-devel",
    "libxext-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "libxklavier-devel",
    "libxrandr",
    "libxscrnsaver-devel",
    "libxxf86vm-devel",
    "linux-pam-devel",
    "mesa-devel",
    "shadow-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce screensaver"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/xfce4-screensaver/start"
source = f"$(XFCE_SITE)/apps/xfce4-screensaver/{pkgver[:-2]}/xfce4-screensaver-{pkgver}.tar.bz2"
sha256 = "d171316136a1189dfe69ef3da7f7a7f842014129ece184cc21ffb13bc0e13a39"
