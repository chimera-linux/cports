pkgname = "nicotine-plus"
pkgver = "3.3.6"
pkgrel = 0
build_style = "python_pep517"
# test_update_check: no networking + patched
# FIXME test_gui_startup: for some reason there's a sigill in python somewhere
# when ran headless (works in actual desktop)
make_check_args = ["-k", "not (test_update_check or test_gui_startup)"]
make_check_wrapper = [
    "dbus-run-session",
    "--",
    "wlheadless-run",
    "--",
]
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
    "xwayland-run",
    *depends,
]
pkgdesc = "Graphical client for the Soulseek network"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://nicotine-plus.github.io/nicotine-plus"
source = (
    f"https://github.com/Nicotine-Plus/nicotine-plus/archive/{pkgver}.tar.gz"
)
sha256 = "3911c178f96da1fdd48dedd98ac2d2ad6a59da388f091f91bb5722871cca91da"
