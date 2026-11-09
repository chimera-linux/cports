pkgname = "zrepl"
pkgver = "1.4.3"
pkgrel = 0
build_style = "go"
prepare_after_patch = True
make_build_args = [
    f"-ldflags=-X github.com/dsh2dsh/zrepl/internal/version.zreplVersion={pkgver}"
]
hostmakedepends = ["go"]
makedepends = ["dinit-chimera"]
depends = ["zfs"]
pkgdesc = "ZFS backup and replication tool - dsh2dsh's enhanced fork"
license = "MIT"
url = "https://github.com/dsh2dsh/zrepl"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "86a6161e70ba51ac8106ce0defc45fe0ee247193eb4483eb04cb22f61d2b59fd"
# check: needs to run zfs command
# cross: generates completions with built binary
options = ["!check", "!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"zrepl.{shell}", "w") as cf:
            self.do(
                "build/zrepl",
                "completion",
                shell,
                stdout=cf,
            )


def install(self):
    self.install_bin("build/zrepl")
    self.install_files(
        "internal/config/samples", "usr/share/examples", name="zrepl"
    )
    self.install_file(
        "dist/freebsd/etc/zrepl/zrepl.yml", "usr/share/examples/zrepl"
    )
    self.install_service(self.files_path / "zrepl")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_license("LICENSE")

    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"zrepl.{shell}", shell)
