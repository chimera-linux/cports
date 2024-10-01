pkgname = "cni-plugins"
pkgver = "1.5.1"
pkgrel = 6
hostmakedepends = ["bash", "go"]
makedepends = ["linux-headers"]
pkgdesc = "Standard CNI plugins for containers"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://www.cni.dev"
source = f"https://github.com/containernetworking/plugins/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a2eff5f064f809ee41f8f49ef8aed1f0a4093c0c772f2ce2caaee4e6f395050a"
# can't run tests inside namespaces
options = ["!check"]


def post_prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()


def init_build(self):
    from cbuild.util import golang

    self.make_env.update(golang.get_go_env(self))


def build(self):
    self.do(
        "bash",
        "build_linux.sh",
        "-ldflags",
        f"-X github.com/containernetworking/plugins/pkg/utils/buildversion.BuildVersion=v{pkgver}",
    )


def install(self):
    self.install_file("bin/*", "usr/libexec/cni", glob=True)
