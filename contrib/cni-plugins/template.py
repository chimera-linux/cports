pkgname = "cni-plugins"
pkgver = "1.4.0"
pkgrel = 0
hostmakedepends = ["bash", "go"]
makedepends = ["linux-headers"]
pkgdesc = "Standard CNI plugins for containers"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://www.cni.dev"
source = f"https://github.com/containernetworking/plugins/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "890e00a8ffc71c860e4f09ab4e1c452d85ec18cc4ac8ee3da11bbfc113355f5e"
# objcopy fails on ppc
# can't run tests inside namespaces
options = ["!debug", "!check"]


def post_prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()


def init_build(self):
    from cbuild.util import golang

    self.make_env.update(golang.get_go_env(self))


def do_build(self):
    self.do(
        "bash",
        "build_linux.sh",
        "-ldflags",
        f"-X github.com/containernetworking/plugins/pkg/utils/buildversion.BuildVersion=v{pkgver}",
    )


def do_install(self):
    self.install_file("bin/*", "usr/libexec/cni", glob=True)
