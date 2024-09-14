pkgname = "terminator"
pkgver = "2.1.4"
pkgrel = 0
build_style = "python_pep517"
make_check_target = "tests"
make_check_wrapper = ["xvfb-run"]
hostmakedepends = [
    "gettext",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = [
    "gobject-introspection",
    "python-cairo",
    "python-configobj",
    "python-gobject",
    "python-psutil",
    "python-pytest",
    "vte-gtk3",
    "xserver-xorg-xvfb",
]
depends = [
    "gsettings-desktop-schemas",
    "libkeybinder3",
    "libnotify",
    "pango",
    "python-configobj",
    "python-dbus",
    "python-gobject",
    "python-psutil",
    "vte-gtk3",
]
pkgdesc = "Tiling terminal emulator application"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "GPL-2.0-only"
url = "https://gnome-terminator.org"
source = f"https://github.com/gnome-terminator/terminator/releases/download/v{pkgver}/terminator-{pkgver}.tar.gz"
sha256 = "af27b0ece862e61dde71d0827afa4a29a414e44599effe3edeebc52cbdf0c5e8"
hardening = ["vis"]
# testsuite fails within container and xvfb
options = ["!check"]
