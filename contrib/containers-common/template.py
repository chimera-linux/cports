pkgname = "containers-common"
pkgver = "0.57.2"
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
_storage_ver = "1.51.0"
_image_ver = "5.29.1"
_skopeo_ver = "1.14.1"
_shortnames_ver = "2023.02.20"
source = [
    f"{_base_url}/common/archive/v{_common_ver}.tar.gz",
    f"{_base_url}/storage/archive/v{_storage_ver}.tar.gz",
    f"{_base_url}/image/archive/v{_image_ver}.tar.gz",
    f"{_base_url}/skopeo/archive/v{_skopeo_ver}.tar.gz",
    f"{_base_url}/shortnames/archive/v{_shortnames_ver}.tar.gz",
]
sha256 = [
    "d5afaa60bb216c37a45f53a2c1cc297700c9926846902e52144ca6f20ba93ede",
    "383bf3d7ef5eec3afee20ae37ca0caf8f2c2ef0ec14104cba2476f73db571c5e",
    "0db7a7b5e866a3ffafb080de158d990ab445b6dfdbb28228964dddc49edeb2fb",
    "b174ada87751ecd7f8e0e292d163c9b0c4a2172a6ba32e1725ae272c24f7f841",
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

    with self.pushd(f"skopeo-{_skopeo_ver}"):
        self.install_file(
            "default-policy.json", "etc/containers", name="policy.json"
        )
        self.install_file("default.yaml", "etc/containers/registries.d")

    with self.pushd(f"shortnames-{_shortnames_ver}"):
        self.install_file(
            "shortnames.conf",
            "etc/containers/registries.conf.d",
            name="00-shortnames.conf",
        )
