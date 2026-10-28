pkgname = "cgal"
pkgver = "6.2"
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
sha256 = "c91fe2e5e13df865a3fc06b0f9b83845c4e88fa243e09ee826a2d3cd774e9dca"
