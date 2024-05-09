pkgname = "containers-common"
pkgver = "0.58.3"
pkgrel = 0
make_cmd = "gmake"
make_build_args = ["-C", "docs"]
make_install_args = list(make_build_args)
hostmakedepends = ["gmake", "go-md2man"]
pkgdesc = "Shared docs and configs for Containers"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/containers/common"
_base_url = url.removesuffix("/common")
_common_ver = pkgver
_storage_ver = "1.53.0"
_image_ver = "5.30.1"
_skopeo_ver = "1.15.0"
_shortnames_ver = "2023.02.20"
source = [
    f"{_base_url}/common/archive/v{_common_ver}.tar.gz",
    f"{_base_url}/storage/archive/v{_storage_ver}.tar.gz",
    f"{_base_url}/image/archive/v{_image_ver}.tar.gz",
    f"{_base_url}/skopeo/archive/v{_skopeo_ver}.tar.gz",
    f"{_base_url}/shortnames/archive/v{_shortnames_ver}.tar.gz",
]
sha256 = [
    "6aafb1f00c5e5e22115abffde114da6ba42b484ac0a8fcef96a7ef09442b50b5",
    "d178e872d0ef2b9658c60a40238d2fb71588bc66e8265e998f1525983bc5166e",
    "b25f86fd0bdf69e80318afb111204225d37abf5221e01bfec3a49796c57991d2",
    "f219d31e5f3742b08a6e7327d84fd84cdcf8e5a297914bb6e19a96fef1b19b76",
    "336ba679d4e510d2eb59cb11321bf16a36ef2dba58024e79dd76b89ffee539e6",
]
# no tests
options = ["!check"]


def do_build(self):
    self.do("gmake", wrksrc=f"common-{_common_ver}/docs")
    self.do("gmake", wrksrc=f"storage-{_storage_ver}/docs")
    self.do("gmake", "docs", wrksrc=f"image-{_image_ver}")


def do_install(self):
    self.install_dir("etc/containers/certs.d")
    self.install_dir("etc/containers/oci/hooks.d")
    self.install_dir("var/lib/containers/sigstore", empty=True)

    with self.pushd(f"common-{_common_ver}"):
        self.install_file("pkg/config/containers.conf", "etc/containers")
        self.install_file("pkg/config/containers.conf", "usr/share/containers")
        self.install_file("pkg/seccomp/seccomp.json", "etc/containers")
        self.install_file("pkg/seccomp/seccomp.json", "usr/share/containers")
        self.do(
            "gmake",
            "install",
            "PREFIX=/usr",
            f"DESTDIR={self.chroot_destdir}",
            wrksrc="docs",
        )

    with self.pushd(f"storage-{_storage_ver}"):
        self.install_file("storage.conf", "etc/containers")
        self.install_file("storage.conf", "usr/share/containers")
        self.do(
            "gmake", "install", f"DESTDIR={self.chroot_destdir}", wrksrc="docs"
        )

    with self.pushd(f"image-{_image_ver}"):
        self.install_file("registries.conf", "etc/containers")
        self.do("gmake", "install", f"DESTDIR={self.chroot_destdir}")

    with self.pushd(f"shortnames-{_shortnames_ver}"):
        self.install_file(
            "shortnames.conf",
            "etc/containers/registries.conf.d",
            name="00-shortnames.conf",
        )
