pkgname = "xfconf"
pkgver = "4.20.0"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--with-helper-path-prefix=/usr/libexec",
    "--enable-gsettings-backend",
]
make_check_wrapper = [
    "dbus-run-session",
    "--",
    "xwfb-run",
    "--",
]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "gobject-introspection",
    "gtk-doc-tools",
    "pkgconf",
    "python",
    "slibtool",
    "vala-devel",
    "xfce4-dev-tools",
]
makedepends = ["glib-devel", "libxfce4util-devel", "vala-devel"]
checkdepends = ["dbus", "xwayland-run"]
pkgdesc = "Xfce configuration system"
license = "GPL-2.0-only AND LGPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/xfconf/start"
source = f"$(XFCE_SITE)/xfce/xfconf/{pkgver[:-2]}/xfconf-{pkgver}.tar.bz2"
sha256 = "8bc43c60f1716b13cf35fc899e2a36ea9c6cdc3478a8f051220eef0f53567efd"
options = ["!cross"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("xfconf-devel")
def _(self):
    return self.default_devel()
