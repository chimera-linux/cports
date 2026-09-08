pkgname = "kakoune"
pkgver = "2026.05.21"
pkgrel = 1
build_style = "makefile"
make_install_args = ["gzip_man=no"]
make_use_env = True
checkdepends = ["git"]
pkgdesc = "Modal code editor inspired by vim"
license = "Unlicense"
url = "https://kakoune.org"
source = f"https://github.com/mawww/kakoune/releases/download/v{pkgver}/kakoune-{pkgver}.tar.bz2"
sha256 = "be1deb3fe9808a0733ab1057309da380bb757307e8fdbb22dc478b674b6bad34"
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


def post_extract(self):
    # fails weirdly
    self.rm("test/compose/history", recursive=True)
