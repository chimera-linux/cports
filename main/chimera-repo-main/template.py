pkgname = "chimera-repo-main"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
depends = ["apk-tools", "!base-cbuild"]
pkgdesc = "Chimera base repository"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"


def do_install(self):
    self.install_file(
        self.files_path / "q66@chimera-linux.org-61a1913b.rsa.pub",
        "etc/apk/keys",
    )
    self.install_file(
        self.files_path / "00-repo-main.list", "etc/apk/repositories.d"
    )
    self.install_file(
        self.files_path / "00-repo-main-debug.list", "etc/apk/repositories.d"
    )


@subpackage("chimera-repo-main-debug")
def _dbg(self):
    self.pkgdesc = f"{pkgdesc} (debug packages)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return ["etc/apk/repositories.d/*-debug.list"]
