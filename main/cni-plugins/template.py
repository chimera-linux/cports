pkgname = "cni-plugins"
pkgver = "1.10.0"
pkgrel = 0
prepare_after_patch = True
hostmakedepends = ["bash", "go"]
makedepends = ["linux-headers"]
pkgdesc = "Standard CNI plugins for containers"
license = "Apache-2.0"
url = "https://www.cni.dev"
source = f"https://github.com/containernetworking/plugins/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "15a36f0a88e90704126d2d523a9704c4cab2439a4a19c9ac23961b31c2a311c6"
# can't run tests inside namespaces
options = ["!check"]

# relocation errors when linking
if self.profile.arch == "loongarch64":
    env = {"CGO_ENABLED": "0"}


def post_prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()


def build(self):
    from cbuild.util import golang

    self.do(
        "bash",
        "build_linux.sh",
        "-ldflags",
        f"-X github.com/containernetworking/plugins/pkg/utils/buildversion.BuildVersion=v{pkgver}",
        env=golang.get_go_env(self),
    )


def install(self):
    self.install_file("bin/*", "usr/lib/cni", glob=True)
