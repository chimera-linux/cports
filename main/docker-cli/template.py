pkgname = "docker-cli"
pkgver = "28.3.2"
pkgrel = 3
build_style = "makefile"
_commit = "ce1223035ac3ab8922717092e63a184cf67b493d"
make_build_target = "dynbinary"
hostmakedepends = [
    "bash",
    "go",
    "go-md2man",
    "pkgconf",
]
depends = ["git"]
pkgdesc = "Container and image management tool"
license = "Apache-2.0"
url = "https://docker.com"
source = f"https://github.com/docker/cli/archive/v{pkgver}.tar.gz"
sha256 = "b65cd415e63be23fcaa63107bc47a762173a06c84fb78b1575edc5443bb39867"
env = {
    "AUTO_GOPATH": "1",
    "GITCOMMIT": _commit,
    "VERSION": pkgver,
    "DISABLE_WARN_OUTSIDE_CONTAINER": "1",
}
# nah
options = ["!check"]

if self.profile().arch == "loongarch64":
    broken = "PIC linking issues"


def prepare(self):
    # figure out why this doesn't work otherwise anymore without net
    self.do("make", "manpages", allow_network=True)


def init_build(self):
    from cbuild.util import golang

    self.env["GOPATH"] = str(self.chroot_cwd)
    self.env["GOBIN"] = str(self.chroot_cwd / "bin")
    if self.profile().arch == "loongarch64":
        self.env["CGO_ENABLED"] = "0"
    else:
        self.env["CGO_ENABLED"] = "1"
    self.env.update(golang.get_go_env(self))


def pre_build(self):
    self.mkdir(self.cwd / "src/github.com/docker", parents=True)
    self.ln_s(self.chroot_cwd, self.cwd / "src/github.com/docker/cli")


def install(self):
    dbin = (self.cwd / "build/docker").resolve().name
    self.install_bin(f"build/{dbin}", name="docker")

    self.install_completion("contrib/completion/bash/docker", "bash", "docker")
    self.install_completion(
        "contrib/completion/fish/docker.fish", "fish", "docker"
    )
    self.install_completion("contrib/completion/zsh/_docker", "zsh", "docker")

    self.install_man("man/man1/docker.1")
    self.install_man("man/man1/docker-build.1")
    self.install_man("man/man1/docker-run.1")
    self.install_man("man/man5/Dockerfile.5")
    self.install_man("man/man5/docker-config-json.5")
