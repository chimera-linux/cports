pkgname = "kakoune"
pkgver = "2024.05.18"
pkgrel = 1
build_style = "makefile"
make_install_args = ["gzip_man=no"]
make_use_env = True
checkdepends = ["git"]
pkgdesc = "Modal code editor inspired by vim"
maintainer = "superwhiskers <whiskerdev@protonmail.com>"
license = "Unlicense"
url = "https://kakoune.org"
source = f"https://github.com/mawww/kakoune/releases/download/v{pkgver}/kakoune-{pkgver}.tar.bz2"
sha256 = "dae8ac2e61d21d9bcd10145aa70b421234309a7b0bc57fad91bc34dbae0cb9fa"
hardening = ["vis", "cfi"]
# check may be disabled
options = []

if self.profile().arch == "aarch64" or self.profile().endian == "big":
    # aarch64 fails kak_selection test
    # big endian gets stuck in the suite
    options += ["!check"]
