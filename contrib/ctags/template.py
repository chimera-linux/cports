pkgname = "ctags"
pkgver = "6.1.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-iconv",
    "--enable-json",
    "--enable-pcre2",
    "--enable-xml",
    "--enable-yaml",
]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["automake", "gmake", "libtool", "pkgconf", "python-docutils"]
makedepends = ["jansson-devel", "libxml2-devel", "libyaml-devel", "pcre2-devel"]
checkdepends = ["python"]
pkgdesc = "Fork of Exuberant Ctags to generate index/tag files"
maintainer = "Renato Botelho do Couto <renato@netgate.com>"
license = "GPL-2.0-or-later"
url = "https://ctags.io"
source = f"https://github.com/universal-ctags/ctags/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1eb6d46d4c4cace62d230e7700033b8db9ad3d654f2d4564e87f517d4b652a53"
