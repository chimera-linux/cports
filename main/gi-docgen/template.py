pkgname = "gi-docgen"
pkgver = "2025.4"
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
sha256 = "66c865d459febdfb5e4078a88df06183620c3e91f726d1dc608d88ee3605526e"
