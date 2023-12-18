pkgname = "terminator"
pkgver = "2.1.3"
pkgrel = 1
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
    "python-pytest",
    "python-cairo",
    "python-gobject",
    "xserver-xorg-xvfb",
    "gobject-introspection",
    "vte-gtk3",
    "python-configobj",
    "python-psutil",
]
depends = [
    "python-psutil",
    "python-gobject",
    "gsettings-desktop-schemas",
    "libkeybinder3",
    "libnotify",
    "python-dbus",
    "python-configobj",
    "vte-gtk3",
    "pango",
]
pkgdesc = "Tiling terminal emulator application"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "GPL-2.0-only"
url = "https://gnome-terminator.org"
source = f"https://github.com/gnome-terminator/terminator/releases/download/v{pkgver}/terminator-{pkgver}.tar.gz"
sha256 = "0ae9943f3d6b72230c14bcb355de84dd81274c033e76ca4698e80d7c93cd6ae5"
hardening = ["vis"]
# testsuite fails within container and xvfb
options = ["!check"]
