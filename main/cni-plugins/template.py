pkgname = "cni-plugins"
pkgver = "1.6.1"
pkgrel = 0
hostmakedepends = ["bash", "go"]
makedepends = ["linux-headers"]
pkgdesc = "Standard CNI plugins for containers"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.cni.dev"
source = f"https://github.com/containernetworking/plugins/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5e2ea69bca08bfb92921f22fa2cc1e69392ee139a5878068dfbc1c7568e37b01"
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
    self.install_file("bin/*", "usr/lib/cni", glob=True)
