pkgname = "cgal"
pkgver = "6.1.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
]
pkgdesc = "Computational Geometry Algorithms Library"
license = "GPL-3.0-or-later AND LGPL-3.0-or-later"
url = "https://www.cgal.org"
source = f"https://github.com/CGAL/cgal/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d798163dd5a85a15a971fd50d55a5700d64cef473637e1839078e9463b1f6b53"
