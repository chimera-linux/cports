pkgname = "f2"
pkgver = "1.9.1"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/f2"]
hostmakedepends = ["go"]
pkgdesc = "Command-line tool for batch renaming files and directories"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "MIT"
url = "https://github.com/ayoisaiah/f2"
source = f"https://github.com/ayoisaiah/f2/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fbeb4540c4afe4aa25565685ee7ef7498449da7fc5f5b70a0e303b15c6e35f71"


def post_install(self):
    self.install_license("LICENCE")
    with self.pushd("scripts/completions"):
        for sh in ("bash", "fish", "zsh"):
            self.install_completion("f2." + sh, sh)
