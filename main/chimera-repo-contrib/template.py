pkgname = "chimera-repo-contrib"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
depends = ["chimera-repo-main"]
pkgdesc = "Chimera contrib repository"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"


def do_install(self):
    self.install_file(
        self.files_path / "01-repo-contrib.list", "etc/apk/repositories.d"
    )
    self.install_file(
        self.files_path / "01-repo-contrib-debug.list", "etc/apk/repositories.d"
    )


@subpackage("chimera-repo-contrib-debug")
def _dbg(self):
    self.pkgdesc = f"{pkgdesc} (debug packages)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return ["etc/apk/repositories.d/*-debug.list"]
