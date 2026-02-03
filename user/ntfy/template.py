pkgname = "ntfy"
pkgver = "2.16.0"
pkgrel = 0
build_style = "go"
make_env = {"CGO_ENABLED": "1"}
make_build_args = [
    "-ldflags=-s"
    + f" -X main.version={pkgver}"
    + " -X main.commit=release"
    + " -X main.date= ",
]
make_check_args = [
    "./client/...",
    "./log/...",
    "./server/...",
    "./user/...",
    "./util/...",
]
hostmakedepends = ["go", "nodejs"]
makedepends = ["dinit-chimera", "sqlite-devel"]
go_build_tags = [
    "netgo",
    "nopayments",
    "nofirebase",
    "osusergo",
    "sqlite_omit_load_extension",
]
pkgdesc = "UnifiedPush distributor supporting push notifications"
license = "Apache-2.0 AND GPL-2.0-only"
url = "https://ntfy.sh"
source = (
    f"https://github.com/binwiederhier/ntfy/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "b564e16166711a319a21cb5711e2d000ba0332454c2af8aaa168b2b5e77ea8de"
options = ["!cross"]


def prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()

    self.do("npm", "ci", wrksrc="web", allow_network=True)
    self.do("npm", "run", "build", wrksrc="web")
    self.mv("web/build/index.html", "web/build/app.html")
    self.rm("server/site", recursive=True, force=True)
    self.mv("web/build", "server/site")
    self.rm("server/site/config.js")


def init_build(self):
    self.mkdir("server/docs", parents=True)
    self.do("touch", "server/docs/index.html")
    self.do("touch", "server/site/app.html")


def post_install(self):
    self.install_service(self.files_path / "ntfy")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
