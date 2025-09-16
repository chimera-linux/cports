pkgname = "modemmanager"
pkgver = "1.24.2"
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
    "dinit-chimera",
    "dinit-dbus",
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
sha256 = "fbc75adcc0d7b0565f256e7ff4e8872b0a37c4413ff576665f7470932d9c1b68"


def post_install(self):
    self.install_service(self.files_path / "modemmanager")


@subpackage("modemmanager-devel")
def _(self):
    return self.default_devel()


@subpackage("modemmanager-libs")
def _(self):
    return self.default_libs()
