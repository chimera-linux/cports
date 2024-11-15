pkgname = "gi-docgen"
pkgver = "2024.1"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0 OR GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gi-docgen"
source = f"$(GNOME_SITE)/gi-docgen/{pkgver[:-2]}/gi-docgen-{pkgver}.tar.xz"
sha256 = "870c77f9620462cce49e35542a42dc1612fc858733e83dbbe248c535458aec1e"
