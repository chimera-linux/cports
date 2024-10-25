pkgname = "codeberg-pages"
# important fix for wildcard certs which is not included in latest release
pkgver = "5.1_git20240802"
pkgrel = 0
_gitrev = "9524b1eb12f77fa345cc8a220f67ae244da0ab12"
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
    f"https://codeberg.org/Codeberg/pages-server/archive/{_gitrev}.tar.gz",
    "https://github.com/mattn/go-sqlite3/archive/refs/tags/v1.14.22.tar.gz",
]
source_paths = [".", "go-sqlite3-patched"]
sha256 = [
    "bec54f9ba7e61a16fb838fe8aa6ed7526d3caba4d7788c1d74093c6fe87b950d",
    "5b1d74ec4359b1ae0fe373fab37ae8a661ed128cf2f89b27875ecbb18bbe1078",
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
