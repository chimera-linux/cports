pkgname = "cdecl"
pkgver = "18.7.2"
pkgrel = 0
pkgdesc = (
    "Composing and deciphering C/C++ declarations or casts, aka ‘‘gibberish’’"
)
license = "GPL-3.0-only"
url = "https://github.com/paul-j-lucas/cdecl"
source = f"{url}/releases/download/cdecl-{pkgver}/cdecl-{pkgver}.tar.gz"
sha256 = "e91cc201c79456b923b45cfa779da62f5ca91824d11c545167ee7bb33a9fb810"

build_style = "gnu_configure"

configure_gen = ["./bootstrap"]
hostmakedepends = ["automake", "byacc", "flex", "readline-devel"]
options = ["!check"]
