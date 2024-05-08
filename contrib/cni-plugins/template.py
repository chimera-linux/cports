pkgname = "cni-plugins"
pkgver = "1.4.1"
pkgrel = 1
hostmakedepends = ["bash", "go"]
makedepends = ["linux-headers"]
pkgdesc = "Standard CNI plugins for containers"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://www.cni.dev"
source = f"https://github.com/containernetworking/plugins/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f8e7055bc77bbd1e978157c2dcb53836f5f4d9d582f7bc2dffdd78997a267f96"
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
