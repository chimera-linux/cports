pkgname = "codeberg-pages"
pkgver = "5.1"
pkgrel = 0
build_style = "go"
hostmakedepends = [
    "go",
]
makedepends = [
    "sqlite-devel",
]
pkgdesc = "Serve static pages from Gitea/Forgejo repositories"
maintainer = "Gnarwhal <git.aspect893@passmail.net>"
license = "EUPL-1.2"
url = "https://docs.codeberg.org/codeberg-pages"
source = [
    "https://codeberg.org/Codeberg/pages-server/archive/03881382a4c286e3a7dc351f095f9147e89c2d6d.tar.gz",
    "https://github.com/mattn/go-sqlite3/archive/refs/tags/v1.14.22.tar.gz",
]
source_paths = [".", "go-sqlite3-patched"]
sha256 = [
    "23b2bcff621d16c70d6d9a4a59c7b0903d40236e9470e5c9864bb41693a2414b",
    "5b1d74ec4359b1ae0fe373fab37ae8a661ed128cf2f89b27875ecbb18bbe1078",
]


def post_extract(self):
    # Test depends on a network connection
    self.rm(self.srcdir / "server/handler/handler_test.go")


def do_prepare(self):
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


def init_build(self):
    from cbuild.util import golang

    self.make_env.update(golang.get_go_env(self))
    self.make_env["EXTRA_GOFLAGS"] = f"{self.get_goflags(shell=True)} -trimpath"
    # https://github.com/golang/go/issues/64875
    self.make_env["CGO_ENABLED"] = "1"
    self.make_env["TAGS"] = "libsqlite3 sqlite sqlite_unlock_notify"


def post_install(self):
    self.install_bin("build/pages", name="codeberg-pages")
    self.install_license("LICENSE")

    self.install_file(self.files_path / "config.env", "etc/codeberg-pages")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "codeberg-pages")
