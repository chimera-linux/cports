pkgname = "blueman"
pkgver = "2.4.4"
pkgrel = 4
build_style = "meson"
# XXX drop libexec
configure_args = [
    "--libexecdir=/usr/lib",
    "-Druntime_deps_check=false",
]
hostmakedepends = [
    "gettext",
    "glib",
    "meson",
    "pkgconf",
    "python",
    "python-cython",
]
makedepends = [
    "bluez-devel",
    "glib-devel",
    "linux-headers",
    "python-gobject-devel",
]
depends = [
    "bluez",
    "gtk+3",
    "iproute2",
    "networkmanager-libs",
    "libpulse",
    "python-cairo",
    "python-gobject",
]
checkdepends = ["python-dbusmock", "python-dbus"]
pkgdesc = "GTK Bluetooth Manager"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-or-later"
url = "https://blueman-project.github.io/blueman"
source = f"https://github.com/blueman-project/blueman/releases/download/{pkgver}/blueman-{pkgver}.tar.xz"
sha256 = "d34f9154c8c6887d15679d129744922ac72f6a71cb2bccfb6662f8ca446e85f0"
# TODO
options = ["!check"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")
    self.uninstall("usr/lib/systemd/system")

    # TODO: caja and nemo-python aren't packaged, when they are, add a
    # subpackage for each extension (see blueman-nautilus below)
    self.uninstall("usr/share/nemo-python")
    self.uninstall("usr/share/caja-python")


@subpackage("blueman-nautilus")
def _(self):
    self.subdesc = "Nautilus integration"
    self.install_if = [self.parent, "nautilus"]
    self.depends = [self.parent, "nautilus-python"]

    return ["usr/share/nautilus-python"]
