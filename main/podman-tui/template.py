pkgname = "podman-tui"
pkgver = "1.2.2"
pkgrel = 1
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
sha256 = "97243e025bf8a0ad4b7e87197cc4e608da0af8bb447b1ffd0e01bcb58273b619"
