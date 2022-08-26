pkgname = "modemmanager"
pkgver = "1.18.10"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static", "--disable-Werror", "--enable-introspection",
    "--enable-vala", "--enable-plugin-qcom-soc", "--with-polkit=permissive",
    "--with-udev-base-dir=/usr/lib/udev",
]
make_cmd = "gmake"
hostmakedepends = [
    "gmake", "pkgconf", "glib-devel", "gobject-introspection", "vala",
    "xsltproc", "gettext-tiny",
]
makedepends = [
    "libglib-devel", "libgudev-devel", "polkit-devel", "libqmi-devel",
    "libmbim-devel", "libxslt-devel", "vala-devel", "elogind-devel",
    "python-gobject-devel", "python-dbus-devel", "linux-headers", "ppp"
]
depends = ["ppp"]
checkdepends = ["dbus"]
pkgdesc = "Mobile broadband modem management service"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.freedesktop.org/wiki/Software/ModemManager"
source = f"$(FREEDESKTOP_SITE)/ModemManager/ModemManager-{pkgver}.tar.xz"
sha256 = "16255f8229eeeb2dfecb8dd1370360d46f1015ec85e6fba5c1cbd9f4371d65eb"

@subpackage("modemmanager-devel")
def _devel(self):
    return self.default_devel()

@subpackage("modemmanager-libs")
def _lib(self):
    return self.default_libs()
