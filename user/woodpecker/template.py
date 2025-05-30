pkgname = "woodpecker"
pkgver = "3.6.0"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X go.woodpecker-ci.org/woodpecker/v3/version.Version={pkgver}",
    "./cmd/agent",
    "./cmd/cli",
    "./cmd/server",
]
hostmakedepends = ["go", "pnpm"]
makedepends = ["nodejs", "libgcc-chimera"]
go_build_tags = ["noupgrade"]
pkgdesc = "Extensible CI/CD engine"
license = "Apache-2.0"
url = "https://woodpecker-ci.org"
source = f"https://github.com/woodpecker-ci/woodpecker/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "77e6cf71266b0b11a045a71da17bef27a65631a32bf717ef4f85c539101418d9"
# mock tests not built
options = ["!check"]


def post_prepare(self):
    self.do("pnpm", "install", wrksrc="web", allow_network=True)


def pre_build(self):
    self.do("pnpm", "build", wrksrc="web")


def install(self):
    self.install_bin("build/agent", name="woodpecker-agent")
    self.install_bin("build/cli", name="woodpecker-cli")
    self.install_bin("build/server", name="woodpecker-server")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "woodpecker-server")
    self.install_service(self.files_path / "woodpecker-agent")
    self.install_file(
        "nfpm/woodpecker-server.env.example",
        "etc/default",
        name="woodpecker-server",
    )
    self.install_file(
        "nfpm/woodpecker-agent.env.example",
        "etc/default",
        name="woodpecker-agent",
    )
