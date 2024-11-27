pkgname = "runc"
pkgver = "1.2.2"
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
    "libseccomp-devel",
    "linux-headers",
]
pkgdesc = "CLI tool for spawning and running containers on Linux"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/opencontainers/runc"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "0eabc936d481d123be92c429588f9d1de7cafd36b37a8a5085b1412e758796a1"
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
