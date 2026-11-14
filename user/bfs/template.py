pkgname = "bfs"
pkgver = "4.1.6"
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
sha256 = "5b706e1b362c1f05093e1436b396fc8129c6e456a112b9e4a06fd7916f19baaf"
hardening = ["cfi", "vis"]
