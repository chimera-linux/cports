pkgname = "forgejo"
pkgver = "9.0.1"
pkgrel = 1
build_style = "makefile"
make_build_target = "all"
make_check_target = "test-backend"
make_use_env = True
hostmakedepends = ["go", "nodejs"]
makedepends = ["linux-pam-devel", "sqlite-devel"]
depends = ["git", "git-lfs"]
pkgdesc = "Git forge"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT AND GPL-3.0-or-later"
url = "https://forgejo.org"
source = [
    f"https://codeberg.org/forgejo/forgejo/archive/v{pkgver}.tar.gz",
    "https://github.com/mattn/go-sqlite3/archive/refs/tags/v1.14.24.tar.gz",
]
source_paths = [".", "go-sqlite3-patched"]
sha256 = [
    "e31448dbf5ca0f6fcd0084991bd52eb1e2b39e8fc117512bb2e375d40e341201",
    "8fa3b0b66914ae2dd4ddef9a954f614c5b3eb6ac9d80ee61ae2d08e3178507ec",
]
# check takes quite a bit
options = ["!check", "!cross"]


if self.profile().arch == "riscv64":
    broken = "npx stuck forever in build env"


def prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()

    # replace the go dep
    self.do(
        "go",
        "mod",
        "edit",
        "-replace",
        f"github.com/mattn/go-sqlite3@v1.14.22={self.chroot_srcdir / 'go-sqlite3-patched'}",
    )

    self.log("installing npm dependencies...")
    self.do("npm", "ci", allow_network=True)


def init_build(self):
    from cbuild.util import golang

    self.make_env.update(golang.get_go_env(self))
    self.make_env["EXTRA_GOFLAGS"] = f"{self.get_goflags(shell=True)} -trimpath"
    # https://github.com/golang/go/issues/64875
    self.make_env["CGO_ENABLED"] = "1"
    self.make_env["GITEA_VERSION"] = pkgver
    self.make_env["TAGS"] = "bindata libsqlite3 sqlite sqlite_unlock_notify pam"

    setting = "code.gitea.io/gitea/modules/setting"
    self.make_env["LDFLAGS"] = (
        f"-X '{setting}.AppWorkPath=/var/lib/forgejo/' -X '{setting}.CustomConf=/etc/forgejo/app.ini' -linkmode=external"
    )


def install(self):
    self.install_bin("gitea", name="forgejo")
    self.install_license("LICENSE")

    self.install_file(
        "custom/conf/app.example.ini", "usr/share/examples/forgejo"
    )
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "forgejo")
