pkgname = "gotify"
pkgver = "2.5.0"
pkgrel = 0
build_style = "go"
make_build_args = ["-ldflags", f"-X main.Version={pkgver} -X main.Mode=prod"]
hostmakedepends = ["go", "yarn"]
makedepends = ["sqlite-devel"]
go_build_tags = ["libsqlite3"]
go_check_tags = ["libsqlite3"]
pkgdesc = "Server for sending and receiving real-time messages"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT AND CC-BY-4.0"
url = "https://gotify.net"
source = f"https://github.com/gotify/server/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "209eb48ac233ff8d9d67b405c4063cb5a33612688e1e8183ebade2128c69c798"


def post_prepare(self):
    self.do("yarn", allow_network=True, wrksrc="ui")


def pre_build(self):
    self.do(
        "yarn",
        "build",
        "--offline",
        wrksrc="ui",
        env={"NODE_OPTIONS": "--openssl-legacy-provider"},
    )


def install(self):
    self.install_license("LICENSE")
    self.install_bin("build/server", name="gotify-server")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "gotify")
    self.install_file("config.example.yml", "etc/gotify", name="config.yml")
