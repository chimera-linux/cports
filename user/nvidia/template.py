pkgname = "nvidia"
pkgver = "560.35.03"
pkgrel = 0
archs = ["x86_64"]
hostmakedepends = ["gcompat", "patchelf"]
depends = [
    # linked to
    "libgcc-chimera",
    "gcompat",
    "openssl",

    # executed when used
    "nvidia-modprobe",

    # used in egl icd
    "nvidia-settings",

    # needed to be functional
    "egl-gbm",
    "egl-wayland",
    "libglvnd",
]
pkgdesc = "NVIDIA accelerated graphics driver"
maintainer = "mizz1e <158266562+mizz1e@users.noreply.github.com>"
license = "custom:nvidia"
url = "https://www.nvidia.com/download/index.aspx"
source = f"https://download.nvidia.com/XFree86/Linux-x86_64/{pkgver}/NVIDIA-Linux-x86_64-{pkgver}.run"
sha256 = "f2932c92fadd43c5b2341be453fc4f73f0ad7185c26bb7a43fbde81ae29f1fe3"
hardening = ["!pie"]
# there is nothing to check
options = ["!check", "!cross"]

restricted = "work in progress, patches binaries, requires ldso help"

# all of this should really just be parsed out of .manifest
_dir = f"NVIDIA-Linux-x86_64-{pkgver}"

_libs = [
    f"libEGL.so.{pkgver}",
    f"libEGL_nvidia.so.{pkgver}",
    f"libGLESv1_CM_nvidia.so.{pkgver}",
    f"libGLESv2_nvidia.so.{pkgver}",
    f"libGLX_nvidia.so.{pkgver}",
    f"libglxserver_nvidia.so.{pkgver}",
    f"libcuda.so.{pkgver}",
    f"libcudadebugger.so.{pkgver}",
    f"libnvcuvid.so.{pkgver}",
    f"libnvidia-allocator.so.{pkgver}",
    "libnvidia-api.so.1",
    f"libnvidia-cfg.so.{pkgver}",
    "libnvidia-egl-xcb.so.1",
    "libnvidia-egl-xlib.so.1",
    f"libnvidia-eglcore.so.{pkgver}",
    f"libnvidia-encode.so.{pkgver}",
    f"libnvidia-fbc.so.{pkgver}",
    f"libnvidia-glcore.so.{pkgver}",
    f"libnvidia-glsi.so.{pkgver}",
    f"libnvidia-glvkspirv.so.{pkgver}",
    f"libnvidia-gpucomp.so.{pkgver}",
    f"libnvidia-ml.so.{pkgver}",
    f"libnvidia-ngx.so.{pkgver}",
    f"libnvidia-nvvm.so.{pkgver}",
    f"libnvidia-opencl.so.{pkgver}",
    f"libnvidia-opticalflow.so.{pkgver}",
    f"libnvidia-pkcs11-openssl3.so.{pkgver}",
    f"libnvidia-ptxjitcompiler.so.{pkgver}",
    f"libnvidia-rtcore.so.{pkgver}",
    f"libnvidia-tls.so.{pkgver}",
    f"libnvidia-vksc-core.so.{pkgver}",
    f"libnvoptix.so.{pkgver}",
    f"libvdpau_nvidia.so.{pkgver}",
]

_bins = ["nvidia-smi"]

def do_extract(self):
    self.do("sh", self.chroot_sources_path / f"{_dir}.run", "--extract-only")

def _patch(step, lib):
    stdout = step.do("patchelf", "--print-needed", lib, capture_output=True).stdout

    if not stdout:
        return

    patchelf = ["patchelf", lib]
    name = str(lib.name)

    for dep in stdout.splitlines():
        dep = dep.decode()

        match dep:
            case "ld-linux-x86-64.so.2" | "libdl.so.2" | "libm.so.6" | "libpthread.so.0" | "librt.so.1":
                patchelf.extend(["--remove-needed", dep])
            case "libc.so.6":
                patchelf.extend(["--replace-needed", dep, "libgcompat.so.0"])
            case "libcrypto.so.1.1":
                patchelf.extend(["--replace-needed", dep, "libcrypto.so"])

    print(patchelf)

    step.do(*patchelf)

def do_build(self):
    for path in (*_bins, *_libs):
        _patch(self, (self.cwd / _dir / path).relative_to(self.cwd))

