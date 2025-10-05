pkgname = "f2"
pkgver = "2.0.3"
pkgrel = 9
build_style = "go"
make_build_args = ["./cmd/f2"]
hostmakedepends = ["go"]
checkdepends = ["perl-image-exiftool-progs"]
pkgdesc = "Command-line tool for batch renaming files and directories"
license = "MIT"
url = "https://github.com/ayoisaiah/f2"
source = f"https://github.com/ayoisaiah/f2/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "164e1282ae1f2ea6a8af93c785d7bb214b09919ad8537b8fbab5b5bc8ee1a396"


def post_install(self):
    self.install_license("LICENCE")
    with self.pushd("scripts/completions"):
        for sh in ("bash", "fish", "zsh"):
            self.install_completion("f2." + sh, sh)
