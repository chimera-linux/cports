pkgname = "swi-prolog"
pkgver = "9.3.24"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCCACHE=OFF"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "fontconfig-devel",
    "gmp-devel",
    "libarchive-devel",
    "libjpeg-turbo-devel",
    "libunwind-devel",
    "libx11-devel",
    "libxft-devel",
    "libxinerama-devel",
    "libxpm-devel",
    "libxt-devel",
    "libyaml-devel",
    "openssl3-devel",
    "pcre2-devel",
    "readline-devel",
    "unixodbc-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Comprehensive Prolog environment"
license = "BSD-2-Clause"
url = "https://www.swi-prolog.org"
source = f"https://www.swi-prolog.org/download/devel/src/swipl-{pkgver}.tar.gz"
sha256 = "c1d570c30564a4b8db4d4bbf467c5c6c0da82664ec9ea09cd6f0415df1f505d5"
# TODO
options = ["!distlicense"]