def do_install(self):
    # again, parse from manifest
    with self.pushd(self.cwd / _dir):
        for lib in _libs:
            self.install_lib(lib)

        for bin in _bins:
            self.install_bin(bin)

        self.install_file("10_nvidia.json", "usr/share/glvnd/egl_vendor.d")
        self.install_file("nvidia_icd.json", "usr/share/vulkan/icd.d")
        self.install_file("nvidia_layers.json", "usr/share/vulkan/implicit_layer.d")

    self.install_link("usr/lib/libEGL_nvidia.so.0", f"libEGL_nvidia.so.{pkgver}")
    self.install_link("usr/lib/libGLESv1_CM_nvidia.so.1", f"libGLESv1_CM_nvidia.so.{pkgver}")
    self.install_link("usr/lib/libGLESv2_nvidia.so.2", f"libGLESv2_nvidia.so.{pkgver}")
    self.install_link("usr/lib/libGLX_nvidia.so.0", f"libGLX_nvidia.so.{pkgver}")

    self.install_link("usr/lib/libcuda.so.1", f"libcuda.so.{pkgver}")
    self.install_link("usr/lib/libcuda.so", f"libcuda.so.1")

    self.install_link("usr/lib/libcudadebugger.so.1", f"libcudadebugger.so.{pkgver}")

    self.install_link("usr/lib/libnvcuvid.so.1", f"libnvcuvid.so.{pkgver}")
    self.install_link("usr/lib/libnvcuvid.so", f"libnvcuvid.so.1")

    self.install_link("usr/lib/libnvidia-allocator.so.1", f"libnvidia-allocator.so.{pkgver}")
    self.install_link("usr/lib/libnvidia-allocator.so", f"libnvidia-allocator.so.1")

    self.install_link("usr/lib/libnvidia-cfg.so.1", f"libnvidia-cfg.so.{pkgver}")
    self.install_link("usr/lib/libnvidia-cfg.so", f"libnvidia-cfg.so.1")

    self.install_link("usr/lib/libnvidia-encode.so.1", f"libnvidia-encode.so.{pkgver}")
    self.install_link("usr/lib/libnvidia-encode.so", f"libnvidia-encode.so.1")

    self.install_link("usr/lib/libnvidia-ml.so.1", f"libnvidia-ml.so.{pkgver}")
    self.install_link("usr/lib/libnvidia-ml.so", f"libnvidia-ml.so.1")

    self.install_link("usr/lib/libnvidia-ngx.so.1", f"libnvidia-ngx.so.{pkgver}")

    self.install_link("usr/lib/libnvidia-nvvm.so.1", f"libnvidia-nvvm.so.{pkgver}")
    self.install_link("usr/lib/libnvidia-nvvm.so", f"libnvidia-nvvm.so.1")

    self.install_link("usr/lib/libnvidia-opencl.so.1", f"libnvidia-opencl.so.{pkgver}")

    self.install_link("usr/lib/libnvidia-opticalflow.so.1", f"libnvidia-opticalflow.so.{pkgver}")
    self.install_link("usr/lib/libnvidia-opticalflow.so", f"libnvidia-opticalflow.so.1")

    self.install_link("usr/lib/libnvidia-ptxjitcompiler.so.1", f"libnvidia-ptxjitcompiler.so.{pkgver}")
    self.install_link("usr/lib/libnvidia-ptxjitcompiler.so", f"libnvidia-ptxjitcompiler.so.1")

    self.install_link("usr/lib/libnvidia-vksc-core.so.1", f"libnvidia-vksc-core.so.{pkgver}")

    self.install_dir("usr/lib/gbm")
    self.install_link("usr/lib/gbm/nvidia-drm_gbm.so", "../libnvidia-allocator.so.1")

    # firmware
    firmware_dir = f"usr/lib/firmware/nvidia/{pkgver}"

    for path in (self.cwd / _dir / "firmware").glob(f"*.bin"):
        self.install_files(path, firmware_dir)

    # ckms
    ckms_dir = f"usr/src/{pkgname}-{pkgver}"

    for file in (*(self.cwd / _dir / "kernel-open").iterdir(), self.files_path / "ckms.ini"):
        self.install_files(file, f"usr/src/{pkgname}-{pkgver}")


def post_install(self):
    self.install_license(self.cwd / _dir / "LICENSE")


@subpackage("nvidia-ckms")
def _(self):
    self.subdesc = "Nvidia kernel driver sources"
    self.install_if = [self.parent, "ckms"]
    self.depends = [
        self.parent,
        "ckms",
        "gmake",
    ]

    return ["usr/src"]
