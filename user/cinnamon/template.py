# Update cinnamon-schemas when bumping
pkgname = "cinnamon"
pkgver = "6.2.9"
pkgrel = 0
build_style = "meson"
# XXX: drop libexec
configure_args = ["--libexecdir=/usr/lib", "-Ddefault_library=shared"]
hostmakedepends = [
    "gobject-introspection",
    "intltool",
    "meson",
    "pkgconf",
]
makedepends = [
    "at-spi2-core-devel",
    "cinnamon-menus-devel",
    "cjs-devel",
    "dbus-devel",
    "glib-devel",
    "gstreamer-devel",
    "gtk+3-devel",
    "libx11-devel",
    "libxml2-devel",
    "mesa-devel",
    "muffin-devel",
    "networkmanager-devel",
    "polkit-devel",
    "xapp-devel",
]
depends = [
    "accountsservice",
    "bash",
    "cinnamon-control-center",
    "cinnamon-desktop",
    "cinnamon-menus",
    "cinnamon-schemas",
    "cinnamon-screensaver",
    "cinnamon-session",
    "evolution-data-server",
    "glib",
    "gsound",
    "gtk+3",
    "libical",
    "libkeybinder3",
    "libnotify",
    "libtimezonemap",
    "nemo",
    "network-manager-applet",
    "openrc-settingsd",
    "python-cairo",
    "python-dbus",
    "python-gobject",
    "python-pam",
    "python-pexpect",
    "python-pillow",
    "python-psutil",
    "python-pytz",
    "python-requests",
    "python-setproctitle",
    "python-tinycss2",
    "python-xapp",
    "touchegg",
    "upower-libs",
    "xapp",
]
pkgdesc = "Linux desktop that provides a traditional user experience"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://projects.linuxmint.com/cinnamon"
source = (
    f"https://github.com/linuxmint/cinnamon/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "a0b15b98a899532d531689ea11ff6805a87fcf5994e238322b6c916bf8c29919"
broken_symlinks = ["etc/xdg/menus/cinnamon-applications-merged"]
# meson.build: tests are not currently functional
options = ["!check", "!cross"]


def post_install(self):
    # Schema files are provided by cinnamon-schemas
    self.uninstall("usr/share/glib-2.0")


@subpackage("cinnamon-meta")
def _(self):
    self.subdesc = "recommends package"
    self.install_if = [self.parent]
    self.depends = ["gnome-terminal", "slick-greeter", "xapp-apps"]
    self.options = ["empty"]

    return []
