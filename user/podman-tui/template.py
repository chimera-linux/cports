pkgname = "podman-tui"
pkgver = "1.10.0"
pkgrel = 0
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
sha256 = "18213b021dd3d33ef5f51f83220a342a13d1287fa4b00eef35aa9e5a1de00e2b"


def post_extract(self):
    # fails on builder, works in ci
    self.rm("ui/dialogs/progress_test.go")
