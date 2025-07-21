pkgname = "modemmanager"
pkgver = "1.24.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddbus_policy_dir=/usr/share/dbus-1/system.d",
    "-Ddefault_library=shared",
    "-Dintrospection=true",
    "-Dplugin_qcom_soc=enabled",
    "-Dpolkit=permissive",
    "-Dsystemd_journal=false",
    "-Dsystemdsystemunitdir=no",
    "-Dudevdir=/usr/lib/udev",
    "-Dvapi=true",
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "libxslt-progs",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "bash-completion",
    "elogind-devel",
    "glib-devel",
    "libgudev-devel",
    "libmbim-devel",
    "libqmi-devel",
    "libxslt-devel",
    "linux-headers",
    "polkit-devel",
    "ppp",
    "python-dbus-devel",
    "python-gobject-devel",
    "vala-devel",
]
depends = ["dinit-dbus", "ppp"]
checkdepends = ["dbus"]
pkgdesc = "Mobile broadband modem management service"
license = "GPL-2.0-or-later"
url = "https://www.freedesktop.org/wiki/Software/ModemManager"
source = f"https://gitlab.freedesktop.org/mobile-broadband/ModemManager/-/archive/{pkgver}/ModemManager-{pkgver}.tar.gz"
sha256 = "50e166bb24acb00bcaed814483920dfbc5b26d5424faee974b54c702e425a7c7"


def post_install(self):
    self.install_service(self.files_path / "modemmanager")


@subpackage("modemmanager-devel")
def _(self):
    return self.default_devel()


@subpackage("modemmanager-libs")
def _(self):
    return self.default_libs()
