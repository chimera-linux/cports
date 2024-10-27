pkgname = "runc"
pkgver = "1.2.0"
pkgrel = 0
build_style = "makefile"
make_build_args = ["all", "man", f"COMMIT=chimera-r{pkgrel}"]
make_install_args = ["BINDIR=/usr/bin", "install-bash", "install-man"]
make_check_target = "localunittest"
make_use_env = True
hostmakedepends = [
    "bash",
    "go",
    "go-md2man",
    "pkgconf",
]
makedepends = [
    "libatomic-chimera-devel-static",
    "libseccomp-devel",
    "libunwind-devel-static",
    "linux-headers",
    "musl-devel-static",  # runc-dmz
]
pkgdesc = "CLI tool for spawning and running containers on Linux"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/opencontainers/runc"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "25072beb84f4adae316a968241dc74ac30982d38e4459635074aa9e9d87d3de7"
# tests create namespaces and fail because no perms
options = ["!check"]


def post_extract(self):
    # delete stray incomplete vendor dir
    self.rm("vendor/", recursive=True)


def post_prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()


def init_build(self):
    from cbuild.util import golang

    self.make_env.update(golang.get_go_env(self))
