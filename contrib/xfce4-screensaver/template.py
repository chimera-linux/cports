pkgname = "xfce4-screensaver"
pkgver = "4.18.3"
pkgrel = 1
# workaround for lack of gdbus port
_dbus_gmain_rev = "93e8fced640e29bd6fbcc066a6c854a8dd74f8ab"
build_style = "gnu_configure"
configure_args = ["--with-xf86gamma-ext"]
# check target fails without this
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
    "dbus-devel",
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
source = [
    f"$(XFCE_SITE)/apps/xfce4-screensaver/{pkgver[:-2]}/xfce4-screensaver-{pkgver}.tar.bz2",
    f"https://gitlab.freedesktop.org/dbus/dbus-glib/-/archive/{_dbus_gmain_rev}/dbus-glib-{_dbus_gmain_rev}.tar.gz",
]
source_paths = [".", "dbus-gmain"]
sha256 = [
    "d171316136a1189dfe69ef3da7f7a7f842014129ece184cc21ffb13bc0e13a39",
    "b05a1cab9564d5490df3f92d564cec8582e82cc264130a071b0e0a8d9350ec18",
]


def post_extract(self):
    self.mkdir("src/dbus-gmain")
    self.cp("dbus-gmain/dbus-gmain.c", "src")
    self.cp("dbus-gmain/dbus-gmain/dbus-gmain.h", "src/dbus-gmain")


def post_install(self):
    self.rename("etc/pam.d", "usr/lib/pam.d", relative=False)
