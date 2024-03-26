pkgname = "gnome-shell-extension-gsconnect"
pkgver = "56"
pkgrel = 1
# XXX drop after next release
_commit = "43594cc23826fdc6b17acd04b67b34338acf78d4"
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
# source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "bcce8a391b4f18a5d94d250af923f7ecec203a81a1d0a71c8527005dccaad856"
