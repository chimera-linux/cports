pkgname = "podman-tui"
pkgver = "1.2.3"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
makedepends = [
    "libbtrfs-devel",
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
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/containers/podman-tui"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ce13ff135187463820360c89c853bdc98d219e1f856c66eb4c96be9caa0ffefc"
