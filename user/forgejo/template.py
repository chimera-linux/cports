pkgname = "forgejo"
pkgver = "12.0.4"
pkgrel = 0
build_style = "makefile"
make_build_target = "all"
make_check_target = "test-backend"
make_use_env = True
hostmakedepends = ["go", "nodejs"]
makedepends = ["dinit-chimera", "linux-pam-devel", "sqlite-devel"]
depends = ["git", "git-lfs"]
pkgdesc = "Git forge"
license = "MIT AND GPL-3.0-or-later"
url = "https://forgejo.org"
source = f"https://codeberg.org/forgejo/forgejo/archive/v{pkgver}.tar.gz"
sha256 = "a4029f056dd69c33cd7e63925885ef0227644d61e0c992380370a5a9e295944c"
# check takes quite a bit
options = ["!check", "!cross"]

if self.profile().arch == "riscv64":
    broken = "runs out of memory on builder"


def prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()

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

    setting = "forgejo.org/modules/setting"
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
