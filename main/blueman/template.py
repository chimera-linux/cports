pkgname = "blueman"
pkgver = "2.4.6"
pkgrel = 0
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
    "libpulse",
    "networkmanager-libs",
    "python-cairo",
    "python-gobject",
]
checkdepends = ["python-dbusmock", "python-dbus"]
pkgdesc = "GTK Bluetooth Manager"
license = "GPL-3.0-or-later"
url = "https://blueman-project.github.io/blueman"
source = f"https://github.com/blueman-project/blueman/releases/download/{pkgver}/blueman-{pkgver}.tar.xz"
sha256 = "c712a737f9855906684c074d166d4f10c7f165378af96612818bbffcfbf8e566"
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
