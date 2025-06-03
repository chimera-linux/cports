pkgname = "kakoune"
pkgver = "2025.06.03"
pkgrel = 0
build_style = "makefile"
make_install_args = ["gzip_man=no"]
make_use_env = True
checkdepends = ["git"]
pkgdesc = "Modal code editor inspired by vim"
license = "Unlicense"
url = "https://kakoune.org"
source = f"https://github.com/mawww/kakoune/releases/download/v{pkgver}/kakoune-{pkgver}.tar.bz2"
sha256 = "ced5941f1bdfb8ef6b0265b00bfd7389e392fb41b2bf11990cee9d6e95316499"
hardening = ["vis", "cfi"]
# check may be disabled
options = []

if (
    self.profile().arch in ["aarch64", "riscv64"]
    or self.profile().endian == "big"
):
    # aarch64 fails kak_selection test
    # big endian gets stuck in the suite
    options += ["!check"]
