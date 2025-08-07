pkgname = "podman-tui"
pkgver = "1.5.0"
pkgrel = 3
build_style = "go"
hostmakedepends = ["go"]
makedepends = [
    "btrfs-progs-devel",
    "linux-headers",
    "sqlite-devel",
]
checkdepends = [
    "gpgme-devel",
    "pkgconf",
]
go_build_tags = [
    "btrfs_noversion",
    "containers_image_openpgp",
    "exclude_graphdriver_btrfs",
    "exclude_graphdriver_devicemapper",
    "libsqlite3",
    "remote",
]
go_check_tags = [*go_build_tags]
pkgdesc = "Podman terminal UI"
license = "Apache-2.0"
url = "https://github.com/containers/podman-tui"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d9ba16d37f959d7ae5ca6650c3ccc7b0e1a726215791c99604f8f5955ee8f61d"


def post_extract(self):
    # fails on builder, works in ci
    self.rm("ui/dialogs/progress_test.go")
