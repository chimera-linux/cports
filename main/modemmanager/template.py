pkgname = "modemmanager"
pkgver = "1.22.0"
pkgrel = 3
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
    "meson",
    "pkgconf",
    "vala",
    "libxslt-progs",
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.freedesktop.org/wiki/Software/ModemManager"
source = f"https://gitlab.freedesktop.org/mobile-broadband/ModemManager/-/archive/{pkgver}/ModemManager-{pkgver}.tar.gz"
sha256 = "6c8f8720737a3788e394c700f36236278c9de09d76069a079e6f1daaf08b2768"


def post_install(self):
    self.install_service(self.files_path / "modemmanager")


@subpackage("modemmanager-devel")
def _(self):
    return self.default_devel()


@subpackage("modemmanager-libs")
def _(self):
    return self.default_libs()
