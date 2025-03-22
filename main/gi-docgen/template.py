pkgname = "gi-docgen"
pkgver = "2025.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "pkgconf",
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-jinja2",
    "python-markdown",
    "python-markupsafe",
    "python-pygments",
    "python-typogrify",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Documentation generator for GObject-based libraries"
license = "Apache-2.0 OR GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gi-docgen"
source = f"$(GNOME_SITE)/gi-docgen/{pkgver[:-2]}/gi-docgen-{pkgver}.tar.xz"
sha256 = "8a89a58bc0f77dfc3e8a2a0e3497fc39f5413ae35e5597e9ec6160abf8ee14d8"
