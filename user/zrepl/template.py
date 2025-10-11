pkgname = "zrepl"
pkgver = "1.0.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
makedepends = ["dinit-chimera"]
depends = ["zfs"]
pkgdesc = "ZFS backup and replication tool - dsh2dsh's enhanced fork"
license = "MIT"
url = "https://github.com/dsh2dsh/zrepl"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "33f5c42b423bb0c38ecab909d3a641a3218a6baae97e5c70ebf70b2b9b346017"
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
