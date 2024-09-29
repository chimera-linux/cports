pkgname = "gnome-shell-extension-gsconnect"
pkgver = "57"
pkgrel = 1
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
    "gtk-update-icon-cache",
    "libxml2-progs",
    "meson",
    "pkgconf",
]
depends = ["evolution-data-server", "gnome-shell", "gsound", "openssl"]
checkdepends = ["dbus", "gnome-shell", "xserver-xorg-xvfb"]
pkgdesc = "KDE Connect implementation for GNOME"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://github.com/GSConnect/gnome-shell-extension-gsconnect"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6c67eb9d1e04e515f2116603577a6b775ba36373dcedd1f343a22eed753c7af5"
# All tests fail in latest release https://github.com/GSConnect/gnome-shell-extension-gsconnect/issues/1786
options = ["!check"]
