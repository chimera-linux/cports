pkgname = "kakoune"
pkgver = "2024.05.09"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_install_args = ["gzip_man=no"]
make_use_env = True
hostmakedepends = ["gmake"]
pkgdesc = "Modal code editor inspired by vim"
maintainer = "superwhiskers <whiskerdev@protonmail.com>"
license = "Unlicense"
url = "https://kakoune.org"
source = f"https://github.com/mawww/kakoune/releases/download/v{pkgver}/kakoune-{pkgver}.tar.bz2"
sha256 = "2190bddfd3af590c0593c38537088976547506f47bd6eb6c0e22350dbd16a229"
hardening = ["vis", "cfi"]
