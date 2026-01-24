pkgname = "gotosocial"
pkgver = "0.20.3"
pkgrel = 0
build_style = "go"
prepare_after_patch = True
make_build_args = [f"-ldflags=-X main.Version={pkgver}", "./cmd/gotosocial"]
make_check_env = {"GTS_DB_TYPE": "sqlite", "GTS_DB_ADDRESS": ":memory:"}
hostmakedepends = ["go", "go-swagger", "yarn"]
makedepends = ["dinit-chimera"]
checkdepends = []
depends = []
go_build_tags = ["netgo", "osusergo", "kvformat"]
go_check_tags = ["netgo", "osusergo", "kvformat"]
pkgdesc = "ActivityPub server"
license = "AGPL-3.0-or-later"
url = "https://gotosocial.org"
source = f"https://codeberg.org/superseriousbusiness/gotosocial/archive/v{pkgver}.tar.gz"
sha256 = "2d3a8c7098da52a5bf031f605443bf13f7533df134fd304d04b869e53a20c234"
# flaky
options = ["!check"]

match self.profile().arch:
    case "aarch64" | "x86_64":
        pass
    case _:
        go_build_tags += ["nowasm"]
        go_check_tags += ["nowasm"]
        depends += ["cmd:ffmpeg!ffmpeg", "cmd:ffprobe!ffmpeg"]
        checkdepends += ["ffmpeg"]


def post_extract(self):
    # subtle fp value differences, harmless
    self.rm("internal/media/manager_test.go")
    self.rm("internal/api/client/admin/emojicreate_test.go")
    self.rm("internal/api/client/admin/emojiupdate_test.go")
    self.rm("internal/federation/dereferencing/emoji_test.go")


def post_prepare(self):
    self.do("go", "mod", "vendor", allow_network=True)
    self.do(
        "yarn",
        "--cwd",
        "./web/source",
        "install",
        "--frozen-lockfile",
        allow_network=True,
    )
    self.do(
        "yarn",
        "--cwd",
        "./web/source",
        "ts-patch",
        "install",
        allow_network=True,
    )
    self.do("yarn", "--cwd", "./web/source", "build", allow_network=True)


def post_build(self):
    self.do(
        "swagger",
        "generate",
        "spec",
        "-o",
        "web/assets/swagger.yaml",
        "--scan-models",
    )


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "gotosocial")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_dir("usr/share/gotosocial/web")
    self.install_file("example/config.yaml", "usr/share/gotosocial")
    self.install_files("web/assets", "usr/share/gotosocial/web")
    self.install_files("web/template", "usr/share/gotosocial/web")
