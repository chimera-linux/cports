pkgname = "containers-common"
pkgver = "0.59.2"
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
_storage_ver = "1.54.0"
_image_ver = "5.31.1"
_skopeo_ver = "1.15.1"
_shortnames_ver = "2023.02.20"
source = [
    f"{_base_url}/common/archive/v{_common_ver}.tar.gz",
    f"{_base_url}/storage/archive/v{_storage_ver}.tar.gz",
    f"{_base_url}/image/archive/v{_image_ver}.tar.gz",
    f"{_base_url}/skopeo/archive/v{_skopeo_ver}.tar.gz",
    f"{_base_url}/shortnames/archive/v{_shortnames_ver}.tar.gz",
]
sha256 = [
    "69f6ce1752ab55b439229bbd6b9d31f0f74ab67517768d277a8e4891e2c85de2",
    "eaca427de11b7144673d643c36f1d9d277bef520ce4b7fc070c15c8b93fc1485",
    "123f0f28a7be9072bd137dc2d2adb8510d590a10adc6b1649290a9f5dfdf7de7",
    "4db9798afd45e3282f35ddad3e494db99231e84470f30d6b105a3ed687e67ee0",
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
