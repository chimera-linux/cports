pkgname = "f2"
pkgver = "2.2.2"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/f2"]
hostmakedepends = ["go"]
checkdepends = ["perl-image-exiftool-progs"]
pkgdesc = "Command-line tool for batch renaming files and directories"
license = "MIT"
url = "https://github.com/ayoisaiah/f2"
source = f"https://github.com/ayoisaiah/f2/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0785e40b1fd2adb55165f668dc2635d47559fd7534b0f1da33849f155c4e539b"


def post_install(self):
    self.install_license("LICENCE")
    with self.pushd("scripts/completions"):
        for sh in ("bash", "fish", "zsh"):
            self.install_completion("f2." + sh, sh)
