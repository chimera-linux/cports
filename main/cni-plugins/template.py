pkgname = "cni-plugins"
pkgver = "1.7.1"
pkgrel = 6
hostmakedepends = ["bash", "go"]
makedepends = ["linux-headers"]
pkgdesc = "Standard CNI plugins for containers"
license = "Apache-2.0"
url = "https://www.cni.dev"
source = f"https://github.com/containernetworking/plugins/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "95b639f8ccbb714da98e331ef8813f790d447fce5417f2f8a575f3c62bfb1474"
# can't run tests inside namespaces
options = ["!check"]

# relocation errors when linking
if self.profile().arch == "loongarch64":
    env = {"CGO_ENABLED": "0"}


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
