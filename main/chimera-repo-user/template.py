pkgname = "chimera-repo-user"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
depends = ["chimera-repo-contrib"]
pkgdesc = "Chimera user repository"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"


def do_install(self):
    self.install_file(
        self.files_path / "01-repo-user.list", "etc/apk/repositories.d"
    )
    self.install_file(
        self.files_path / "01-repo-user-debug.list", "etc/apk/repositories.d"
    )


@subpackage("chimera-repo-user-debug")
def _dbg(self):
    self.pkgdesc = f"{pkgdesc} (debug packages)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return ["etc/apk/repositories.d/*-debug.list"]
