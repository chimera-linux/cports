pkgname = "xfce4-screensaver"
pkgver = "4.20.0"
pkgrel = 1
# workaround for lack of gdbus port
_dbus_gmain_rev = "623a4f3386a675060335e20afd810c6e10ae2cc8"
build_style = "gnu_configure"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "pkgconf",
    "slibtool",
    "xfce4-dev-tools",
]
makedepends = [
    "dbus-devel",
    "elogind-devel",
    "garcon-devel",
    "gtk+3-devel",
    "libwnck-devel",
    "libx11-devel",
    "libxext-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "libxklavier-devel",
    "libxscrnsaver-devel",
    "linux-pam-devel",
    "mesa-devel",
    "shadow-devel",
    "xfconf-devel",
]
# Needed for xfce4-screensaver-configure.py
depends = ["python-gobject"]
pkgdesc = "Xfce screensaver"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/xfce4-screensaver/start"
source = [
    f"$(XFCE_SITE)/apps/xfce4-screensaver/{pkgver[:-2]}/xfce4-screensaver-{pkgver}.tar.xz",
    f"https://gitlab.freedesktop.org/dbus/dbus-glib/-/archive/{_dbus_gmain_rev}/dbus-glib-{_dbus_gmain_rev}.tar.gz",
]
source_paths = [".", "dbus-gmain"]
sha256 = [
    "e370298d002848fdb2065fee254cb5b0efa0f2699b74299c234019c8d79b852e",
    "c1206c06fd625e864e06dbf43bab8543837ac35cbefa03457eda152cdf60c9ba",
]
# FIXME lintpixmaps
options = ["!lintpixmaps"]


def post_extract(self):
    self.mkdir("src/dbus-gmain")
    self.cp("dbus-gmain/dbus-gmain/dbus-gmain.c", "src")
    self.cp("dbus-gmain/dbus-gmain/dbus-gmain.h", "src/dbus-gmain")


def post_install(self):
    self.rename("etc/pam.d", "usr/lib/pam.d", relative=False)
