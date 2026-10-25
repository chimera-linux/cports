pkgname = "cdecl"
pkgver = "18.7.2"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["automake"]
makedepends = ["libedit-readline-devel"]
checkdepends = ["bash"]
pkgdesc = "Translate C/C++ syntax to plain English"
license = "GPL-3.0-or-later"
url = "https://github.com/paul-j-lucas/cdecl"
source = f"{url}/releases/download/cdecl-{pkgver}/cdecl-{pkgver}.tar.gz"
sha256 = "e91cc201c79456b923b45cfa779da62f5ca91824d11c545167ee7bb33a9fb810"
# fails configure with: 'config.status: linking ././fnmatch_.h to ./fnmatch.h'
options = ["!cross"]
