pkgname = "f2"
pkgver = "2.2.1"
pkgrel = 2
build_style = "go"
make_build_args = ["./cmd/f2"]
hostmakedepends = ["go"]
checkdepends = ["perl-image-exiftool-progs"]
pkgdesc = "Command-line tool for batch renaming files and directories"
license = "MIT"
url = "https://github.com/ayoisaiah/f2"
source = f"https://github.com/ayoisaiah/f2/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "69e60baeb8e15644088713d7b2fb1e7d23131a92ef5fa61ed4c2c18160078ff1"


def post_install(self):
    self.install_license("LICENCE")
    with self.pushd("scripts/completions"):
        for sh in ("bash", "fish", "zsh"):
            self.install_completion("f2." + sh, sh)
