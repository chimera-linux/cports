pkgname = "llama-cpp"
pkgver = "0.0.9518"
pkgrel = 0
build_style = "cmake"
make_check_args = [
    "-E",
    "(test-jinja-py|test-download-model|test-thread-safety|test-arg-parser|test-state-restore-fragmented|test-recurrent-state-rollback|test-save-load-state|test-eval-callback-download-model|test-eval-callback)",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "linux-headers",
    "ninja",
    "nodejs",
    "openssl3-devel",
    "pkgconf",
]
checkdepends = ["bash"]
pkgdesc = "LLM inference in C/C++"
license = "MIT"
url = "https://github.com/ggml-org/llama.cpp"
source = [
    f"{url}/archive/b{pkgver.split('.')[2]}.tar.gz",
    f"{url}/releases/download/b{pkgver.split('.')[2]}/llama-b{pkgver.split('.')[2]}-ui.tar.gz",
]
sha256 = [
    "dc665b803ffd495cd5bb75516806a182d79e78bcf093b0a80dfc00dc914b4814",
    "b3ce6b956263b48c444a2c0e221b030972c266597eed16f34e087e7d2cca07dd",
]


def post_extract(self):
    # Copy over precompiled UI
    with self.pushd(f"llama-b{pkgver.split('.')[2]}"):
        self.do("mkdir", f"../llama.cpp-b{pkgver.split('.')[2]}/tools/ui/dist")
        self.do(
            "cp",
            "bundle.css",
            f"../llama.cpp-b{pkgver.split('.')[2]}/tools/ui/dist/",
        )
        self.do(
            "cp",
            "bundle.js",
            f"../llama.cpp-b{pkgver.split('.')[2]}/tools/ui/dist/",
        )
        self.do(
            "cp",
            "index.html",
            f"../llama.cpp-b{pkgver.split('.')[2]}/tools/ui/dist/",
        )
        self.do(
            "cp",
            "loading.html",
            f"../llama.cpp-b{pkgver.split('.')[2]}/tools/ui/dist/",
        )
    self.cmake_dir = f"llama.cpp-b{pkgver.split('.')[2]}"


def post_install(self):
    self.install_license(f"llama.cpp-b{pkgver.split('.')[2]}/LICENSE")
