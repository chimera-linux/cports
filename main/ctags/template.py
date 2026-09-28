pkgname = "ctags"
pkgver = "6.2.1"
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
sha256 = "f56829e9a576025e98955597ee967099a871987b3476fbd8dbbc2b9dc921f824"
