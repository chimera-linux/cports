pkgname = "plotinus"
pkgver = "0.2.0"
pkgrel = 0
build_style = "cmake"
# Vendored dependency
cmake_dir = "unityx/plotinus"
hostmakedepends = ["cmake", "ninja", "pkgconf", "vala"]
makedepends = ["gtk+3-devel"]
pkgdesc = "Searchable command palette in every modern GTK+ application"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/p-e-w/plotinus"
source = "https://gitlab.com/ubuntu-unity/unity-x/unityx/-/archive/main/unityx-main.tar.gz?path=unityx/plotinus>plotinus.tgz"
sha256 = "22c131b1dce41e5b648a8b9263e15453515ba2141393ebc321a9d1ad1feda3f4"
hardening = ["vis", "cfi"]
# No tests
options = ["!check"]
