pkgname = "codeberg-pages"
pkgver = "6.0"
pkgrel = 0
build_style = "go"
make_check_args = [
    "-skip",
    # Requires network connection
    "TestHandlerPerformance",
]
hostmakedepends = [
    "go",
]
makedepends = [
    "sqlite-devel",
]
go_build_tags = [
    "libsqlite3",
    "sqlite",
    "sqlite_unlock_notify",
]
pkgdesc = "Serve static pages from Gitea/Forgejo repositories"
maintainer = "Gnarwhal <git.aspect893@passmail.net>"
license = "EUPL-1.2"
url = "https://docs.codeberg.org/codeberg-pages"
source = [
    f"https://codeberg.org/Codeberg/pages-server/archive/v{pkgver}.tar.gz",
    "https://github.com/mattn/go-sqlite3/archive/refs/tags/v1.14.24.tar.gz",
]
source_paths = [".", "go-sqlite3-patched"]
sha256 = [
    "2bdb2943db86338fdfcb452fbb6d84e7a4ad05712492dd564d4e5c84a4c8d750",
    "8fa3b0b66914ae2dd4ddef9a954f614c5b3eb6ac9d80ee61ae2d08e3178507ec",
]
env = {
    # https://github.com/golang/go/issues/64875
    "CGO_ENABLED": "1",
}


def prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()

    # Replace the go dep
    self.do(
        "go",
        "mod",
        "edit",
        "-replace",
        f"github.com/mattn/go-sqlite3@v1.14.16={self.chroot_srcdir / 'go-sqlite3-patched'}",
    )


def post_install(self):
    self.install_bin("build/pages", name="codeberg-pages")
    self.install_license("LICENSE")

    self.install_file(self.files_path / "config.env", "etc/codeberg-pages")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "codeberg-pages")
