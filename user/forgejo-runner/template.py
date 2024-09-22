pkgname = "forgejo-runner"
pkgver = "3.5.1"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X gitea.com/gitea/act_runner/internal/pkg/ver.version=v{pkgver}"
]
make_check_args = [
    "-skip",
    "Test_runCreateRunnerFile|Test_ping",
    "./...",
]
hostmakedepends = ["go"]
depends = ["podman"]
pkgdesc = "Daemon that runs CI jobs for Forgejo"
maintainer = "Gnarwhal <git.aspect893@passmail.net>"
license = "MIT"
url = "https://code.forgejo.org/forgejo/runner"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "0c53e5ee6ea57eadcc3ebbb4fbe203478500f78b058b13d8ccc3b63b775955c0"


def install(self):
    self.install_bin(
        f"{self.cwd}/{self.make_dir}/act_runner", name="forgejo-runner"
    )
    self.install_file(
        self.files_path / "docker_host.env", "usr/share/forgejo-runner"
    )
    self.install_service(self.files_path / "forgejo-runner")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_license("LICENSE")
