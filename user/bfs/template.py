pkgname = "bfs"
pkgver = "4.0.8"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--enable-release",
    "--with-libacl",
    "--with-libcap",
    "--with-liburing",
    "--with-oniguruma",
]
# the integration-tests fail to run with cbuild
make_check_target = "unit-tests"
hostmakedepends = ["pkgconf"]
makedepends = ["acl-devel", "libcap-devel", "liburing-devel", "oniguruma-devel"]
checkdepends = ["bash"]
pkgdesc = "Breadth-first version of the UNIX find command"
license = "0BSD"
url = "https://github.com/tavianator/bfs"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0b7bc99fca38baf2ce212b0f6b03f05cd614ea0504bc6360e901d6f718180036"
hardening = ["cfi", "vis"]
