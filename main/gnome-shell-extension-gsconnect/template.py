pkgname = "gnome-shell-extension-gsconnect"
pkgver = "67"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dinstalled_tests=false"]
# Would've used weston-headless-run here instead of xvfb-run, but that runs
# into a gtk3 bug in one of the tests:
# https://github.com/chimera-linux/cports/pull/1223#issue-2079623168
make_check_wrapper = ["dbus-run-session", "xvfb-run"]
hostmakedepends = [
    "bash",
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gtk+3-update-icon-cache",
    "libxml2-progs",
    "meson",
    "pkgconf",
]
makedepends = ["dbus-devel"]
depends = ["evolution-data-server", "gnome-shell", "gsound", "openssl3"]
checkdepends = ["dbus", "gnome-shell", "xserver-xorg-xvfb"]
pkgdesc = "KDE Connect implementation for GNOME"
license = "GPL-2.0-or-later"
url = "https://github.com/GSConnect/gnome-shell-extension-gsconnect"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "99d7e098f88611c566dea95fd9b9221bcec72e3174bf1aee7d67ba40be423603"
# All tests fail in latest release https://github.com/GSConnect/gnome-shell-extension-gsconnect/issues/1786
options = ["!check"]
