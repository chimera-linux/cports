pkgname = "bubblejail"
pkgver = "0.8.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dbytecode-optimization=0",
    "-Duse_python_site_packages_dir=true",
]
hostmakedepends = [
    "desktop-file-utils",
    "meson",
    "pkgconf",
]
makedepends = [
    "libseccomp-devel",
    "python-jinja2",
    "python-pyxdg",
    "python-tomli-w",
]
depends = [
    "libseccomp",
    "python-jinja2",
    "python-pyqt6",
    "python-pyxdg",
    "python-tomli-w",
    "xdg-dbus-proxy",
]
pkgdesc = "Bubblewrap based sandboxing for desktop applications"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/igo95862/bubblejail"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "ad52d0819384a50de8ed59d991f25350c9b13a807549772f7cfda1097e4b98ca"
