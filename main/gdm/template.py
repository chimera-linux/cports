pkgname = "gdm"
pkgver = "46.2"
pkgrel = 1
build_style = "meson"
# TODO: plymouth
configure_args = [
    "-Ddefault-pam-config=arch",
    "-Dat-spi-registryd-dir=/usr/libexec",
    "-Dscreenshot-dir=/var/lib/gdm/greeter",
    "-Dplymouth=disabled",
    "-Dxauth-dir=/run/gdm",
    "-Dpam-prefix=/usr/lib",
    "-Dpid-file=/run/gdm/gdm.pid",
    "-Dwayland-support=true",
    "-Dselinux=disabled",
    "-Dlibaudit=disabled",
    "-Dsystemd-journal=false",
    "-Dsystemdsystemunitdir=/tmp",
    "-Ddbus-sys=/usr/share/dbus-1/system.d",
    "-Dsystemdsystemunitdir=no",
    "-Dsystemduserunitdir=no",
    "-Ddefault_library=shared",
    "-Dlogind-provider=elogind",
    "-Duser=_gdm",
    "-Dgroup=_gdm",
]
hostmakedepends = [
    "dconf",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "itstool",
    "linux-pam-devel",
    "meson",
    "pkgconf",
]
makedepends = [
    "accountsservice-devel",
    "elogind-devel",
    "gettext-devel",
    "glib-devel",
    "gtk+3-devel",
    "json-glib-devel",
    "libcanberra-devel",
    "libgudev-devel",
    "libx11-devel",
    "libxau-devel",
    "linux-pam-devel",
]
checkdepends = ["check-devel"]
depends = [
    "elogind",
    "fprintd-meta",
    "gnome-session",
    "gnome-settings-daemon",
    "gnome-shell",
    "gsettings-desktop-schemas",
    "openrc-settingsd",
    "turnstile",
    "xrdb",
    "xwayland",
]
pkgdesc = "GNOME display manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/GDM"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "4ee345422a16537150cd842450cda52b2ca86984bc51ee20cdc025dcf4bd268b"


def post_install(self):
    self.install_file(self.files_path / "Xsession", "etc/gdm", mode=0o755)

    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")

    self.install_service(self.files_path / "gdm")

    # drop magic nonsense with wayland disabling, we don't support
    # xorg in main repository anyway, so that has to be optional
    self.uninstall("usr/lib/udev/rules.d/61-gdm.rules")


@subpackage("libgdm")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()


@subpackage("gdm-devel")
def _devel(self):
    return self.default_devel()
