pkgname = "kakoune"
pkgver = "2023.08.05"
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
sha256 = "3e45151e0addd3500de2d6a29b5aacf2267c42bb256d44a782e73defb29cda5c"
hardening = ["vis", "cfi"]
