pkgname = "r"
pkgver = "4.5.1"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = [
    "file",
    "gcc-fortran",
    "perl",
    "pkgconf",
]
makedepends = [
    "bzip2-devel",
    "cairo-devel",
    "curl-devel",
    "icu-devel",
    "libdeflate-devel",
    "libjpeg-turbo-devel",
    "libtiff-devel",
    "libx11-devel",
    "libxt-devel",
    "pcre2-devel",
    "readline-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Statistical computing environment"
license = "GPL-2.0-or-later"
url = "https://www.r-project.org"
source = f"https://cran.r-project.org/src/base/R-{pkgver.split('.')[0]}/R-{pkgver}.tar.gz"
sha256 = "b42a7921400386645b10105b91c68728787db5c4c83c9f6c30acdce632e1bb70"
# int: traps in aarch64 ci
hardening = ["!int"]
# cross: unsupported by upstream
# lto: gfortran does not like the flag
options = ["!cross", "!lto"]
