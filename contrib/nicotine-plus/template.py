pkgname = "nicotine-plus"
pkgver = "3.3.0"
pkgrel = 0
build_style = "python_pep517"
# test_update_check: no networking + patched
# FIXME test_gui_startup: for some reason there's a sigill in python somewhere
# when ran headless (works in actual desktop)
make_check_args = ["-k", "not (test_update_check or test_gui_startup)"]
make_check_wrapper = ["dbus-run-session", "weston-headless-run"]
hostmakedepends = [
    "gettext",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "gtk4",
    "python-gobject",
]
checkdepends = [
    "dbus",
    "python-pytest",
    "weston",
] + depends
pkgdesc = "Graphical client for the Soulseek network"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://nicotine-plus.github.io/nicotine-plus"
source = (
    f"https://github.com/Nicotine-Plus/nicotine-plus/archive/{pkgver}.tar.gz"
)
sha256 = "c94bd7ecf6a107445836df80efed9b8c18cab307d812c2b91be18e93dfb4ac1f"
