pkgname = "ctags"
pkgver = "6.2.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-iconv",
    "--enable-json",
    "--enable-pcre2",
    "--enable-xml",
    "--enable-yaml",
]
make_dir = "."
hostmakedepends = ["automake", "libtool", "pkgconf", "python-docutils"]
makedepends = ["jansson-devel", "libxml2-devel", "libyaml-devel", "pcre2-devel"]
checkdepends = ["python"]
pkgdesc = "Fork of Exuberant Ctags to generate index/tag files"
license = "GPL-2.0-or-later"
url = "https://ctags.io"
source = f"https://github.com/universal-ctags/ctags/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "313c864bb19c7da79aea77b94db1bb44d14c1f88b992285d7ea8968b3cbc125f"
