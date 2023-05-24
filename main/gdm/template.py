pkgname = "gdm"
pkgver = "44.0"
pkgrel = 0
build_style = "meson"
# TODO: plymouth
configure_args = [
    "-Ddefault-pam-config=arch",
    "-Dat-spi-registryd-dir=/usr/libexec",
    "-Dscreenshot-dir=/var/lib/gdm/greeter",
    "-Dplymouth=disabled",
    "-Dxauth-dir=/run/gdm",
    "-Dpid-file=/run/gdm/gdm.pid",
    "-Dwayland-support=true",
    "-Dselinux=disabled",
    "-Dlibaudit=disabled",
    "-Dsystemd-journal=false",
    "-Dsystemdsystemunitdir=/tmp",
    "-Ddbus-sys=/usr/share/dbus-1/system.d",
    "-Dsystemduserunitdir=/tmp",
    "-Ddefault_library=shared",
    "-Duser=_gdm",
    "-Dgroup=_gdm",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "dconf",
    "gettext-tiny",
    "gobject-introspection",
    "glib-devel",
    "linux-pam-devel",
    "itstool",
]
makedepends = [
    "elogind-devel",
    "gettext-tiny-devel",
    "accountsservice-devel",
    "glib-devel",
    "libx11-devel",
    "libxau-devel",
    "libcanberra-devel",
    "libgudev-devel",
    "gtk+3-devel",
    "xserver-xorg-devel",
    "linux-pam-devel",
]
checkdepends = ["check-devel"]
depends = [
    "gnome-settings-daemon",
    "gnome-shell",
    "gnome-session",
    "xwayland",
    "xrdb",
    "gsettings-desktop-schemas",
    "elogind",
    "turnstile",
]
pkgdesc = "GNOME display manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/GDM"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "ce20b0a221dbf8cde0064b501fd8f38f73839152857c4535337eb09cc52f7f6c"
system_users = [
    {
        "name": "_gdm",
        "id": None,
        "home": "/var/lib/gdm",
    }
]


def post_install(self):
    self.install_file(self.files_path / "Xsession", "etc/gdm", mode=0o755)

    self.install_service(self.files_path / "gdm-prepare")
    self.install_service(self.files_path / "gdm")

    # drop leftovers
    self.rm(self.destdir / "tmp", recursive=True)


@subpackage("libgdm")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()


@subpackage("gdm-devel")
def _devel(self):
    return self.default_devel()
