pkgname = "gdm"
pkgver = "48.0"
pkgrel = 0
build_style = "meson"
# TODO: plymouth
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "-Ddefault-pam-config=arch",
    "-Dat-spi-registryd-dir=/usr/lib",
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
    "dinit-chimera",
    "dinit-dbus",
    "elogind",
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
    "openrc-settingsd",
]
checkdepends = ["check-devel"]
depends = [
    "dinit-dbus",
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
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/GDM"
source = f"$(GNOME_SITE)/gdm/{pkgver[:-2]}/gdm-{pkgver}.tar.xz"
sha256 = "1bc06daff093ec7b5e37ecb4f92e5da3474a1b1ba076edb9151ee967d1c30adf"


def post_install(self):
    self.install_file(self.files_path / "Xsession", "etc/gdm", mode=0o755)

    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")

    self.install_service(self.files_path / "gdm")

    # drop magic nonsense with wayland disabling, we don't support
    # xorg in main repository anyway, so that has to be optional
    self.uninstall("usr/lib/udev/rules.d/61-gdm.rules")


@subpackage("gdm-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libgdm")]

    return self.default_libs()


@subpackage("gdm-devel")
def _(self):
    return self.default_devel()
