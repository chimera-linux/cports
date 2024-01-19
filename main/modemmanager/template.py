pkgname = "modemmanager"
pkgver = "1.18.12"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--disable-Werror",
    "--enable-introspection",
    "--enable-vala",
    "--enable-plugin-qcom-soc",
    "--with-polkit=permissive",
    "--with-udev-base-dir=/usr/lib/udev",
    "--with-dbus-sys-dir=/usr/share/dbus-1/system.d",
]
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "pkgconf",
    "glib-devel",
    "gobject-introspection",
    "vala",
    "xsltproc",
    "gettext",
]
makedepends = [
    "glib-devel",
    "libgudev-devel",
    "polkit-devel",
    "libqmi-devel",
    "libmbim-devel",
    "libxslt-devel",
    "vala-devel",
    "elogind-devel",
    "python-gobject-devel",
    "python-dbus-devel",
    "linux-headers",
    "ppp",
]
depends = ["ppp"]
checkdepends = ["dbus"]
pkgdesc = "Mobile broadband modem management service"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.freedesktop.org/wiki/Software/ModemManager"
source = f"$(FREEDESKTOP_SITE)/ModemManager/ModemManager-{pkgver}.tar.xz"
sha256 = "b464e4925d955a6ca86dd08616e763b26ae46d7fd37dbe281678e34065b1e430"


@subpackage("modemmanager-devel")
def _devel(self):
    return self.default_devel()


@subpackage("modemmanager-libs")
def _lib(self):
    return self.default_libs()


configure_gen = []
